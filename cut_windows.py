import trimatic


up = 100
down = 100

""" msg = trimatic.message_box ("Select sketch", "Sketch")
if msg is False:
    raise SystemExit(0) """
#selected_sketch = trimatic.get_selection()
selected_sketch = trimatic.find_sketch("Sketch-001_duplicate")
extrude_direction = selected_sketch.object_coordinate_system.z_axis
cut_planes = trimatic.extrude(entities=selected_sketch,direction=extrude_direction, depth1=up, depth2=down)

""" msg = trimatic.message_box("Cut which parts?","Cut parts")
if msg is False:
    raise SystemExit(0) """
cut_parts = trimatic.find_part("Box-001")
#cut_parts = trimatic.get_selection()
cut_parts = trimatic.cut(cut_parts, cut_planes)
trimatic.hollow(entities=cut_planes, hollow_type=trimatic.HollowType.Both, distance=1, reduce=False, smooth_factor=0)

# doesn't work - makes a zero triangle part
new_list = []

new_list.append(cut_parts[0])

new_list.append(cut_planes)
trimatic.boolean_intersection(new_list)
# trimatic.boolean_intersection([dup_planes,cut_parts])
