import trimatic
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
cut_parts = trimatic.cut(earmold, plane)
trimatic.delete(plane)
earmold2 = earmold
msg = trimatic.message_box("Please select the part to keep", "Keep")
earmold = trimatic.duplicate(trimatic.get_selection())
for item in cut_parts:
    if item != earmold:
        trimatic.delete(item)
