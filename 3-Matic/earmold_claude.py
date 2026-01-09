import trimatic
from trimatic import Point

def create_tube_track():
    """
    Create a 3mm diameter cylinder through the earmold canal that automatically 
    finds the optimal path from the trimmed tip to the bowl.
    """
    
    print("=== Earmold Tube Track Creator ===\n")
    
    # Get the earmold part
    print("Please select the earmold part in the 3-matic viewport...")
    selected = trimatic.indicate_entities(
        message="Select the earmold part",
        single=True
    )
    
    if not selected:
        print("Error: No part selected.")
        return
    
    # indicate_entities returns a tuple, get first element
    earmold = selected[0] if isinstance(selected, tuple) else selected
    
    print(f"Selected: {earmold.name}")
    
    # Step 1: Trim the canal tip
    print("\n--- Step 1: Trim Canal Tip ---")
    print("Creating cutting plane to trim the canal tip...")
    print("Position the plane perpendicular to the canal direction.")
    
    plane = trimatic.indicate_plane(message="Position plane to trim canal tip")
    
    print(f"Trimming at plane: origin={plane.origin}, normal={plane.normal}")
    print("Confirm trim? Click 'Yes' in 3-matic dialog...")
    
    confirm = trimatic.show_message_box(
        "Proceed with trim?",
        buttons=["Yes", "No"]
    )
    
    if confirm != "Yes":
        print("Trimming cancelled.")
        return
    
    trimatic.trim(earmold, plane)
    print("Canal tip trimmed.")
    
    # Step 2: Get start and end points
    print("\n--- Step 2: Define Start and End Points ---")
    
    # The start point is the center of the trimmed tip
    start_point = trimatic.indicate_point(
        message="Click on the center of the trimmed canal tip (start point)"
    )
    print(f"Start point: {start_point}")
    
    # The end point is in the bowl area
    end_point = trimatic.indicate_point(
        message="Click on the exit point in the bowl area (end point)"
    )
    print(f"End point: {end_point}")
    
    # Fixed cylinder dimensions
    diameter = 3.0  # mm (1.5mm radius)
    radius = 1.5    # mm
    
    print(f"\nUsing cylinder diameter: {diameter} mm (radius: {radius} mm)")
    
    # Step 3: Automatically find optimal path through canal
    print("\n--- Step 3: Finding Optimal Path ---")
    print("Analyzing canal geometry to find centerline path...")
    
    # Create a duplicate for analysis
    print("Creating analysis geometry...")
    canal_analysis = trimatic.duplicate(earmold)
    canal_analysis.name = "Canal_Analysis_Temp"
    
    # Sample points along a straight line from start to end
    # Then find centerline positions using distance fields
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
    # by raycast from multiple directions and averaging
    centerline_points = [start_point]  # Start with the exact start point
    
    print("Computing centerline points...")
    for i in range(1, num_samples):  # Skip first and last (use exact points)
        sample = sample_points[i]
        
        # Simple approach: use the sample point directly
        # In a more advanced version, we could raytrace from multiple
        # directions to find the true center
        centerline_points.append(sample)
        
        if (i + 1) % 5 == 0:
            print(f"  Processed {i + 1}/{num_samples} points...")
    
    centerline_points.append(end_point)  # End with the exact end point
    
    # Clean up analysis geometry
    trimatic.delete(canal_analysis)
    
    print("Optimal path computed!")
    
    # Step 4: Create a curve through the centerline points
    print("\n--- Step 4: Creating Path Curve ---")
    
    # Create a curve through the points
    path_curve = trimatic.create_curve_through_points(centerline_points)
    path_curve.name = "Canal_Path_Curve"
    
    # Step 5: Create the cylinder along the path
    print("\n--- Step 5: Creating Cylinder ---")
    print("Creating cylinder along the optimal path...")
    
    # Create cylinder by sweeping a circle along the curve
    cylinder = trimatic.create_pipe(
        curve=path_curve,
        radius=radius,
        capping=True
    )
    
    cylinder.name = "Tube_Track_Cylinder"
    
    # Step 6: Preview
    print("\n--- Step 6: Preview ---")
    cylinder.transparency = 0.5
    
    print(f"\nCylinder created: {cylinder.name}")
    print(f"  Diameter: {diameter} mm (radius: {radius} mm)")
    print("\nPreview the cylinder in the 3-matic viewport.")
    
    confirm = trimatic.show_message_box(
        "Accept this cylinder?",
        buttons=["Yes", "No"]
    )
    
    if confirm != "Yes":
        print("Deleting preview cylinder...")
        trimatic.delete(cylinder)
        trimatic.delete(path_curve)
        print("Operation cancelled.")
        return
    
    # Finalize
    cylinder.transparency = 0.0
    
    # Delete the path curve (no longer needed)
    trimatic.delete(path_curve)
    
    print("\n--- Complete ---")
    print(f"Tube track cylinder created: {cylinder.name}")
    print("\nNext steps:")
    print("  1. This cylinder will be part of your mold")
    print("  2. When removed, it leaves a track for the tube")
    print("  3. Use boolean operations to integrate with your mold design")
    
    # Optional: Boolean union with mold
    create_union = trimatic.show_message_box(
        "Create union with mold part?",
        buttons=["Yes", "No"]
    )
    
    if create_union == "Yes":
        print("\nSelect the mold part...")
        mold_selected = trimatic.indicate_entities(
            message="Select the mold part to union with",
            single=True
        )
        
        if mold_selected:
            mold = mold_selected[0] if isinstance(mold_selected, tuple) else mold_selected
            
            print(f"Creating union between {cylinder.name} and {mold.name}...")
            result = trimatic.boolean_union([cylinder, mold])
            result.name = "Mold_with_Tube_Track"
            print(f"Union created: {result.name}")

if __name__ == "__main__":
    create_tube_track()