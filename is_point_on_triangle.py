import numpy as np
from scipy.spatial import KDTree


def build_kd_tree(vertices, triangles):
    """Builds a KD-Tree using triangle centroids."""
    centroids = []
    for tri in triangles:
        A, B, C = vertices[tri[0]], vertices[tri[1]], vertices[tri[2]]
        centroid = (A + B + C) / 3  # Compute centroid
        centroids.append(centroid)

    return KDTree(centroids)


def find_nearby_triangles(kd_tree, query_point, max_triangles=10):
    """Finds the closest triangles to a given point."""
    _, indices = kd_tree.query(query_point, k=max_triangles)
    return indices  # Return indices of candidate triangles


def is_point_on_triangle(A, B, C, P):
    """Checks if point P is on triangle ABC using barycentric coordinates."""

    # Compute normal of the triangle
    AB = B - A
    AC = C - A
    normal = np.cross(AB, AC)

    # Check if P lies in the same plane as A, B, C
    AP = P - A
    if not np.isclose(np.dot(normal, AP), 0):  # Plane check
        return False

    # Compute barycentric coordinates
    v0 = C - A
    v1 = B - A
    v2 = P - A

    d00 = np.dot(v0, v0)
    d01 = np.dot(v0, v1)
    d11 = np.dot(v1, v1)
    d20 = np.dot(v2, v0)
    d21 = np.dot(v2, v1)

    denom = d00 * d11 - d01 * d01
    beta = (d11 * d20 - d01 * d21) / denom
    gamma = (d00 * d21 - d01 * d20) / denom
    alpha = 1 - beta - gamma

    return (0 <= alpha <= 1) and (0 <= beta <= 1) and (0 <= gamma <= 1)


def find_triangle_for_point(vertices, triangles, kd_tree, P):
    """Finds the triangle that contains point P."""

    # Get candidate triangles near P
    candidate_indices = find_nearby_triangles(kd_tree, P, max_triangles=10)

    # Check each candidate triangle
    for index in candidate_indices:
        tri = triangles[index]
        A, B, C = (
            np.array(vertices[tri[0]]),
            np.array(vertices[tri[1]]),
            np.array(vertices[tri[2]]),
        )

        if is_point_on_triangle(A, B, C, P):
            return index  # Return the triangle index if found

    return None  # Point is not on any triangle
