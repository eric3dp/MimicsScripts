
import trimatic
import numpy as np
import normals


def create_hollow_cylinder(
        solid, point, hollow,
        outer_cyl_radius, height, wall_thickness):

    # Creates a hollow cylinder at the specified
    # point and subtracts it from the mold.
    normal = -np.array(normals.find_closest_triangle_and_normal(hollow, point))

    # Calculate cylinder endpoints with
    # extra length for clean boolean operations
    point_forward = tuple(np.array(point) + (height + 1) * normal)
    point_backward = tuple(np.array(point) - (wall_thickness + 1) * normal)

    # Create outer shell of cylinder
    outer_cyl = trimatic.create_cylinder_part(
        point_1=tuple(np.array(point) - wall_thickness * normal),
        point_2=tuple(np.array(point) + height * normal),
        radius=outer_cyl_radius,
    )

    # Create inner cavity cylinder
    inner_cyl = trimatic.create_cylinder_part(
        point_1=point_backward,
        point_2=point_forward,
        radius=outer_cyl_radius - wall_thickness,
    )

    # Copy parts to prepare for booleans
    inner_cyl_copy = trimatic.duplicate(inner_cyl)
    solid = trimatic.duplicate(solid)
    # Boolean subtractions
    outer_cyl = trimatic.boolean_subtraction(outer_cyl, inner_cyl)
    outer_cyl = trimatic.boolean_subtraction(outer_cyl, solid)
    output = trimatic.boolean_subtraction(hollow, inner_cyl_copy)
    output = trimatic.boolean_union((output, outer_cyl))

    return output


def injection(mold):
    # Injection site dimensions
    filling_radius = 2.5
    filling_wall = 2
    filling_height = 4
    hollow = trimatic.duplicate(mold)
    hollow.name = f"{mold.name}_hollow"
    hollow = make_hollow(hollow)

    # point out where the injection site should go
    print("Place a point for the injection site")
    point = trimatic.indicate_coordinate()

    # Add injection site
    hollow = create_hollow_cylinder(
        mold,
        point,
        hollow,
        filling_radius + filling_wall,
        filling_height,
        filling_wall
    )

    # Add vents
    hollow = make_vents(mold, hollow)
    hollow = make_vents(mold, hollow)

    while trimatic.message_box("Do you need more vents?\
            Click Cancel when done.", ""):
        hollow = make_vents(mold, hollow)

    return mold


def make_vents(mold, hollow):
    # consider making this point choice directly on solid
    # to prevent extra holes if at odd angles
    # or more advanced logic to catch them and prevent
    print("Choose a point for the vent")
    vent_point = trimatic.indicate_coordinate()
    output = create_hollow_cylinder(
        mold, vent_point, hollow,
        outer_cyl_radius=2, height=2, wall_thickness=1
    )
    return output


def make_hollow(mold):
    # Parameters for hollowing
    hollow_distance = 0.5
    hollow_smallest_detail = 0.5
    hollow_smooth_factor = 0.5
    # duplicate solid interior
    mold_dupe = trimatic.duplicate(mold)

    # Create an offset hollow surface
    hollow_part = trimatic.hollow(
        entities=[mold],
        hollow_type=trimatic.HollowType.Outside,
        distance=hollow_distance,
        smallest_detail=hollow_smallest_detail,
        smooth_factor=hollow_smooth_factor,
    )
    # Make the surface into a part so Get_triangles will work
    hollow_part = trimatic.Surface.get_parent(hollow_part)
    # Merge hollow exterior with solid interior
    mold_dupe = trimatic.invert_normal(mold_dupe)
    hollow_part = trimatic.merge([hollow_part, mold_dupe])
    hollow_part.name = "hollow_part"
    return hollow_part


mold = trimatic.get_selection()[0]
injection(mold)
