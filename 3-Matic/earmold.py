import trimatic
import normals
import numpy as np

# TO-DO:
# - replace "find parts" and hardcoded name with initial selection
# - add scan plane cutting, filleting
# - add scan clean-up/smoothing
# - add initial hollowing
# - automate creation of tube
# - add automation for hearing vent in canal
# - clean it all up so it makes sense
#
# DONE:
# - silicone injection port and vents automated

selected = trimatic.get_selection()
i = 0
points = [0, 0, 0]
while i < 3:
    points[i] = trimatic.indicate_coordinate()
    i += 1
plane = trimatic.create_plane_3_points(
    point1=points[0], point2=points[1], point3=points[2]
)
impression = trimatic.cut(selected, plane)
msg = trimatic.message_box("Please select the part to keep", "Keep")
earmold = trimatic.duplicate(trimatic.get_selection())
trimatic.delete(impression)
trimatic.delete(earmold.find_surface_set("Cutting plane"))
trimatic.fill_hole_freeform(earmold.get_bad_contours(), tangent=True)
vector = np.array(plane.normal) * -2  # 2mm
trimatic.translate(plane, vector)
trimatic.cut(earmold, plane)
trimatic.delete(plane)
earmold2 = earmold
msg = trimatic.message_box("Please select the part to keep", "Keep")
earmold = trimatic.duplicate(trimatic.get_selection())

trimatic.delete(earmold2)


def create_hollow_cylinder(mold, point, outer_radius, height, wall_thickness):
    """Creates a hollow cylinder at the specified
    point and subtracts it from the mold."""
    normal = -np.array(normals.find_closest_triangle_and_normal(mold, point))

    # Calculate cylinder endpoints with
    # extra length for clean boolean operations
    point_forward = tuple(np.array(point) + (height + 1) * normal)
    point_backward = tuple(np.array(point) - (wall_thickness + 1) * normal)

    # Create outer shell
    outer = trimatic.create_cylinder_part(
        point_1=tuple(np.array(point) - wall_thickness * normal),
        point_2=tuple(np.array(point) + height * normal),
        radius=outer_radius,
    )

    # Create inner cavity
    inner = trimatic.create_cylinder_part(
        point_1=point_backward,
        point_2=point_forward,
        radius=outer_radius - wall_thickness,
    )

    # Subtract from parts
    earmold_copy = trimatic.duplicate(
        trimatic.find_parts("Earmold_before-tube"))
    inner_copy = trimatic.duplicate(inner)

    outer = trimatic.boolean_subtraction(outer, earmold_copy)
    outer = trimatic.boolean_subtraction(outer, inner)
    mold = trimatic.boolean_subtraction(mold, inner_copy)

    return mold


def injection(mold, point):
    # Injection site dimensions
    filling_radius = 2.5
    filling_wall = 2
    filling_height = 4

    mold = create_hollow_cylinder(
        mold,
        point,
        filling_radius + filling_wall,
        filling_height,
        filling_wall
    )

    # Add vents
    mold = make_vents(mold)
    mold = make_vents(mold)

    while trimatic.message_box("Do you need more vents?", ""):
        mold = make_vents(mold)

    return mold


def make_vents(mold):
    vent_point = trimatic.indicate_coordinate()
    return create_hollow_cylinder(
        mold, vent_point, outer_radius=2, height=2, wall_thickness=1
    )


"""
# Request a part selection if nothing is selected
premold = trimatic.get_selection()
if len(premold) == 0:
    trimatic.message_box("Please select a part", "No part selected")

earmold = trimatic.get_selection()[0]
print("Select where you'd like the injection port")
point = trimatic.indicate_coordinate()
mold = injection(earmold, point)

print("Complete")
"""
