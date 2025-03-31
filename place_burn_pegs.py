import trimatic
import point_on_triangle as pot

PARTS_DIR = (
    "C:\\Users\\bradened\\OneDrive - Arkansas Children's\\"
    "3D Files\\Parts\\Burn\\"
)
ORIGIN = (0, 0, 0)

# SELECT PART TO PUT KNOB ON#
msg = trimatic.message_box(
    "Select the part to place the knob on.",
    "Knob Placement",
)
if msg is False:
    raise SystemExit(0)
selected = trimatic.get_selection()

# KNOB PLACEMENT #
print("Select a point to place securement knob.")
knob_point = trimatic.indicate_coordinate()  # pick a point in the scene
knob = trimatic.import_part_stl(PARTS_DIR + "knob.stl")

knob_move = tuple(k - o for k, o in zip(knob_point, ORIGIN))
trimatic.translate(knob, knob_move)  # move the knob to the point

part_triangles = selected[0].get_triangles()
mesh = pot.to_mesh(part_triangles)
triangle = pot.find_triangle(mesh, knob_point)
# normal = pot.find_normal(triangle)
angle, axis, normal_finish = pot.find_rotation(triangle, knob_point)

# ROTATE KNOB #
knob = trimatic.rotate(
    knob,
    angle_deg=angle,
    axis_origin=knob_point,
    axis_direction=axis
)
