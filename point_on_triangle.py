import numpy as np
import trimesh


def to_mesh(input_mesh):
    vertices, triangles = map(np.array, input_mesh)
    mesh = trimesh.Trimesh(vertices=vertices, faces=triangles, process=False)
    return mesh


def find_triangle(mesh, point):
    point = np.array(point)
    # shoot ray from point in arbitrary direction
    ray_origin = point.reshape(1, 3)
    ray_direction = np.array([[0, 0, 1]])
    # find the first triangle it intersects
    intersection_index = mesh.ray.intersects_first(
        ray_origins=ray_origin, ray_directions=ray_direction
    )
    if intersection_index >= 0:
        # get the triangle vertices
        triangle_indices = mesh.faces[intersection_index].flatten()
        A, B, C = triangle_indices
        # look for point in the triangle
#        if trimesh.intersections.point_in_polygon(point, [A, B, C]):
    return triangle_indices
#    return None


def find_rotation(triangle, normal_start):
    """
    Parameters:
    - triangle: list of 3 points that form target triangle
    - normal_start: normal of part to rotate

    Returns:
    - Tuple of angle, axis_direction, and normal
    """
    A, B, C = triangle
    AB = B - A
    AC = C - A
    normal_finish = np.cross(AB, AC)

    axis_direction = np.cross(normal_start, normal_finish)
    axis_direction = axis_direction / np.linalg.norm(axis_direction)
    cos_theta = np.dot(normal_start, normal_finish) / (
        np.linalg.norm(normal_start) * np.linalg.norm(normal_finish)
    )
    theta = np.arccos(np.clip(cos_theta, -1.0, 1.0))
    angle = np.degrees(theta)
    return angle, axis_direction, normal_finish
