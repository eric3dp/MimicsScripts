import trimatic
import normals
import numpy as np

def canal(part):
    if isinstance(part, tuple):
        part = part[0]
    canal_radius = 1.75
    """
    Trim the canal tip. Use pre/post lists to get the new surface
    Use spheres to get the center point of the surface
    Get canal normal
    Use project point to find where it intersects the impression
    """
    print("Please trim the canal to the desired length")
    list_pre = trimatic.Part.get_surfaces(part)
    trimatic.activate_trim(part)
    list_post = trimatic.Part.get_surfaces(part)
    surface = [item for item in list_post if item not in list_pre] + [item for item in list_pre if item not in list_post]
    sphere1 = trimatic.create_sphere_fit(surface)
    sphere = trimatic.convert_analytical_to_mesh(sphere1)
    canal_point = trimatic.compute_center_of_gravity(sphere)
    trimatic.delete((sphere, sphere1))

    canal_normal = normals.find_closest_triangle_and_normal(part, canal_point)
    canal_reverse = tuple(-np.array(canal_normal))
    
    canal_contacts = trimatic.project_point(
        point_to_project=canal_point,
        direction=canal_reverse,
        parts=part,
        project_through=True
    )
    print("mark the exit point for the tube")
    exit_choice = trimatic.indicate_coordinate()
    canal_exit = canal_contacts[len(canal_contacts)-1]
    canal_line = trimatic.create_line(canal_point, canal_exit)
    move_dist = canal_line.length * 0.1
    x = 0
    new_max = canal_exit
    while x < 11:
        exit_line = trimatic.create_line(new_max, exit_choice)
        exit_line.name = f"Line_{x}"
        x = x + 1
        new_max = normals.move_point(
            new_max,
            canal_normal,
            move_dist
            )
    
""" 
    # this is the problem. max and min give corners of the bounding box not the literal object
    min = intersect.dimension_max
    max = intersect.dimension_min
    canal_line = trimatic.create_line(min, max)
    
    print("mark the exit point for the tube")
    exit_point = trimatic.indicate_coordinate()
    exit_normal = normals.find_closest_triangle_and_normal(part, exit_point)
    exit_point_moved = normals.move_point(exit_point, -np.array(exit_normal), 0.5)

    move_dist = canal_line.length * 0.1
    x = 0
    this_max = max
    while x < 11:
        
        new_max = normals.move_point(
            this_max,
            canal_normal,
            move_dist
            )
        del_cyl = trimatic.create_cylinder_part(exit_point_moved, new_max, 0.01)
        x = x + 1
        part_dup = trimatic.duplicate(part)
        trimatic.boolean_intersection((part_dup, del_cyl))
        this_max = new_max
        

    
"""

canal(trimatic.get_selection()[0])
