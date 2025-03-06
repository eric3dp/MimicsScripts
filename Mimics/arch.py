import mimics

THRESHOLD_MIN = mimics.segment.HU2GV(400)
THRESHOLD_MAX = mimics.segment.HU2GV(8645)


def create_mask(name):
    mask = mimics.segment.create_mask()
    mask.name = name
    if name != "Blood":
        print(f"Mark the {name}")
        mimics.segment.activate_edit_mask(mask, "Draw", "Ellipse")
    return mask


blood = create_mask("Blood")
mimics.segment.threshold(
    mask=blood, threshold_min=THRESHOLD_MIN, threshold_max=THRESHOLD_MAX
)

part_names = ["Aorta", "PA", "PDA", "Other"]
part_list = [create_mask(name) for name in part_names]

mimics.segment.split_mask(blood, part_list)
