import trimatic
import numpy as np
import math


def debug_cotton_detection():
    """
    Debug version - stops after sphere intersection to inspect results
    """
    print("\n=== Cotton Detection Debug ===\n")

    # Import STL file
    stl_path = r"C:\Users\bradened\OneDrive - Arkansas Children's\3D Files" \
        r"\AMU\Models\ACH25-331 - EarMold01\ACH25-331 LowerJawScan3.stl"
    print(f"Importing STL: {stl_path}")

    try:
        imported = trimatic.import_part_stl(stl_path)
        print(f"Imported: {imported.name}")
        earmold = imported
    except Exception as e:
        print(f"Import failed: {e}")
        print("Trying to use selected part instead...")

        # Fallback to selection
        selection = trimatic.get_selection()
        if not selection or len(selection) == 0:
            print("Error: No part selected and import failed.")
            return

        earmold = selection[0]

    print(f"Working with: {earmold.name}")

    # Create geometry curves to find rough areas
    print("\nCreating geometry curves (30° angle)...")
    rough_curves = trimatic.create_geometry_curve_angle_based(
        entities=earmold, angle=30.0
    )

    if not rough_curves:
        print("No rough areas detected")
        return

    if not isinstance(rough_curves, tuple):
        rough_curves = [rough_curves]

    print(f"Found {len(rough_curves)} rough area curves")

    # Filter by length - only short curves (<1mm)
    print("\nFiltering for short curves (<1mm)...")
    curve_centroids = []
    max_curve_length = 1.0

    for i, curve in enumerate(rough_curves):
        try:
            points = curve.points

            if points and len(points) > 0:
                # Calculate curve length
                curve_length = 0.0
                for j in range(len(points) - 1):
                    p1 = points[j]
                    p2 = points[j + 1]
                    segment_length = math.sqrt(
                        (p2[0] - p1[0]) ** 2
                        + (p2[1] - p1[1]) ** 2
                        + (p2[2] - p1[2]) ** 2
                    )
                    curve_length += segment_length

                if curve_length <= max_curve_length:
                    avg_x = sum(p[0] for p in points) / len(points)
                    avg_y = sum(p[1] for p in points) / len(points)
                    avg_z = sum(p[2] for p in points) / len(points)
                    curve_centroids.append((avg_x, avg_y, avg_z))
                elif i < 5:
                    print(f"  Skipping long curve {i}: \
                           length = {curve_length:.2f} mm")
        except Exception as e:
            if i < 5:
                print(f"  Warning: Could not process curve {i}: {e}")
            continue

    print(f"Extracted {len(curve_centroids)} short curves")

    if len(curve_centroids) < 10:
        print("Not enough short curves found")
        trimatic.delete(rough_curves)
        return

    # Find densest cluster
    print("\nFinding densest cluster...")
    cluster_radius = 5.0
    max_density = 0
    # densest_point = None
    cluster_points = []

    for point in curve_centroids:
        density = 0
        nearby_points = []
        for other_point in curve_centroids:
            distance = math.sqrt(
                (point[0] - other_point[0]) ** 2
                + (point[1] - other_point[1]) ** 2
                + (point[2] - other_point[2]) ** 2
            )
            if distance < cluster_radius:
                density += 1
                nearby_points.append(other_point)

        if density > max_density:
            max_density = density
            # densest_point = point
            cluster_points = nearby_points

    print(f"Found cluster with {max_density} curves within {cluster_radius}mm")

    if max_density <= 20:
        print("Cluster not dense enough (need >20 curves)")
        trimatic.delete(rough_curves)
        return

    # Calculate cluster center
    cluster_center = (
        sum(p[0] for p in cluster_points) / len(cluster_points),
        sum(p[1] for p in cluster_points) / len(cluster_points),
        sum(p[2] for p in cluster_points) / len(cluster_points),
    )

    print(f"Cluster center: {cluster_center}")

    # Calculate cluster radius
    max_dist = 0.0
    for point in cluster_points:
        dist = math.sqrt(
            (point[0] - cluster_center[0]) ** 2
            + (point[1] - cluster_center[1]) ** 2
            + (point[2] - cluster_center[2]) ** 2
        )
        if dist > max_dist:
            max_dist = dist

    sphere_radius = max_dist * 1.1
    print(f"\nCreating sphere: radius = {sphere_radius:.2f} mm")

    # Create sphere
    test_sphere = trimatic.create_sphere_center_radius(
        center_point=cluster_center, radius=sphere_radius
    )

    test_sphere_mesh = trimatic.convert_analytical_to_mesh(test_sphere)

    # Create intersection curve
    print("Creating intersection curve with earmold...")
    intersection_curves = trimatic.create_intersection_curve(
        entity_set1=test_sphere_mesh,
        entity_set2=earmold, intersection_curve_in=2
    )

    if not intersection_curves:
        print("ERROR: No intersection curve found!")
        trimatic.delete((test_sphere, test_sphere_mesh))
        trimatic.delete(rough_curves)
        return

    # Extract curve data before deleting anything
    if isinstance(intersection_curves, tuple):
        max_curve = None
        max_length = 0
        for c in intersection_curves:
            try:
                if c.points and len(c.points) > max_length:
                    max_length = len(c.points)
                    max_curve = c
            except:
                continue
        boundary_curve = max_curve
    else:
        boundary_curve = intersection_curves

    if not boundary_curve:
        print("ERROR: Could not find valid boundary curve")
        trimatic.delete((test_sphere, test_sphere_mesh))
        trimatic.delete(rough_curves)
        return

    curve_points = boundary_curve.points

    print(f"Intersection curve has {len(curve_points)} points")

    # Calculate boundary center
    boundary_center = (
        sum(p[0] for p in curve_points) / len(curve_points),
        sum(p[1] for p in curve_points) / len(curve_points),
        sum(p[2] for p in curve_points) / len(curve_points),
    )

    print(f"Boundary center: {boundary_center}")

    # Calculate curve normal
    p1 = np.array(curve_points[0])
    p2 = np.array(curve_points[len(curve_points) // 3])
    p3 = np.array(curve_points[2 * len(curve_points) // 3])

    v1 = p2 - p1
    v2 = p3 - p1

    normal = np.cross(v1, v2)
    normal_length = np.linalg.norm(normal)

    if normal_length < 0.001:
        print("ERROR: Could not calculate curve normal")
        trimatic.delete((test_sphere, test_sphere_mesh))
        trimatic.delete(rough_curves)
        return

    canal_normal = normal / normal_length

    # Check direction
    vec_to_boundary = np.array(boundary_center) - np.array(cluster_center)

    if np.dot(canal_normal, vec_to_boundary) < 0:
        canal_normal = -canal_normal
        print("Flipped normal to point into canal")

    canal_direction = tuple(canal_normal)

    print(f"\nCanal direction: {canal_direction}")

    # Create visual markers
    print("\n=== Creating Visual Markers ===")

    # Red sphere at cluster center
    marker_cluster = trimatic.create_sphere_part(cluster_center, radius=1.0)
    marker_cluster.name = "DEBUG_ClusterCenter_RED"
    marker_cluster.color = (1, 0, 0)

    # Blue sphere at boundary center
    marker_boundary = trimatic.create_sphere_part(boundary_center, radius=1.0)
    marker_boundary.name = "DEBUG_BoundaryCenter_BLUE"
    marker_boundary.color = (0, 0, 1)

    # Green line showing canal direction
    canal_endpoint = (
        boundary_center[0] + canal_direction[0] * 10,
        boundary_center[1] + canal_direction[1] * 10,
        boundary_center[2] + canal_direction[2] * 10,
    )
    marker_line = trimatic.create_line(boundary_center, canal_endpoint)
    marker_line.name = "DEBUG_CanalDirection_GREEN"

    # Keep the intersection curve visible
    if isinstance(intersection_curves, tuple):
        for i, c in enumerate(intersection_curves):
            c.name = f"DEBUG_IntersectionCurve_{i}"
    else:
        intersection_curves.name = "DEBUG_IntersectionCurve"

    # Delete the sphere (but keep curves and markers)
    # trimatic.delete((test_sphere, test_sphere_mesh))

    # Delete rough curves (cleanup)
    # trimatic.delete(rough_curves)

    print("\n=== DONE ===")
    print("Inspect the scene:")
    print("  RED sphere = cotton ball center")
    print("  BLUE sphere = boundary center (where sphere intersects canal)")
    print("  GREEN line = canal direction")
    print("  Intersection curves = boundary between cotton and canal")
    print("\nDoes the green line point INTO the canal correctly?")


if __name__ == "__main__":
    try:
        debug_cotton_detection()
    except Exception as e:
        print(f"\nError: {e}")
        import traceback

        traceback.print_exc()
