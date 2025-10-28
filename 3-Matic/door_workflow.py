import trimatic
import normals

# Step 1: Check if a part is selected, if not prompt user to select one
selection = trimatic.get_selection()
if len(selection) == 0 or not isinstance(selection[0], trimatic.Part):
    trimatic.message_box(
        message="Please select a part in the object tree, then press OK to continue.",
        title="Select a Part",
        with_cancel=False,
    )
    selection = trimatic.get_selection()
    if len(selection) == 0 or not isinstance(selection[0], trimatic.Part):
        print("Error: No part selected. Script terminated.")
        raise ValueError("A part must be selected to continue.")

selected_part = selection[0]
part_name = selected_part.name
print(f"Selected part: {selected_part.name}")

# Step 2: Activate trim tool with preserve_inner_and_outer method
print("Activating trim tool. Draw your trim outline and apply when ready...")
trimatic.activate_trim(
    entities=selected_part, trim_method=trimatic.TrimMethod.preserve_inner_and_outer
)
print(f"Trim completed on {part_name}")

# Step 3: Assign resulting parts to 'body' and 'door' variables
body = trimatic.find_part(f"{part_name}-1")
body.name = "body"
door = trimatic.find_part(f"{part_name}-2")
door.name = "door"
print(f"Parts created: {body.name} and {door.name}")

# Step 4: Find "side surface list" surface set in body and merge into a single surface in a new part
side_surface_set = body.find_surface_set("Side surface list")
if side_surface_set is None:
    print("Error: 'side surface list' surface set not found in body.")
    raise ValueError("Surface set 'side surface list' not found.")

# Get all surfaces from the surface set and merge them
side_surfaces = side_surface_set.get_surfaces()
merged_part = trimatic.merge(side_surfaces)
merged_part.name = "merged_sides"
print(f"Merged {len(side_surfaces)} surfaces into new part: {merged_part.name}")
newpart = trimatic.copy_to_part(merged_part)
newpart.name = "newpart"
hollow = newpart
# Step 5: Hollow the merged surfaces part
trimatic.hollow(
    entities=hollow, distance=1.1, hollow_type=trimatic.HollowType.Both, smooth_factor=0
)
hollow.name = "hollow"

print("Hollow operation completed.")

# Step 6: Subtract hollow from body and door
hollow_keep = trimatic.duplicate(hollow)
body_keep = trimatic.duplicate(body)
door_keep = trimatic.duplicate(door)
body_sub = trimatic.boolean_subtraction(body_keep, hollow_keep)
body_sub.name = "body_sub"
hollow_keep = trimatic.duplicate(hollow)
door_sub = trimatic.boolean_subtraction(door_keep, hollow_keep)
door_sub.name = "door_sub"
print("Subtraction operations completed.")

# Step 7: Intersect hollow with body and door
hollow_keep = trimatic.duplicate(hollow)
body_keep = trimatic.duplicate(body)
door_keep = trimatic.duplicate(door)
body_int = trimatic.boolean_intersection([body_keep, hollow_keep])
body_int.name = "body_int"
hollow_keep = trimatic.duplicate(hollow)
door_int = trimatic.boolean_intersection([door_keep, hollow_keep])
door_int.name = "door_int"
print("Intersection operations completed.")

# Step 8: Hide specified parts
hollow.visible = False
door.visible = False
door_sub.visible = False
door_int.visible = False
print("Parts hidden: hollow, door, door_sub, door_int")

# Step 9: Prompt user to indicate magnet points
print("Please indicate points where you want magnets. Press ESC when done.")
magnet_points = []
point_count = 0

while True:
    try:
        point = trimatic.indicate_coordinate()
        point_count += 1
        magnet_points.append(point)
        print(f"Magnet point {point_count} selected at: {point}")
    except:
        print(f"Total magnet points selected: {point_count}")
        break

# Step 10: Create cylinders at each magnet point and subtract from body_int and door_int
# Step 10: Create cylinders at each magnet point and subtract from body_int and door_int
cylinders = []

for i, point in enumerate(magnet_points, 1):
    # Get the normal of the closest triangle at this point
    normal = None

    # Try to get normal from body_int
    normal = normals.find_closest_triangle_and_normal(body_int, point)

    # If not found or too far, try door_int
    if normal is None:
        normal = normals.find_closest_triangle_and_normal(door_int, point)

    if normal is None:
        print(f"Warning: Could not find normal for point {i} at {point}. Skipping...")
        continue

    print(f"Normal for magnet {i}: {normal}")

    # Calculate cylinder endpoints (1.05mm in each direction from center point)
    point_1 = (
        point[0] - normal[0] * 1.05,
        point[1] - normal[1] * 1.05,
        point[2] - normal[2] * 1.05,
    )
    point_2 = (
        point[0] + normal[0] * 1.05,
        point[1] + normal[1] * 1.05,
        point[2] + normal[2] * 1.05,
    )

    # Create cylinder
    cylinder = trimatic.create_cylinder_part(
        point_1=point_1, point_2=point_2, radius=1.05
    )
    cylinder.name = f"magnet_{i}"
    cylinders.append(cylinder)
    print(f"Created cylinder for magnet {i}")

    # Subtract cylinder from body_int and door_int
    body_int = trimatic.subtract(body_int, cylinder)
    door_int = trimatic.subtract(door_int, cylinder)

print(f"Subtracted {len(cylinders)} magnet cylinders from body_int and door_int")

# Step 11: Move cylinders, body, and door to trash folder
trash_folder = trimatic.find_group("Trash")
if trash_folder is None:
    trash_folder = trimatic.create_group("Trash")

for cylinder in cylinders:
    cylinder.parent_group = trash_folder

body.parent_group = trash_folder
door.parent_group = trash_folder

print("Moved cylinders, body, and door to Trash folder.")
print("Script completed successfully!")
