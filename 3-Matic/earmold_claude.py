import trimatic
from trimatic import Point, Vector
import math

def create_tube_track():
    """
    Create a 3mm diameter cylinder through the earmold canal that automatically 
    finds the optimal path from the trimmed tip to the bowl.
    """
    
    print("=== Earmold Tube Track Creator ===\n")
    
    # Get the earmold part
    parts = trimatic.get_parts()
    if not parts:
        print("Error: No parts found in the project.")
        return
    
    print("Available parts:")
    for i, part in enumerate(parts):
        print(f"  {i+1}. {part.name}")
    
    part_idx = int(input("\nSelect earmold part number: ")) - 1
    earmold = parts[part_idx]
    
    print(f"\nSelected: {earmold.name}")
    
    # Step 1: Trim the canal tip
    print("\n--- Step 1: Trim Canal Tip ---")
    print("Please select a plane to trim the canal tip.")
    print("TIP: Use a cutting plane perpendicular to the canal direction.")
    input("Press Enter when you've positioned the cutting plane...")
    
    plane = trimatic.indicate_plane()
    
    print(f"Trimming at plane: origin={plane.origin}, normal={plane.normal}")
    confirm = input("Proceed with trim? (y/n): ")
    
    if confirm.lower() != 'y':
        print("Trimming cancelled.")
        return
    
    trimatic.trim(earmold, plane)
    print("Canal tip trimmed.")
    
    # Step 2: Get start and end points
    print("\n--- Step 2: Define Start and End Points ---")
    
    # The start point is the center of the trimmed tip
    print("Click on the center of the trimmed canal tip (start point)...")
    start_point = trimatic.indicate_point()
    print(f"Start point: {start_point}")
    
    # The end point is in the bowl area
    print("Click on the exit point in the bowl area (end point)...")
    end_point = trimatic.indicate_point()
    print(f"End point: {end_point}")
    
    # Fixed cylinder dimensions
    diameter = 3.0  # mm (1.5mm radius)
    radius = 1.5    # mm
    
    print(f"\nUsing cylinder diameter: {diameter} mm (radius: {radius} mm)")
    
    # Step 3: Automatically find optimal path through canal
    print("\n--- Step 3: Finding Optimal Path ---")
    print("Analyzing canal geometry to find centerline path...")
    
    # Create a shrinkwrap of the canal interior to work with
    print("Creating analysis geometry...")
    canal_analysis = trimatic.duplicate(earmold)
    canal_analysis.name = "Canal_Analysis_Temp"
    
    # Strategy: Use medial axis or centerline detection
    # The canal is essentially a tube, so we want to find its centerline
    
    try:
        # Option 1: Try to use skeletonization/medial axis
        print("Computing canal centerline...")
        
        # Create a medial axis (skeleton) of the canal
        # This gives us the centerline through the canal automatically
        skeleton = trimatic.create_skeleton(canal_analysis)
        
        # Extract the branch of the skeleton that connects start to end
        print("Extracting path from start to end...")
        path_curve = trimatic.extract_skeleton_branch(
            skeleton=skeleton,
            start_point=start_point,
            end_point=end_point
        )
        
    except (AttributeError, Exception) as e:
        # Fallback: Use distance field method
        print("Using distance field method...")
        
        # Sample points along a straight line from start to end
        # Then project them to the canal centerline using distance fields
        num_samples = 20
        sample_points = []
        
        for i in range(num_samples + 1):
            t = i / num_samples
            sample = Point(
                start_point.x + t * (end_point.x - start_point.x),
                start_point.y + t * (end_point.y - start_point.y),
                start_point.z + t * (end_point.z - start_point.z)
            )
            sample_points.append(sample)
        
        # For each sample point, find the centerline position
        # by finding the point that maximizes distance to the canal walls
        centerline_points = []
        
        print("Computing centerline points...")
        for i, sample in enumerate(sample_points):
            # Find the point near this sample that's furthest from walls
            # Use a search sphere around the sample point
            search_radius = 5.0  # mm
            
            # Get the maximum inscribed sphere at this location
            center = trimatic.find_max_inscribed_sphere_center(
                part=canal_analysis,
                search_point=sample,
                search_radius=search_radius
            )
            
            centerline_points.append(center)
            
            if (i + 1) % 5 == 0:
                print(f"  Processed {i + 1}/{num_samples + 1} points...")
        
        # Create a smooth curve through the centerline points
        path_curve = trimatic.create_curve_through_points(centerline_points)
        
        # Smooth the curve to avoid sharp corners
        path_curve = trimatic.smooth_curve(path_curve, smoothing_factor=0.7)
    
    # Clean up analysis geometry
    trimatic.delete(canal_analysis)
    
    print("Optimal path computed!")
    
    # Step 4: Create the cylinder along the optimal path
    print("\n--- Step 4: Creating Cylinder ---")
    print("Creating cylinder along the optimal path...")
    
    cylinder = trimatic.create_pipe_along_curve(
        curve=path_curve,
        diameter=diameter,
        smooth=True
    )
    
    cylinder.name = "Tube_Track_Cylinder"
    
    # Step 5: Verify clearance
    print("\n--- Step 5: Checking Clearance ---")
    print("Verifying cylinder fits within canal...")
    
    # Check if cylinder intersects with earmold walls
    clearance_check = trimatic.measure_distance(cylinder, earmold)
    min_clearance = clearance_check.minimum_distance
    
    print(f"Minimum clearance to canal walls: {min_clearance:.2f} mm")
    
    if min_clearance < 0:
        print("WARNING: Cylinder intersects with canal walls!")
        print(f"The 3mm diameter cylinder is too large for this canal.")
    elif min_clearance < 0.3:
        print("WARNING: Very tight fit - clearance < 0.3mm")
    else:
        print("Clearance looks good!")
    
    # Step 6: Preview
    print("\n--- Step 6: Preview ---")
    cylinder.transparency = 0.5
    trimatic.color_part(cylinder, color=(0, 255, 0))  # Green
    
    print(f"\nCylinder created: {cylinder.name}")
    print(f"  Diameter: {diameter} mm (radius: {radius} mm)")
    print(f"  Minimum clearance: {min_clearance:.2f} mm")
    print("\nPreview the cylinder in the 3-matic viewport.")
    
    confirm = input("\nAccept this cylinder? (y/n): ")
    
    if confirm.lower() != 'y':
        print("Deleting preview cylinder...")
        trimatic.delete(cylinder)
        print("Operation cancelled.")
        return
    
    # Finalize
    cylinder.transparency = 0.0
    print("\n--- Complete ---")
    print(f"Tube track cylinder created: {cylinder.name}")
    print("\nNext steps:")
    print("  1. This cylinder will be part of your mold")
    print("  2. When removed, it leaves a track for the tube")
    print("  3. Use boolean operations to integrate with your mold design")
    
    # Optional: Boolean union with mold
    create_union = input("\nCreate union with mold part? (y/n): ")
    if create_union.lower() == 'y':
        print("\nSelect the mold part:")
        mold_parts = [p for p in trimatic.get_parts() if p != earmold and p != cylinder]
        for i, part in enumerate(mold_parts):
            print(f"  {i+1}. {part.name}")
        
        if mold_parts:
            mold_idx = int(input("Select mold part number: ")) - 1
            mold = mold_parts[mold_idx]
            
            print(f"Creating union between {cylinder.name} and {mold.name}...")
            result = trimatic.boolean_union([cylinder, mold])
            result.name = "Mold_with_Tube_Track"
            print(f"Union created: {result.name}")

if __name__ == "__main__":
    create_tube_track()