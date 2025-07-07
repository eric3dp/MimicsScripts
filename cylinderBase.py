import trimatic
import trimatic.data

fullname = trimatic.get_project_filename()  # get full path and file name of
modelfolder = fullname.rsplit("\\", 2)[
    1
]  # split the string into two parts at the last \, keep folder
newfile = (
    fullname.rsplit("\\", 1)[0] + "\\" + modelfolder + "_Base.3mf"
)  # make the file name for the export the same as the folder

wall_thickness = 3
bottom_cut = wall_thickness + 1
base_label_height = 8
base_min_height = 10 + wall_thickness
base_diameter = 0.6
modelparts = []

# get selected parts
selection = trimatic.get_selection()
# prompt if parts not selected
if len(selection) < 1:
    trimatic.message_box(
        "Select the parts you'd like to make a base for, then click OK",
        "Cylindrical Base Script",
    )
    selection = trimatic.get_selection()
# exit if still nothing selected
if len(selection) < 1:
    trimatic.message_box("Nothing selected. Quitting.", "Nothing selected")
    raise SystemExit(0)

for x in selection:
    if isinstance(x, trimatic.Group):
        for y in x.items:
            modelparts.append(y)
    else:
        modelparts.append(x)

modelparts = trimatic.duplicate(modelparts)
newpart1 = trimatic.merge(modelparts)
newpart2 = trimatic.wrap(
    entities=newpart1, gap_closing_distance=1, smallest_detail=1,
    resulting_offset=0.5
)
trimatic.delete(newpart1)

# find the bottom center of the part
dim_max = newpart2.dimension_max
dim_min = newpart2.dimension_min
dim_delta = newpart2.dimension_delta
cyl_x = dim_min[0] + dim_delta[0] / 2
cyl_y = dim_min[1] + dim_delta[1] / 2
cyl_z = dim_min[2] - base_min_height
cyl_origin = [cyl_x, cyl_y, cyl_z]
cyl_radius = dim_delta[0] * base_diameter / 2
base_cyl_ana = trimatic.create_cylinder_axis(
    origin_point=cyl_origin, direction=[0, 0, 1], radius=cyl_radius,
    height=dim_delta[2]
)
base_cyl = trimatic.convert_analytical_to_mesh(base_cyl_ana)
trimatic.delete(base_cyl_ana)
f1 = base_cyl.find_surface("Top").get_border().get_contours()[0]
trimatic.fillet(entities=(f1), radius=cyl_radius - 0.5, tolerance=0.1)
base_cyl = trimatic.remove_undercut(
    undercut_entity=base_cyl, fitting_entity=newpart2, direction=[0, 0, -1]
)
cut_point = trimatic.compute_center_of_gravity(newpart2)
cut_plane = trimatic.create_plane_normal_origin([0, 0, -1], cut_point)
cut_bases = trimatic.cut(entities=base_cyl, cutting_entity=cut_plane)
if type(cut_bases) is tuple:
    trimatic.delete(cut_bases[0])
    base_cyl = cut_bases[1]
else:
    base_cyl = cut_bases
trimatic.delete(cut_plane)
trimatic.delete(newpart2)

box = trimatic.create_box_part(
    [cyl_x - cyl_radius, cyl_y - cyl_radius, cyl_z],
    cyl_radius * 2,
    cyl_radius,
    base_min_height,
)
base_cyl = trimatic.boolean_union([box, base_cyl])

base_cyl_hollow = trimatic.duplicate(base_cyl)
base_cyl_hollow = trimatic.hollow(
    entities=base_cyl_hollow,
    hollow_type=trimatic.HollowType.Inside,
    distance=wall_thickness,
    reduce=False,
).get_parent()

cut_plane = trimatic.create_plane_normal_origin(
    [0, 0, 1], [cyl_x - cyl_radius, cyl_y - cyl_radius, cyl_z]
)
trimatic.translate(cut_plane, [0, 0, bottom_cut])

base_cyl = trimatic.cut(base_cyl, cut_plane)
trimatic.delete(base_cyl[0])
trimatic.delete(cut_plane)
base_cyl = base_cyl[1]
base_cyl = trimatic.boolean_subtraction(base_cyl, base_cyl_hollow)
base_cyl.name = "Base"

# Everything below this point is garbage currently
# testing labeling - this works but isn't sized or centered.
# Also does it with surfaces, not a different object.

label_text = modelfolder.rsplit(" ", 2)[0]
text_length = 21
text_origin = [
    cyl_x - text_length,
    cyl_y - cyl_radius,
    base_cyl.dimension_min[2] + 1,
]
text_direction = [1, 0, 0]

text_surface = trimatic.quick_label(
    entity=base_cyl,
    text=label_text,
    point=text_origin,
    direction=text_direction,
    alignment=trimatic.TextAlignment.Center,
    font="Arial",
    bold=True,
    font_height=base_label_height,
    label_height=-1,
)
text_set = base_cyl.find_surface("Top surfaces")
text_set = trimatic.uniform_offset(text_set, 1, solid=True)
text_set.color = (0, 0, 1)
