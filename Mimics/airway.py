import mimics

airway_mask = mimics.segment.create_mask()
airway_mask.name = "Airway"
# airway_mask.color = [0,1,0] - having this line this frequently crashes Mimics or times out

desired_max_threshold = -575
converted_max_threshold = desired_max_threshold + 1024

mimics.segment.threshold(
    mask=airway_mask,
    threshold_min=1,
    threshold_max=converted_max_threshold)

bounding_masks = [
    mimics.data.masks.find("(?i)^AO.*",regex = True),
    mimics.data.masks.find("(?i)^LV.*",regex = True),
    mimics.data.masks.find("(?i)^LA.*",regex = True),
    ]
crop_box = mimics.measure.get_bounding_box(bounding_masks)

mimics.segment.crop_mask(
    mask=airway_mask,
    bounding_box=crop_box)

# region_mark = mimics.analyze.indicate_point("Please click on the airway.")

# mimics.segment.region_grow(
#     input_mask = airway_mask,
#     point = region_mark,
#     slice_type = "Axial",
#     target_mask = airway_mask
#     )