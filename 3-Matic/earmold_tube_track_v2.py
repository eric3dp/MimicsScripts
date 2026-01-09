import trimatic
import normals
import numpy as np

def create_tube_track():
    """
    Create a 3mm diameter cylinder through the earmold canal from the trimmed tip to the bowl.
    This cylinder will be part of your mold - when removed, it leaves a track for gluing the tube.
    """
    
    print("=== Earmold Tube Track Creator ===\n")
    
    # Get the earmold part from selection
    selection = trimatic.get_selection()
    if not selection or len(selection) == 0:
        trimatic.message_box(
            message="Please select the earmold part in the object tree, then click OK.",
            title="Select Earmold",
            with_cancel=False
        )
        selection = trimatic.get_selection()
        if not selection or len(selection) == 0:
            print("Error: No part selected. Exiting.")
            return
    
    earmold = selection[0]
    if isinstance(earmold, tuple):
        earmold = earmold[0]
    
    print(f"Selected: {earmold.name}")
    
    # Fixed cylinder dimensions
    cylinder_diameter = 3.0  # mm (1.5mm radius)
    cylinder_radius = 1.5
    
    print(f"Using cylinder diameter: {cylinder_diameter} mm (radius: {cylinder_radius} mm)")
    
    # Step 1: Trim the canal tip using activate_trim
    print("\n--- Step 1: Trim Canal Tip ---")
    print("Trim the canal to the desired length...")
    
    # Get surfaces before trim to identify the new surface after
    surfaces_before = trimatic.Part.get_surfaces(earmold)
    
    # Activate trim tool (user draws trim line interactively)
    trimatic.activate_trim(earmold)
    
    # Get surfaces after trim
    surfaces_after = trimatic.Part.get_surfaces(earmold)
    
    # Find the new surface created by the trim
    new_surface = [s for s in surfaces_after if s not in surfaces_before]
    if not new_surface:
        print("Error: No new surface found after trim. Exiting.")
        return
    
    trimmed_surface = new_surface[0]
    print(f"Trimmed surface identified: {trimmed_surface.name}")
    
    # Step 2: Find center point of trimmed tip using sphere fit
    print("\n--- Step 2: Finding Canal Start Point ---")
    
    # Fit an analytical sphere to the trimmed surface to find its center
    sphere_analytical = trimatic.create_sphere_fit(trimmed_surface)
    sphere_mesh = trimatic.convert_analytical_to_mesh(sphere_analytical)
    canal_start_point = trimatic.compute_center_of_gravity(sphere_mesh)
    
    print(f"Canal start point: {canal_start_point}")
    
    # Clean up sphere objects
    trimatic.delete((sphere_mesh, sphere_analytical))
    
    # Step 3: Get the canal normal at the start point
    print("\n--- Step 3: Finding Canal Direction ---")
    
    canal_normal = normals.find_closest_triangle_and_normal(earmold, canal_start_point)
    print(f"Canal normal: {canal_normal}")
    
    # Reverse the normal to point into the canal
    canal_direction = tuple(-np.array(canal_normal))
    
    # Step 4: Project through the canal to find potential exit points
    print("\n--- Step 4: Projecting Through Canal ---")
    
    canal_projection_points = trimatic.project_point(
        point_to_project=canal_start_point,
        direction=canal_direction,
        parts=earmold,
        project_through=True
    )
    
    if not canal_projection_points:
        print("Warning: Could not project through canal. Using manual exit point only.")
        canal_end_projection = canal_start_point
    else:
        # Get the furthest projection point
        canal_end_projection = canal_projection_points[-1]
        print(f"Found {len(canal_projection_points)} projection points through canal")
    
    # Step 5: User selects the exit point in the bowl
    print("\n--- Step 5: Select Exit Point ---")
    print("Click on the exit point in the bowl area where the tube should emerge...")
    
    trimatic.message_box(
        message="Click on the exit point in the bowl area (where tube emerges)",
        title="Select Exit Point",
        with_cancel=False
    )
    
    bowl_exit_point = trimatic.indicate_coordinate()
    print(f"Bowl exit point: {bowl_exit_point}")
    
    # Step 6: Create path points through the canal
    print("\n--- Step 6: Creating Path Through Canal ---")
    
    # Create a line from start to projected end to calculate segment distance
    path_line = trimatic.create_line(canal_start_point, canal_end_projection)
    segment_distance = path_line.length * 0.1  # 10% of path length per segment
    
    # Generate points along the canal direction
    path_points = [canal_start_point]
    current_point = canal_start_point
    
    # Create 10 intermediate points along the canal normal direction
    for i in range(10):
        current_point = normals.move_point(
            current_point,
            canal_direction,
            segment_distance
        )
        path_points.append(current_point)
    
    # Add the bowl exit point as the final point
    path_points.append(bowl_exit_point)
    
    print(f"Created path with {len(path_points)} points")
    
    # Step 7: Create curve through the path points
    print("\n--- Step 7: Creating Curve ---")
    
    path_curve = trimatic.create_curve(path_points, earmold)
    path_curve.name = "Tube_Path"
    
    print(f"Path curve created: {path_curve.name}")
    
    # Step 8: Create cylinder along the curve using circular_sweep
    print("\n--- Step 8: Creating Cylinder ---")
    print("Creating tube track cylinder along the path...")
    
    cylinder = trimatic.circular_sweep(
        sweep_paths=path_curve,
        sweep_diameter=cylinder_diameter,
        accuracy=0.01,
        round_begin=False,
        round_end=False
    )
    
    cylinder.name = "Tube_Track_Cylinder"
    cylinder.transparency = 0.5  # Semi-transparent for preview
    
    print(f"Cylinder created: {cylinder.name}")
    
    # Step 9: Show completion message
    print("\n--- Complete ---")
    
    trimatic.message_box(
        message=f"Tube track cylinder created!\n\n"
                f"Name: {cylinder.name}\n"
                f"Diameter: {cylinder_diameter} mm\n"
                f"Path points: {len(path_points)}\n\n"
                f"The cylinder is semi-transparent for preview.\n\n"
                f"Next steps:\n"
                f"1. Visually inspect the fit\n"
                f"2. Use boolean operations to integrate with your mold\n"
                f"3. When removed from cast, it leaves a track for the tube",
        title="Tube Track Complete",
        with_cancel=False
    )
    
    print(f"\nTube track cylinder created: {cylinder.name}")
    print("Next steps:")
    print("  1. Inspect the cylinder fit visually")
    print("  2. Set transparency to 0 if satisfied: cylinder.transparency = 0")
    print("  3. Use boolean union/subtraction with your mold part")
    print("  4. When silicone cast is made, removing this cylinder leaves tube track")
    
    return cylinder, path_curve

if __name__ == "__main__":
    try:
        create_tube_track()
    except Exception as e:
        print(f"\nError occurred: {e}")
        import traceback
        traceback.print_exc()
