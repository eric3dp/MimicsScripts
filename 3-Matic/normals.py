import trimatic


def calculate_triangle_normal(v1, v2, v3):
    """
    Calculate the normal vector of a triangle given three vertices.
    Uses the cross product of two edge vectors.

    Args:
        v1, v2, v3: trimatic.Point objects or tuples of (x, y, z) coordinates

    Returns:
        Tuple of (nx, ny, nz) representing the normalized normal vector
    """
    # Convert points to tuples if needed
    if hasattr(v1, "x"):
        v1 = (v1.x, v1.y, v1.z)
    if hasattr(v2, "x"):
        v2 = (v2.x, v2.y, v2.z)
    if hasattr(v3, "x"):
        v3 = (v3.x, v3.y, v3.z)

    # Calculate two edge vectors
    edge1 = (v2[0] - v1[0], v2[1] - v1[1], v2[2] - v1[2])
    edge2 = (v3[0] - v1[0], v3[1] - v1[1], v3[2] - v1[2])

    # Calculate cross product
    nx = edge1[1] * edge2[2] - edge1[2] * edge2[1]
    ny = edge1[2] * edge2[0] - edge1[0] * edge2[2]
    nz = edge1[0] * edge2[1] - edge1[1] * edge2[0]

    # Normalize the vector
    length = (nx**2 + ny**2 + nz**2) ** 0.5
    if length > 0:
        nx /= length
        ny /= length
        nz /= length

    return (nx, ny, nz)


def find_closest_triangle_and_normal(part, point):
    """
    Find the closest triangle to a point and return its normal.

    Args:
        part: trimatic.Part object
        point: Tuple of (x, y, z) coordinates

    Returns:
        Tuple of (nx, ny, nz) representing the normal vector, or None if not found
    """
    # Get all triangles and vertices from the part
    points, triangles = part.get_triangles()

    if len(triangles) == 0:
        return None

    min_distance = float("inf")
    best_normal = None

    for triangle in triangles:
        # Get the three vertices of the triangle (indices into points list)
        v1 = points[triangle[0]]
        v2 = points[triangle[1]]
        v3 = points[triangle[2]]

        # Convert to coordinate tuples if they're Point objects
        if hasattr(v1, "x"):
            v1_coords = (v1.x, v1.y, v1.z)
            v2_coords = (v2.x, v2.y, v2.z)
            v3_coords = (v3.x, v3.y, v3.z)
        else:
            v1_coords = v1
            v2_coords = v2
            v3_coords = v3

        # Calculate centroid of triangle
        centroid = (
            (v1_coords[0] + v2_coords[0] + v3_coords[0]) / 3.0,
            (v1_coords[1] + v2_coords[1] + v3_coords[1]) / 3.0,
            (v1_coords[2] + v2_coords[2] + v3_coords[2]) / 3.0,
        )

        # Calculate distance from point to centroid
        distance = (
            (point[0] - centroid[0]) ** 2
            + (point[1] - centroid[1]) ** 2
            + (point[2] - centroid[2]) ** 2
        ) ** 0.5

        # If this is the closest triangle so far, calculate its normal
        if distance < min_distance:
            min_distance = distance
            best_normal = calculate_triangle_normal(v1, v2, v3)

    return best_normal
