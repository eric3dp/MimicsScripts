import mimics

# constants
THRESHOLD_MIN = mimics.segment.HU2GV(-1023)
THRESHOLD_MAX = mimics.segment.HU2GV(-238)

airway_mask = mimics.segment.create_mask()
airway_mask.name = "Airway"
# airway_mask.color = [0,1,0] - frequently crashes or times out

mimics.segment.threshold(
    mask=airway_mask, threshold_min=THRESHOLD_MIN, threshold_max=THRESHOLD_MAX
)

bounding_masks = [
    mimics.data.masks.find("(?i)^(AO|Aorta).*", regex=True),
    mimics.data.masks.find("(?i)^(LV|Left[- ]?Ventricle).*", regex=True),
    mimics.data.masks.find("(?i)^(LA|Left[- ]?Atrium).*", regex=True),
]
crop_box = mimics.measure.get_bounding_box(bounding_masks)

mimics.segment.crop_mask(mask=airway_mask, bounding_box=crop_box)
