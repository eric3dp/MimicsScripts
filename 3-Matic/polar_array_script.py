import trimatic

# Get the entities
cylinder = trimatic.find_part("Cylinder-001")
disk = trimatic.find_part("ACH25-331_2nd")

# Get the center point of the disk to use as rotation axis origin
disk_center = trimatic.compute_center_of_gravity(disk)

# Define the rotation axis (perpendicular to the disk - assuming Z-axis)
# If your disk is oriented differently, change this direction vector
axis_direction = (0, 0, 1)  # Z-axis

# Define the polar array parameters
num_holes = 8  # Number of holes around the circle (change as needed)
angle_between = 360.0 / num_holes  # Degrees between each copy

# Create the polar array using rotate with number_of_copies
# This will create additional copies of the cylinder rotated around the center
rotated_cylinders = trimatic.rotate(
    entities=cylinder,
    angle_deg=angle_between,
    axis_origin=disk_center,
    axis_direction=axis_direction,
    number_of_copies=num_holes - 1  # -1 because we already have the original
)

print(f"Created polar array with {num_holes} cylinders")
print(f"Each cylinder is {angle_between} degrees apart")
print(f"Center point: {disk_center}")
