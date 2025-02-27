import pymatic
import trimatic.utils

import os

from enum import Enum

def exit():
    """Exits 3-matic. Calling this function has the same effect as closing 3-matic's main window. 
    When called through an external IDE setup, 
    an exception can be raised in case the connection to 3-matic was closed before being able to receive the answer to the function call.
    

    :example:

    .. literalinclude:: example/file/exit.py
    """



    return pymatic.exit()

class ExportOption(Enum):
    """Export Option."""

    surface_mesh = "Export surface mesh"
    volume_mesh = "Export volume mesh"
    surface_and_volume_mesh = "Export surface and volume mesh"

class FaceSplitMethod(Enum):
    """Face Split Method."""

    split_by_surface = "By surface"
    split_by_part = "By part"
    split_by_surface_set = "By surface set"
    split_by_shell = "By shell"

class TypeOfElement(Enum):
      element_type_C3D10 = "C3D10"
      element_type_C3D10M = "C3D10M"

class TypeOfBeam(Enum):
      beam_type_linear = "Linear"
      beam_type_quadratic = "Quadratic"

def export_3mf(entities, filename):
    """Exports the specified parts to a 3mf file.

    :param entities: Part or list of parts to export.
    :type entities: trimatic.Part | (trimatic.Part)
    :param filename: Filename
    :type filename: string
    :return: Filename of the file that was written.
    :rtype: string
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/file/export_3mf.py
    """
    if filename is None or not trimatic.utils.check_file_saveable(filename):
         raise ValueError('Invalid file name')

    trimatic.utils.check_type("entities", entities, (trimatic.Part))
    return pymatic.export_3mf(trimatic.utils.single_or_multiple_entities(entities), filename )

def export_abaqus(
        entities, 
        output_directory,
        export_surface = True,
        volume_element_type = None,
        graph_beam_type = None,
        face_split_method = FaceSplitMethod.split_by_surface,
        create_assembly = True
     ):
    """Exports the specified parts as ABAQUS files.

    :param entities: Part or list of parts to export.
    :type entities: trimatic.Part | (trimatic.Part)
    :param output_directory: Destination path to save the files. One file is created per part. The file name will be the name of the part followed by the extension '.inp'.
    :type output_directory: string
    :param export_surface: A boolean value which indicates whether the surface needs to be exported.
    :type export_surface: bool, optional
    :param volume_element_type: A value which indicates the type of volume mesh for exporting. When specifying None, the volume is not exported.
    :type volume_element_type:  trimatic.TypeOfElement, optional
    :param graph_beam_type: A value which indicates the type of graph structure for exporting. When specifying None, the graph structure is not exported.
    :type  graph_beam_type: trimatic.TypeOfBeam, optional
    :param face_split_method: A value which indicates the face split method.
    :type face_split_method: trimatic.FaceSplitMethod, optional
    :param create_assembly: A boolean value which indicates wheather an assembly needs to be created.
    :type create_assembly: bool, optional
    :return: Tuple of paths to the ABAQUS files.
    :rtype: (string)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/file/export_abaqus.py
    """
    trimatic.utils.check_folder_path_is_valid(output_directory)

    trimatic.utils.check_type("entities", entities, (trimatic.Part))
    trimatic.utils.check_type("face_split_method", face_split_method, (FaceSplitMethod,))

    volume_element_type_value = None
    graph_beam_type_value = None

    if volume_element_type != None:
       trimatic.utils.check_type("volume_element_type", volume_element_type, (TypeOfElement,))
       volume_element_type_value = volume_element_type.value

    if graph_beam_type != None:
       trimatic.utils.check_type("graph_beam_type", graph_beam_type, (TypeOfBeam,))
       graph_beam_type_value = graph_beam_type.value

    return pymatic.export_abaqus(trimatic.utils.single_or_multiple_entities(entities), output_directory, 
                                 export_surface, face_split_method.value, volume_element_type_value, 
                                 graph_beam_type_value, create_assembly)

def export_abaqus_single_output(
        entities, 
        filename,
        export_surface = True,
        volume_element_type = None,
        graph_beam_type = None,
        face_split_method = FaceSplitMethod.split_by_surface
     ):
    """Exports the specified parts and/or points to a single ABAQUS file.
    An assembly will be created.

    :param entities: One or more parts and/or points to export.
    :type entities: trimatic.Part | trimatic.Point | (trimatic.Part | trimatic.Point)
    :param filename: The output filename of the file with extension '.inp'.
    :type filename: string
    :param export_surface: A boolean value which indicates whether the surface needs to be exported.
    :type export_surface: bool, optional
    :param volume_element_type: A value which indicates the type of volume mesh for exporting. When specifying None, the volume is not exported.
    :type volume_element_type:  trimatic.TypeOfElement, optional
    :param graph_beam_type: A value which indicates the type of graph structure for exporting. When specifying None, the graph structure is not exported.
    :type  graph_beam_type: trimatic.TypeOfBeam, optional
    :param face_split_method: A value which indicates face split method.
    :type face_split_method: trimatic.FaceSplitMethod, optional
    :return: Tuple of paths to the ABAQUS files.
    :rtype: (string)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/file/export_abaqus_single_output.py
    """
    if filename is None or not trimatic.utils.check_file_saveable(filename):
        raise ValueError('Invalid file name')

    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Point))
    trimatic.utils.check_type("face_split_method", face_split_method, (FaceSplitMethod,))

    volume_element_type_value = None
    graph_beam_type_value = None

    if volume_element_type != None:
       trimatic.utils.check_type("volume_element_type", volume_element_type, (TypeOfElement,))
       volume_element_type_value = volume_element_type.value

    if graph_beam_type != None:
       trimatic.utils.check_type("graph_beam_type", graph_beam_type, (TypeOfBeam,))
       graph_beam_type_value = graph_beam_type.value

    return pymatic.export_abaqus_single_output(trimatic.utils.single_or_multiple_entities(entities), filename, 
                                               export_surface, face_split_method.value, volume_element_type_value, 
                                               graph_beam_type_value)

def export_analysis(entities, output_directory):
    """Exports one or more analyses to file(s).

    :param entities: Analysis to export
    :type entities: trimatic.Analysis | [trimatic.Analysis]
    :param output_directory: Directory to export to. Unique file names will be generated based on the name of the analysis.
    :type output_directory: string
    :return: Tuple of paths to the written files.
    :rtype: (string)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/file/export_analysis.py
    """
    trimatic.utils.check_folder_path_is_valid(output_directory)

    trimatic.utils.check_type("entities", entities, (trimatic.Analysis))

    return pymatic.export_analysis(trimatic.utils.single_or_multiple_entities(entities), output_directory)

def export_ansys(
        entities, 
        output_directory, 
        export_option = ExportOption.surface_mesh, 
        face_split_method = FaceSplitMethod.split_by_surface, 
     ):
    """Exports the specified parts as an ANSYS file

    :param entities: Part or list of parts to export.
    :type entities: trimatic.Part | (trimatic.Part)
    :param output_directory: Destination path to save the file(s). One file is created per part. The file name will be the name of the part followed by the extension '.cdb'.
    :type output_directory: string
    :param export_option: A value which indicates whether the surface mesh, the volume mesh, or both, need to be exported.
    :type export_option: trimatic.ExportOption, optional
    :param face_split_method: A value which indicates face split method (when surfaces are exported).
    :type face_split_method: trimatic.FaceSplitMethod, optional
    :return: Tuple of paths to the ansys files.
    :rtype: (string)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/file/export_ansys.py
    """
    trimatic.utils.check_folder_path_is_valid(output_directory)

    trimatic.utils.check_type("entities", entities, (trimatic.Part))
    trimatic.utils.check_type("export_option", export_option, (ExportOption,))
    trimatic.utils.check_type("face_split_method", face_split_method, (FaceSplitMethod,))

    return pymatic.export_ansys(trimatic.utils.single_or_multiple_entities(entities), output_directory, 
                                 export_option.value, face_split_method.value)

def export_comsol(
        entities, 
        output_directory, 
        export_option = ExportOption.surface_mesh, 
        face_split_method = FaceSplitMethod.split_by_surface
     ):
    """Exports the specified parts as a comsol file.

    :param entities: Part or list of parts to export.
    :type entities: trimatic.Part | (trimatic.Part)
    :param output_directory: Destination path to save the files. One file is created per part. The file name will be the name of the part followed by the extension '.mphxt'.
    :type output_directory: string
    :param export_option: A value which indicates whether the surface mesh, the volume mesh, or both, need to be exported.
    :type export_option: trimatic.ExportOption, optional
    :param face_split_method: A value which indicates face split method (when surfaces are exported).
    :type face_split_method: trimatic.FaceSplitMethod, optional
    :return: Tuple of paths to the comsol files.
    :rtype: (string)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/file/export_comsol.py
    """
    trimatic.utils.check_folder_path_is_valid(output_directory)

    trimatic.utils.check_type("entities", entities, (trimatic.Part))
    trimatic.utils.check_type("export_option", export_option, (ExportOption,))
    trimatic.utils.check_type("face_split_method", face_split_method, (FaceSplitMethod,))

    return pymatic.export_comsol(trimatic.utils.single_or_multiple_entities(entities), output_directory, 
                                 export_option.value, face_split_method.value)

def export_curves_and_primitives(entities, filename):
    """Exports curves and primitives to an XML file.

    :param entities: One or more curves and/or primitives to export.
    :type entities: trimatic.Curve | trimatic.Line | trimatic.Point | trimatic.Plane | trimatic.Arc | trimatic.Cylinder | trimatic.Cone | trimatic.Sphere | [trimatic.Curve | trimatic.Line | trimatic.Point | trimatic.Plane | trimatic.Arc | trimatic.Cylinder | trimatic.Cone | trimatic.Sphere]
    :param filename: Filename
    :type filename: string
    :return: Name of the written file.
    :rtype: string
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/file/export_curves_and_primitives.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Curve, trimatic.Line, trimatic.Point, trimatic.Plane, trimatic.Arc, trimatic.Cylinder, trimatic.Cone, trimatic.Sphere))
    if filename is None or not trimatic.utils.check_file_saveable(filename):
        raise ValueError('Invalid file name')

    return pymatic.export_curves_and_primitives(trimatic.utils.single_or_multiple_entities(entities), filename)

def export_fluent(
        entities, 
        output_directory, 
        export_option = ExportOption.surface_mesh, 
        face_split_method = FaceSplitMethod.split_by_surface
     ):
    """Exports the specified parts as FLUENT files.

    :param entities: Part or list of parts to export.
    :type entities: trimatic.Part | (trimatic.Part)
    :param output_directory: Destination path to save the files. One file is created per part. The file name will be the name  of the part followed by the extension '.msh'.
    :type output_directory: string
    :param export_option: A value which indicates whether the surface mesh, the volume mesh, or both, need to be exported.
    :type export_option: trimatic.ExportOption, optional
    :param face_split_method: A value which indicates face split method (when surfaces are exported).
    :type face_split_method: trimatic.FaceSplitMethod, optional
    :return: Tuple of paths to the FLUENT files.
    :rtype: (string)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/file/export_fluent.py
    """
    trimatic.utils.check_folder_path_is_valid(output_directory)

    trimatic.utils.check_type("entities", entities, (trimatic.Part))
    trimatic.utils.check_type("export_option", export_option, (ExportOption,))
    trimatic.utils.check_type("face_split_method", face_split_method, (FaceSplitMethod,))

    return pymatic.export_fluent(trimatic.utils.single_or_multiple_entities(entities), output_directory, 
                                 export_option.value, face_split_method.value)

def export_iges(entities, output_directory, patching = True):
    """Exports the specified parts to iges files.

    :param entities: Part or list of parts to export.
    :type entities: trimatic.Part | (trimatic.Part)
    :param output_directory: Destination path to save the file(s).
    :type output_directory: string
    :param patching: If True, the part will first be subdivided in patches with default parameters. If you want more control over patching, use trimatic.automatic_rectangular_patching.
    :type patching: bool, optional
    :return: Names of written files.
    :rtype: (string)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/file/export_iges.py
    """

    trimatic.utils.check_folder_path_is_valid(output_directory)

    trimatic.utils.check_type("entities", entities, (trimatic.Part))

    return pymatic.export_iges(trimatic.utils.single_or_multiple_entities(entities), output_directory, patching )

def export_mdck(entities, filename):
    """Export a single MDCK file.

    :param entities: Part or list of parts to export.
    :type entities: trimatic.Part | (trimatic.Part)
    :param filename: Filename
    :type filename: string
    :return: Filename of the file that was written.
    :rtype: string
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/file/export_mdck.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part))
    if filename is None or not trimatic.utils.check_file_saveable(filename):
         raise ValueError('Invalid file name')

    return pymatic.export_mdck(trimatic.utils.single_or_multiple_entities(entities), filename)

def export_measurements_to_xml(entities, filename):
    """Exports measurements to an XML file.

    :param entities: One or more measurements to export.
    :type entities: trimatic.Annotation | trimatic.AngleMeasurement | trimatic.DiameterMeasurement | trimatic.DistanceMeasurement | [trimatic.Annotation | trimatic.AngleMeasurement | trimatic.DiameterMeasurement | trimatic.DistanceMeasurement]
    :param filename: Filename
    :type filename: string
    :return: Filename of the file that was written.
    :rtype: string
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/file/export_measurements_to_xml.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Annotation, trimatic.AngleMeasurement, trimatic.DiameterMeasurement, trimatic.DistanceMeasurement))
    if filename is None or not trimatic.utils.check_file_saveable(filename):
        raise ValueError('Invalid file name')

    return pymatic.export_measurements_to_xml(trimatic.utils.single_or_multiple_entities(entities), filename)

def export_nastran(
        entities, 
        output_directory,
        export_surface = True,
        export_volume = False,
        export_graph = False,
        face_split_method = FaceSplitMethod.split_by_surface
     ):
    """Exports the specified parts as Nastran files.

    :param entities: Part or list of parts to export.
    :type entities: trimatic.Part | (trimatic.Part)
    :param output_directory: Destination path to save the files. One file is created per part. The file name will be the name of the part followed by the extension '.nas'.
    :type output_directory: string
    :param export_surface: A boolean value which indicates whether the surface(s) need to be exported.
    :type export_surface: bool, optional
    :param export_volume: A boolean value which indicates whether the volume(s) need to be exported. 
    :type export_volume:  bool, optional
    :param export_graph: A boolean value which indicates whether the graphs need to be exported.
    :type export_graph: bool, optional
    :param face_split_method: A value which indicates the face split method.
    :type face_split_method: trimatic.FaceSplitMethod, optional
    :return: Tuple of paths to the Nastran files.
    :rtype: (string)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/file/export_nastran.py
    """
    trimatic.utils.check_folder_path_is_valid(output_directory)

    trimatic.utils.check_type("entities", entities, (trimatic.Part))
    trimatic.utils.check_type("face_split_method", face_split_method, (FaceSplitMethod,))
        
    return pymatic.export_nastran(trimatic.utils.single_or_multiple_entities(entities), output_directory, 
                                 export_surface, export_volume, export_graph, face_split_method.value)

def export_obj(entities, filename, units = 1000):
    """Exports the specified parts to an .obj file.

    :param entities: Part or list of parts to export.
    :type entities: trimatic.Part | (trimatic.Part)
    :param filename: Filename
    :type filename: string
    :param units: Units to which file must be written. 1 for mm, 1000 for meters, etc.
    :type units: float, optional
    :return: Filename of the file that was written.
    :rtype: string
    :raises: ValueError, RuntimeError
    :example:

    .. literalinclude:: example/file/export_obj.py	

    """

    trimatic.utils.check_type("entities", entities, (trimatic.Part))
    trimatic.utils.check_resolution('units', units)

    return pymatic.export_obj(trimatic.utils.single_or_multiple_entities(entities), filename, units)

def export_patran(
        entities, 
        output_directory,
        export_surface = True
     ):
    """Exports the specified parts as Patran files.

    :param entities: Part or list of parts to export.
    :type entities: trimatic.Part | (trimatic.Part)
    :param output_directory: Destination path to save the files. One file is created per part. The file name will be the name of the part followed by the extension '.out'.
    :type output_directory: string
    :param export_surface: A boolean value which indicates whether the surface(s) need to be exported. If False, only the volume(s) will be exported.
    :type export_surface: bool, optional
    :return: Tuple of paths to the Patran files.
    :rtype: (string)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/file/export_patran.py
    """
    trimatic.utils.check_folder_path_is_valid(output_directory)

    trimatic.utils.check_type("entities", entities, (trimatic.Part))

    return pymatic.export_patran(trimatic.utils.single_or_multiple_entities(entities), output_directory, 
                                 export_surface )

def export_pdf(entities, filename, header_image = None, header_height = 40, footer_image = None, footer_height = 40):
    """Exports the specified entities to 3D pdf file.

    :param entities: Entities to export.
    :type entities: trimatic.Part | trimatic.Line | trimatic.Point | trimatic.Plane | trimatic.Annotation | trimatic.DiameterMeasurement | trimatic.DistanceMeasurement | trimatic.AngleMeasurement | [trimatic.Object]
    :param filename: Filename
    :type filename: string
    :param header_image: Filename of image to be used for header.
    :type header_image: string, optional
    :param header_height: Height of the header in mm.
    :type header_height: float, optional
    :param footer_image: Filename of image to be used for the footer.
    :type footer_image: string, optional
    :param footer_height: Height of the footer in mm.
    :type footer_height: float, optional
    :return: Filename of the file that was written.
    :rtype: string
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/file/export_pdf.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Line, trimatic.Point, trimatic.Plane, trimatic.Annotation, trimatic.DiameterMeasurement, trimatic.DistanceMeasurement, trimatic.AngleMeasurement ))

    return pymatic.export_pdf(trimatic.utils.single_or_multiple_entities(entities), filename, header_image, header_height, footer_image, footer_height)

def export_screen_capture(filename):
    """Exports the Work Area to an image file. The format is determined by the file name extension. 
    Supported formats/extensions are: .bmp, .jpeg, .gif, .png, and .tiff.

    :param filename: Filename
    :type filename: string
    :return: Upon success, returns the name of the written file.
    :rtype: string
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/file/export_screen_capture.py
    """



    if filename is None or not trimatic.utils.check_file_saveable(filename):
        raise ValueError('Invalid file name')

    return pymatic.export_screen_capture(filename)

def export_step(entities, output_directory, patching = True):
    """Exports the specified parts to step files.

    :param entities: Part or list of parts to export.
    :type entities: trimatic.Part | (trimatic.Part)
    :param output_directory: Destination path to save the file(s).
    :type output_directory: string
    :param patching: If True, the part will first be subdivided into patches with default parameters. If you want more control over the patching, it is recommended to use trimatic.automatic_rectangular_patching.
    :type patching: bool, optional
    :return: Names of written files.
    :rtype: (string)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/file/export_step.py
    """

    trimatic.utils.check_folder_path_is_valid(output_directory)

    trimatic.utils.check_type("entities", entities, (trimatic.Part))

    return pymatic.export_step(trimatic.utils.single_or_multiple_entities(entities), output_directory, patching )

def export_stl_binary(entities, output_directory, include_color = False):
    """Exports the specified part(s) as a binary STL file.

    :param entities: Part or list of parts to export.
    :type entities: trimatic.Part | (trimatic.Part)
    :param output_directory: Destination path to save the file(s).
    :type output_directory: string
    :param include_color: If True, triangle color information is included in the exported part.
    :type include_color: bool, optional
    :return: Tuple of paths to the STL files.
    :rtype: (string)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/file/export_stl_binary.py
    """
    trimatic.utils.check_folder_path_is_valid(output_directory)

    trimatic.utils.check_type("entities", entities, (trimatic.Part))

    return pymatic.export_stl_binary(trimatic.utils.single_or_multiple_entities(entities), output_directory, include_color)


def export_stl_ascii(entities, output_directory, include_surface_structure = False):
    """Exports the specified part(s) as an ASCII STL file.

    :param entities: Part or list of parts to export.
    :type entities: trimatic.Part | (trimatic.Part)
    :param output_directory: Destination path to save the file(s).
    :type output_directory: string
    :param include_surface_structure: If True, surfaces information is included in the export.
    :type include_surface_structure: bool, optional
    :return: Tuple of paths to the STL files.
    :rtype: (string)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/file/export_stl_ascii.py
    """
    trimatic.utils.check_folder_path_is_valid(output_directory)

    trimatic.utils.check_type("entities", entities, (trimatic.Part))

    return pymatic.export_stl_ascii(trimatic.utils.single_or_multiple_entities(entities), output_directory, include_surface_structure)

def export_transformation_matrix(entity, target_entity, filename):
    """Exports the transformation between two entities to a text file.

    This function allows you to export a .txt file containing the transformation matrix that aligns the object coordinate system of an entity (start position) to that of a target entity (final position). 
    A summary of the rotations and translations described by the matrix is also included.

    :param entity: Entity whose OCS is the start position.
    :type entity: trimatic.Part
    :param target_entity: Entity whose OCS is the final position.
    :type target_entity: trimatic.Part
    :param filename: Filename
    :type filename: string
    :return: Filename of the file that was written.
    :rtype: string
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/file/export_transformation_matrix.py
    """


    trimatic.utils.check_type("entity", entity, (trimatic.Part))
    trimatic.utils.check_type("target_entity", target_entity, (trimatic.Part))
    if filename is None or not trimatic.utils.check_file_saveable(filename):
         raise ValueError('Invalid file name')

    return pymatic.export_transformation_matrix(entity, target_entity, filename)

def export_vrml(entities, filename, units = 1000):
    """Exports the specified parts to a .vrml file.

    :param entities: Part or list of parts to export.
    :type entities: trimatic.Part | (trimatic.Part)
    :param filename: Filename
    :type filename: string
    :param units: Units to which file must be written. 1 for mm, 1000 for meters, etc.
    :type units: float, optional
    :return: Filename of the file that was written.
    :rtype: string
    :raises: ValueError, RuntimeError
    :example:

    .. literalinclude:: example/file/export_vrml.py
    """
    if filename is None or not trimatic.utils.check_file_saveable(filename):
         raise ValueError('Invalid file name')

    trimatic.utils.check_type("entities", entities, (trimatic.Part))
    trimatic.utils.check_resolution('units', units)

    return pymatic.export_vrml(trimatic.utils.single_or_multiple_entities(entities), filename, units)

def export_x3d(entities, filename):
    """Exports the specified parts to a X3D file.

    :param entities: Part or list of parts to export.
    :type entities: trimatic.Part | (trimatic.Part)
    :param filename: Filename
    :type filename: string
    :return: Filename of the file that was written.
    :rtype: string
    :raises: ValueError, RuntimeError
    :example:

    .. literalinclude:: example/file/export_x3d.py

    """
    if filename is None or not trimatic.utils.check_file_saveable(filename):
         raise ValueError('Invalid file name')

    trimatic.utils.check_type("entities", entities, (trimatic.Part))
    return pymatic.export_x3d(trimatic.utils.single_or_multiple_entities(entities), filename )

def export_zpr(entities, output_directory):
    """Exports the specified parts as ZPR files.

    :param entities: Part or list of parts to export. Colors defined on surfaces will be exported.
    :type entities: trimatic.Part | (trimatic.Part)
    :param output_directory: Destination path to save the files. One file is created per part. The file name will be the name of the part followed by the extension '.zpr'.
    :type output_directory: string
    :return: Tuple of the path to the ZPR files.
    :rtype: (string)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/file/export_zpr.py
    """
    trimatic.utils.check_folder_path_is_valid(output_directory)

    trimatic.utils.check_type("entities", entities, (trimatic.Part))
    return pymatic.export_zpr(trimatic.utils.single_or_multiple_entities(entities), output_directory )

def get_application_path():
    """Gets the path where 3-matic is installed. This can be useful, for example to locate the DemoFiles folder or the UnitCellLibrary.

    :return: The full path to the application executable file.
    :rtype: string

    :example:

    .. literalinclude:: example/file/get_application_path.py
    """

    return pymatic.get_application_path()

def import_3dm(filename, surface_accuracy = 0.01):
    """Import a single .3dm file.

    :param filename: Path to the file to import.
    :type filename: string
    :param surface_accuracy: The maximum allowed distance deviation between the CAD file and the triangulation.
    :type surface_accuracy: float, optional

    :return: Tuple with imported parts.
    :rtype: (trimatic.Part)
    :raises: FileNotFoundError, RuntimeError

    :example:

    .. literalinclude:: example/file/import_3dm.py
    """


    trimatic.utils.check_resolution('surface_accuracy', surface_accuracy)

    if os.path.isfile(filename):
        return pymatic.import_3dm(filename, surface_accuracy)
    else:
        raise FileNotFoundError('Unable to open file ' + filename)

def import_3mf(filename):
    """Import a 3mf file.

    :param filename: Path to the file to import.
    :type filename: string
    :return: Tuple with imported parts.
    :rtype: (trimatic.Part)
    :raises: FileNotFoundError, RuntimeError

    :example:

    .. literalinclude:: example/file/import_3mf.py
    """


    if os.path.isfile(filename):
        return pymatic.import_3mf(filename)
    else:
        raise FileNotFoundError('Unable to open file ' + filename)

def import_adam(filename):
    """Import an ADaM file.

    :param filename: Path to the file to import.
    :type filename: string

    :return: imported SSM object.
    :rtype: trimatic.SSM
    :raises: FileNotFoundError, RuntimeError

    :example:

    .. literalinclude:: example/file/import_adam.py
    """


    if os.path.isfile(filename):
        return pymatic.import_adam(filename)
    else:
        raise FileNotFoundError('Unable to open file ' + filename)

def import_catia5(filename, surface_accuracy = 0.01):
    """Import a single .CATPart or .CATProduct file.

    :param filename: Path to the file to import.
    :type filename: string
    :param surface_accuracy: The maximum allowed distance deviation between the CAD file and the triangulation.
    :type surface_accuracy: float, optional

    :return: Tuple with imported parts.
    :rtype: (trimatic.Part)
    :raises: FileNotFoundError, RuntimeError

    :example:

    .. literalinclude:: example/file/import_catia5.py
    """


    trimatic.utils.check_resolution('surface_accuracy', surface_accuracy)

    if os.path.isfile(filename):
        return pymatic.import_catia5(filename, surface_accuracy)
    else:
        raise FileNotFoundError('Unable to open file ' + filename)

def import_iges(filename, surface_accuracy = 0.01, layer_to_part = True):
    """Import a single .igs or .iges file.

    :param filename: Path to the file to import.
    :type filename: string
    :param surface_accuracy: The maximum allowed distance deviation between the CAD file and the triangulation.
    :type surface_accuracy: float, optional
    :param layer_to_part: When True: all the entities which are grouped in one layer, will be grouped in one part.
    :type layer_to_part: bool, optional

    :return: Tuple with imported parts.
    :rtype: (trimatic.Part)
    :raises: FileNotFoundError, RuntimeError

    :example:

    .. literalinclude:: example/file/import_iges.py
    """


    trimatic.utils.check_resolution('surface_accuracy', surface_accuracy)

    if os.path.isfile(filename):
        return pymatic.import_iges(filename, surface_accuracy, layer_to_part)
    else:
        raise FileNotFoundError('Unable to open file ' + filename)

def import_magics(filename):
    """Import a single .magics file.

    :param filename: Path to the file to import.
    :type filename: string

    :return: Tuple with imported parts.
    :rtype: (trimatic.Part)
    :raises: FileNotFoundError, RuntimeError
    :example:

    .. literalinclude:: example/file/import_magics.py
    """



    if os.path.isfile(filename):
        return pymatic.import_magics(filename)
    else:
        raise FileNotFoundError('Unable to open file ' + filename)

def import_mdck(filename):
    """Import a single MDCK file.

    :param filename: Path to the file to import.
    :type filename: string
    :return: Tuple with imported parts.
    :rtype: (trimatic.Part)
    :raises: FileNotFoundError, RuntimeError

    :example:

    .. literalinclude:: example/file/import_mdck.py
    """


    if os.path.isfile(filename):
        return pymatic.import_mdck(filename)
    else:
        raise FileNotFoundError('Unable to open file ' + filename)

def import_obj(filename, units = 1000):
    """Import a single obj file.

    :param filename: Path to the file to import.
    :type filename: string
    :param units: Units in which file was written. 1 for mm, 1000 for meters, etc.
    :type units: float, optional

    :return: Tuple with imported parts.
    :rtype: (trimatic.Part)
    :raises: FileNotFoundError, RuntimeError

    :example:

    .. literalinclude:: example/file/import_obj.py
    """


    trimatic.utils.check_resolution('units', units)

    if os.path.isfile(filename):
        return pymatic.import_obj(filename, units)
    else:
        raise FileNotFoundError('Unable to open file ' + filename)

def import_part_stl(filename, fix_normals=False):
    """Import a single STL file.

    :param filename: Path to the file to import.
    :type filename: string
    :param fix_normals: If True, triangles that are detected to have inverted normals are flipped.
    :type fix_normals: bool, optional
    :return: Imported part
    :rtype: trimatic.Part
    :raises: FileNotFoundError, RuntimeError

    :example:

    .. literalinclude:: example/file/import_part_stl.py
    """



    if os.path.isfile(filename):
        return pymatic.import_part_stl(filename, fix_normals)
    else:
        raise FileNotFoundError('Unable to open file ' + filename)


def import_part_stl_split_by_angle(filename, fix_normals=False, wireframe_angle=30):
    """Import a single STL file and automatically split the surfaces according to the specified wireframe angle.

    :param filename: Path to the file to import.
    :type filename: string
    :param fix_normals: If True, triangles that are detected to have inverted normals are flipped.
    :type fix_normals: bool, optional
    :param wireframe_angle: Minimum angle between adjacent triangles for a common edge to be treated as the
        wireframe for splitting.
    :type wireframe_angle: float, optional
    :return: Imported part
    :rtype: trimatic.Part
    :raises: FileNotFoundError, RuntimeError

    :example:

    .. literalinclude:: example/file/import_part_stl_split_by_angle.py
    """



    if os.path.isfile(filename):
        return pymatic.import_part_stl_split_by_angle(filename, fix_normals, wireframe_angle)
    else:
        raise FileNotFoundError('Unable to open file ' + filename)


def import_part_stl_split_by_color(filename, fix_normals=False, keep_surface_color=True):
    """Import a single STL file and automatically split the surfaces according to color.

    :param filename: Path to the file to import.
    :type filename: string
    :param fix_normals: If True, triangles that are detected to have inverted normals are flipped.
    :type fix_normals: bool, optional
    :param keep_surface_color: If True, the surface color of the STL will be preserved after import.
    :type keep_surface_color: bool, optional
    :return: Imported part
    :rtype: trimatic.Part
    :raises: FileNotFoundError, RuntimeError

    :example:

    .. literalinclude:: example/file/import_part_stl_split_by_color.py
    """



    if os.path.isfile(filename):
        return pymatic.import_part_stl_split_by_color(filename, fix_normals, keep_surface_color)
    else:
        raise FileNotFoundError('Unable to open file ' + filename)

def import_pro_engineer(filename, surface_accuracy = 0.01):
    """Import a single .prt or .asm file.

    :param filename: Path to the file to import.
    :type filename: string
    :param surface_accuracy: The maximum allowed distance deviation between the CAD file and the triangulation.
    :type surface_accuracy: float, optional

    :return: Tuple with imported parts.
    :rtype: (trimatic.Part)
    :raises: FileNotFoundError, RuntimeError

    :example:

    .. literalinclude:: example/file/import_pro_engineer.py
    """


    trimatic.utils.check_resolution('surface_accuracy', surface_accuracy)

    if os.path.isfile(filename):
        return pymatic.import_pro_engineer(filename, surface_accuracy)
    else:
        raise FileNotFoundError('Unable to open file ' + filename)

def import_solidworks(filename, surface_accuracy = 0.01):
    """Import a single .sldprt or .sldasm file.

    :param filename: Path to the file to import.
    :type filename: string
    :param surface_accuracy: The maximum allowed distance deviation between the CAD file and the triangulation.
    :type surface_accuracy: float, optional

    :return: Tuple with imported parts.
    :rtype: (trimatic.Part)
    :raises: FileNotFoundError, RuntimeError

    :example:

    .. literalinclude:: example/file/import_solidworks.py
    """


    trimatic.utils.check_resolution('surface_accuracy', surface_accuracy)

    if os.path.isfile(filename):
        return pymatic.import_solidworks(filename, surface_accuracy)
    else:
        raise FileNotFoundError('Unable to open file ' + filename)

def import_step(filename, surface_accuracy = 0.01):
    """Import a single .stp or .step file.

    :param filename: Path to the file to import.
    :type filename: string
    :param surface_accuracy: The maximum allowed distance deviation between the CAD file and the triangulation.
    :type surface_accuracy: float, optional

    :return: Tuple with imported parts.
    :rtype: (trimatic.Part)
    :raises: FileNotFoundError, RuntimeError

    :example:

    .. literalinclude:: example/file/import_step.py
    """


    trimatic.utils.check_resolution('surface_accuracy', surface_accuracy)

    if os.path.isfile(filename):
        return pymatic.import_step(filename, surface_accuracy)
    else:
        raise FileNotFoundError('Unable to open file ' + filename)

def import_unigraphics_parasolid(filename, surface_accuracy = 0.01, layer_to_part = True):
    """Import a single .prt or .x_t or .x_b file.

    :param filename: Path to the file to import.
    :type filename: string
    :param surface_accuracy: The maximum allowed distance deviation between the CAD file and the triangulation.
    :type surface_accuracy: float, optional
    :param layer_to_part: When True: all the entities which are grouped in one layer, will be grouped in one part.
    :type layer_to_part: bool, optional

    :return: Tuple with imported parts.
    :rtype: (trimatic.Part)
    :raises: FileNotFoundError, RuntimeError

    :example:

    .. literalinclude:: example/file/import_unigraphics_parasolid.py
    """


    trimatic.utils.check_resolution('surface_accuracy', surface_accuracy)

    if os.path.isfile(filename):
        return pymatic.import_unigraphics_parasolid(filename, surface_accuracy, layer_to_part)
    else:
        raise FileNotFoundError('Unable to open file ' + filename)

def import_vrml(filename, units = 1000):
    """Import a single .wrl file.

    :param filename: Path to the file to import.
    :type filename: string
    :param units: Units in which file was written. 1 for mm, 1000 for meters, etc.
    :type units: float, optional

    :return: Tuple with imported parts.
    :rtype: (trimatic.Part)
    :raises: FileNotFoundError, RuntimeError
    :example:

    .. literalinclude:: example/file/import_vrml.py
    """


    trimatic.utils.check_resolution('units', units)

    if os.path.isfile(filename):
        return pymatic.import_vrml(filename, units)
    else:
        raise FileNotFoundError('Unable to open file ' + filename)

def import_x3d(filename):
    """Import a single .x3d file.

    :param filename: Path to the file to import.
    :type filename: string
    :return: Tuple with imported parts.
    :rtype: (trimatic.Part)
    :raises: FileNotFoundError, RuntimeError
    :example:

    .. literalinclude:: example/file/import_x3d.py
    """



    if os.path.isfile(filename):
        return pymatic.import_x3d(filename)
    else:
        raise FileNotFoundError('Unable to open file ' + filename)

def import_xml(filename):
    """Import analytical primitives or polydata from an XML file. When importing polydata, curves will be created. A new part will be created to contain the curves.

    :param filename: Path to the file to import.
    :type filename: string
    :return: Imported entities
    :rtype: (trimatic.Part | trimatic.Line | trimatic.Point | trimatic.Plane | trimatic.Arc | trimatic.Cylinder | trimatic.Sphere)
    :raises: FileNotFoundError, RuntimeError

    :example:

    .. literalinclude:: example/file/import_xml.py
    """



    if os.path.isfile(filename):
        return pymatic.import_xml(filename)
    else:
        raise FileNotFoundError('Unable to open file ' + filename)

def new_project():
    """Starts a new project. 
    
    Be advised that the current project will be closed without saving.

    :return: True if a new project was successfully created.
    :rtype: bool
    :raises: RuntimeError

    :example:

    .. literalinclude:: example/file/new_project.py
    """



    return pymatic.new_project()


def open_project(filename):
    """Opens a 3-matic or Magics project file. 
    
    Be advised that the current project will be closed without saving.

    :param filename: Path of the mxp/magics file.
    :type filename: string
    :return: True if a new project was successfully created.
    :rtype: bool
    :raises: FileNotFoundError, RuntimeError, ValueError

    :example:

    .. literalinclude:: example/file/open_project.py
    """


    
    filename = os.path.abspath(filename)
    if not os.path.isfile(filename):
        raise FileNotFoundError('unable to open file ' + filename)
    trimatic.utils.check_file_type(filename, ('.mxp', '.magics'))
    return pymatic.open_project(filename)


def import_project(filename):
    """Imports a 3-matic or Mimics project file. 
    
    Entities from the imported file are merged into what is currently opened.

    :param filename: Path to mxp/mcs file.
    :type filename: string
    :return: Tuple of imported objects.
    :rtype: (trimatic.Object)
    :raises: FileNotFoundError, RuntimeError, ValueError

    :example:

    .. literalinclude:: example/file/import_project.py
    """

    if not os.path.isfile(filename):
        raise FileNotFoundError('unable to open file ' + filename)

    trimatic.utils.check_file_type(filename, ('.mxp', '.mcs'))

    return pymatic.import_project(filename)


def save_project(filename):
    """Saves current project. 
    
    If the file already exists, the file is overwritten.

    :param filename: Path to the file to write. When None is specified, the filename of the currently opened project is used.
    :type filename: string
    :return: Path of written filename.
    :rtype: string
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/file/save_project.py
    """



    if filename is None or trimatic.utils.check_file_saveable(filename):
        return pymatic.save_project(filename)
    else:
        raise ValueError('unable to save file ' + filename)

    
def clear():
    """Clears the object tree and the log window.

    :return: True when the clear operation was successful.
    :rtype: bool
    :raises: RuntimeError

    :example:

    .. literalinclude:: example/file/clear.py
    """
    return new_project()

def get_project_filename():   
    """Returns the full path of the currently opened project.

    :return: path + filename
    :rtype: string
    :raises: RuntimeError
    :example:

    .. literalinclude:: example/file/get_project_filename.py
    """
	
    return pymatic.get_project_filename()
