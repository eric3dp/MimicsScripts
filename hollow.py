import trimatic

# parameters
hollow_distance = 2 # in mm
hollow_smallest_detail = 0.3
hollow_smooth_factor = 0.5

selected = trimatic.get_selection()

parts_to_solids_folder = trimatic.duplicate(selected)
solid_to_merge_back_into_hollow = trimatic.invert_normal(trimatic.duplicate(selected))

hollow_part = trimatic.hollow(
                entities = selected, 
                hollow_type = trimatic.HollowType.Outside, 
                distance= hollow_distance,
                smallest_detail=hollow_smallest_detail,
                smooth_factor = hollow_smooth_factor
                )
if isinstance(solid_to_merge_back_into_hollow, trimatic.Part):
    final_part = trimatic.merge([hollow_part, solid_to_merge_back_into_hollow])
    final_part.name = final_part.name[:-1] + "_hollow"
else:
    for x, merge_list in zip(selected, solid_to_merge_back_into_hollow):
        final_part = trimatic.merge([x, merge_list])
        final_part.name = final_part.name[:-1] + "_hollow"

solids = trimatic.find_group("Solids")
if not solids:
    solids_group = trimatic.create_group("Solids", parts_to_solids_folder)
    solids_group.visible = False

else:
    solids.add_items(parts_to_solids_folder)

