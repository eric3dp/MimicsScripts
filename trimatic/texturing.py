import pymatic
import trimatic.utils

import os

def create_uv_based_rectangular_pattern_with_deformation(
    *args,
    uv_map,
    pattern_entity,
    margin_u = 0.2000,
    margin_v = 0.2000,
    preserve_pattern_height = False,
    height_offset = 0.0000,
    preserve_boundary_entity = True):
    """ Patterns the entity across the UV Map with deformation in the output.

    :param uv_map: Parameterized entity to be used as the patterning guide.
    :type uv_map: trimatic.UVMap
    :param pattern_entity: One part to be patterned across the parameterized surface.
    :type pattern_entity: trimatic.Part
    :param margin_u: The distance between the pattern entities in the U direction in UV units.
    :type margin_u: float, optional
    :param margin_v: The distance between the pattern entities in the U direction in UV units.
    :type margin_v: float, optional
    :param preserve_pattern_height: If True, preserve the original pattern entity height in the patterned output.
    :type preserve_pattern_height: bool, optional
    :param height_offset: The distance between the bottom of the pattern entity and the surface with the UV Map on.
    :type height_offset: float, optional
    :param preserve_boundary_entity: If True, all the partial pattern entities are preserved in the final output.
    :type preserve_boundary_entity: bool, optional

    :return: One part with the output of the patterning operation.
    :rtype: trimatic.Part
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/texturing/create_uv_based_rectangular_pattern_with_deformation.py
    """


    trimatic.utils.check_type("uv_map", uv_map, (trimatic.UVMap))
    trimatic.utils.check_type("pattern_entity", pattern_entity, (trimatic.Part))
    trimatic.utils.check_param_in_range("margin_u", margin_u, 0.0000, 0.9999)
    trimatic.utils.check_param_in_range("margin_v", margin_v, 0.0000, 0.9999)

    return pymatic.create_uv_based_rectangular_pattern_with_deformation(uv_map, pattern_entity, margin_u, margin_v,
                                                                        preserve_pattern_height, height_offset,
                                                                        preserve_boundary_entity)

def create_uv_based_rectangular_pattern_without_deformation(
    uv_map,
    pattern_entity,
    height_offset = 0.0000,
    preserve_boundary_entity = True):
    """ Create rectangular pattern entities based on a UV Map without any deformation.

    :param uv_map: Parameterized entity to be used as the patterning guide.
    :type uv_map: trimatic.UVMap
    :param pattern_entity: One part to be patterned across the parameterized surface
    :type pattern_entity: trimatic.Part
    :param height_offset: The distance between the bottom of the pattern entity and the surface with the UV Map on.
    :type height_offset: float, optional
    :param preserve_boundary_entity: If True, all the partial pattern entities are preserved in the final output.
    :type preserve_boundary_entity: bool, optional

    :return: One part with the output of the patterning operation.
    :rtype: trimatic.Part
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/texturing/create_uv_based_rectangular_pattern_without_deformation.py
    """


    trimatic.utils.check_type("uv_map", uv_map, (trimatic.UVMap))
    trimatic.utils.check_type("pattern_entity", pattern_entity, (trimatic.Part))

    return pymatic.create_uv_based_rectangular_pattern_without_deformation(uv_map, pattern_entity, height_offset , preserve_boundary_entity)

def create_fade_texture(
    *args,
    texture,
    fading_guides,
    is_black = True,
    influence_distance = 1.0000,
    fading_factor = 1.0000):
    """ Fades the texture images to the defined color and distance based on the input guiding curves.

    :param texture: A single texture to be applied with fading.
    :type texture: trimatic.Texture
    :param fading_guides: One or multiple guide curves for the fading lines. Heterogeneous list of entities is allowed.
    :type fading_guides: trimatic.Curve | trimatic.SurfaceContour | trimatic.SurfaceBorder | [trimatic.Curve | trimatic.SurfaceContour | trimatic.SurfaceBorder]
    :param is_black: The color that the fading operation should fade to. If True, the fade color will be set to black, else will be white.
    :type is_black: bool, optional
    :param influence_distance: The distance of the regions influenced by the fading operation in XYZ coordinate system.
    :type influence_distance: float, optional
    :param fading_factor: The intensity of the fading at the position of the fading guide.
    :type fading_factor: float, optional
    
    :return: One or more faded textures.
    :rtype: trimatic.Texture | (trimatic.Texture)
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/texturing/create_fade_texture.py
    """


    trimatic.utils.check_type("texture", texture, (trimatic.Texture))
    trimatic.utils.check_type("fading_guides", fading_guides, (trimatic.Curve, trimatic.SurfaceContour, trimatic.SurfaceBorder))
    trimatic.utils.check_resolution("influence_distance", influence_distance)
    trimatic.utils.check_resolution("fading_factor", fading_factor)

    return pymatic.create_fade_texture(texture, trimatic.utils.single_or_multiple_entities(fading_guides), is_black, influence_distance, fading_factor)

def create_uv_based_texture(
    uv_maps,
    image_path,
    tile_image = True
    ) :
    """ Create UV Based Texture on the selected UV Maps.

    :param uv_maps: Parameterized entities to be textured.
    :type uv_maps: trimatic.UVMap | [trimatic.UVMap]
    :param image_path: Path to the texture image file in the user’s computer. Supported image formats are: .bmp, .jpeg, .gif, .png, .tiff.
    :type image_path: string
    :param tile_image: If True, the tile will be repeated in all the UV boxes in the UV Map.
    :type tile_image: bool, optional

    :return: Newly created textures in the selected UV Maps.
    :rtype: trimatic.Texture | (trimatic.Texture)
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/texturing/create_uv_based_texture.py
    """


    trimatic.utils.check_type("uv_maps", uv_maps, (trimatic.UVMap))
    if os.path.isfile(image_path):
        return pymatic.create_uv_based_texture(trimatic.utils.single_or_multiple_entities(uv_maps), image_path, tile_image)
    else:
        raise FileNotFoundError('Unable to open file ' + image_path)

def create_uv_based_texture_preserve_aspect_ratio(
    uv_maps,
    image_path,
    is_by_width = True,
    tile_image = True
    ) :
    """ Create UV Based Texture on the selected UV Maps while preserving the aspect ratio based on the image aspect ratio.

    :param uv_maps: Parameterized entities to be textured.
    :type uv_maps: trimatic.UVMap | [trimatic.UVMap]
    :param image_path: Path in the computer to the image file. Supported image formats are: .bmp, .jpeg, .gif, .png, .tiff.
    :type image_path: string
    :param is_by_width: If set to True, the region will be preserved by Width (U). If set to False, the region will be preserved by Height (V).
    :type is_by_width: bool, optional
    :param tile_image: If True, the image texture is tiled.
    :type tile_image: bool, optional

    :return: One or more textured objects.
    :rtype: trimatic.Texture | (trimatic.Texture)
    :raises: ValueError | RuntimeError
    
    :example:

    .. literalinclude:: example/texturing/create_uv_based_texture_preserve_aspect_ratio.py
    """
        

    trimatic.utils.check_type("uv_maps", uv_maps, (trimatic.UVMap))
    if os.path.isfile(image_path):
        return pymatic.create_uv_based_texture_preserve_aspect_ratio(trimatic.utils.single_or_multiple_entities(uv_maps), image_path, is_by_width, tile_image)
    else:
        raise FileNotFoundError('Unable to open file ' + image_path)

def set_texture_properties(
    entities,
    white_offset,
    black_offset,
    accuracy):
    """ Sets the texture properties.

    :param entities: Either a single object or a heterogeneous list of entities.
    :type entities: trimatic.UVMap | trimatic.Texture | [trimatic.UVMap | trimatic.Texture]
    :param white_offset: The white offset value for 3D texture.
    :type white_offset: float
    :param black_offset: The black offset value for 3D Texture.
    :type black_offset: float
    :param accuracy: The accuracy for the slice-based texture operations.
    :type accuracy: float

    :return: Textures with properties edited.
    :rtype: trimatic.Texture | (trimatic.Texture)
    :raises: ValueError

    :example:

    .. literalinclude:: example/texturing/set_texture_properties.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Texture, trimatic.UVMap))
    trimatic.utils.check_resolution("black_offset", accuracy)

    return pymatic.set_texture_properties(trimatic.utils.single_or_multiple_entities(entities), white_offset, black_offset, accuracy)

def convert_texture_to_mesh(entities, detail_size):
    """Converts textures to mesh.

    Input entities are grouped by the parts they belong to. For every group, a new part will be created.
    To control texture offsets, use set_texture_properties.

    :param entities: Either a single object or heterogenous list of entities.
    :type entities: trimatic.Part | trimatic.UVMap | trimatic.UVRegion | trimatic.Texture | [trimatic.Part | trimatic.UVRegion | trimatic.UVMap | trimatic.Texture]
    :param detail_size: The resolution at which the texture will be processed to generate the mesh.
    :type detail_size: float

    :return: Newly created part(s).
    :rtype: (trimatic.Part)
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/texturing/convert_texture_to_mesh.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.UVRegion, trimatic.UVMap, trimatic.Texture))
    trimatic.utils.check_resolution("detail_size", detail_size)

    return pymatic.convert_texture_to_mesh(trimatic.utils.single_or_multiple_entities(entities), detail_size)


def create_procedural_leather_texture(
    *args,
    entities,
    texture_resolution = 1000,
    primary_cell_size=1.0000,
    fading_factor=0.1500,
    is_apply_spots = False,
    is_round_cells = False,
    secondary_cell_size_factor=1.0000,
    secondary_cell_intensity=1.0000):
    """Create and apply leather texture procedurally to the desired UV Map(s).

    :param entities: Part(s) with UV Map(s) to be applied with a leather texture.
    :type entities: trimatic.Part | trimatic.UVMap | [trimatic.Part | trimatic.UVMap]
    :param texture_resolution: The resolution of the procedural texture bitmap.
    :type texture_resolution: (int)
    :param primary_cell_size: The main voronoi cell sizes.
    :type primary_cell_size: (float)
    :param fading_factor: The fading factor of the voronoi cells' lines to the center of cell. Useful for generating different kinds of bump profiles for the voronoi cells.
    :type fading_factor: (float)
    :param is_apply_spots: If True, adds spots to the leather texture.
    :type is_apply_spots: (bool)
    :param is_round_cells: If True, voronoi cell lines will be smoothed to create more organic cells.
    :type is_round_cells: (bool)
    :param secondary_cell_size_factor: The factor of the secondary voronoi cells relative to the primary voronoi cells. When set to 1, no secondary cells will be generated.
    :type secondary_cell_size_factor: (float)
    :param secondary_cell_intensity: The intensity of the secondary voronoi cell pixels in the final image texture.
    :type secondary_cell_intensity: (float)

    :return: A tuple of Texture(s) generated by the operation. 
    :rtype: (trimatic.Texture)
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/texturing/create_procedural_leather_texture.py
    """


    trimatic.utils.check_param_smaller_or_equal("texture_resolution", texture_resolution, 16000)
    trimatic.utils.check_param_in_range("fading_factor", fading_factor, 0.001, 0.4)
    trimatic.utils.check_param_in_range("secondary_cell_size_factor", secondary_cell_size_factor, trimatic.utils.get_resolution(), 1)
    trimatic.utils.check_param_smaller_or_equal("secondary_cell_intensity", secondary_cell_intensity, 1)
    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.UVMap))

    return pymatic.create_procedural_leather_texture(trimatic.utils.single_or_multiple_entities(entities),
                                                     texture_resolution,
                                                     primary_cell_size,
                                                     fading_factor,
                                                     is_apply_spots,
                                                     is_round_cells,
                                                     secondary_cell_size_factor,
                                                     secondary_cell_intensity)
