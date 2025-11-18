import mimics

# import numpy as np

aorta = mimics.data.masks.find("AO")
box_aorta = mimics.measure.get_bounding_box(aorta)
box_crop = box_aorta

v0 = box_aorta.origin
v1 = box_aorta.first_vector
v2 = box_aorta.second_vector
v3 = box_aorta.third_vector
# v3 = tuple(np.array(box_aorta.third_vector) * 0.73)

coord = mimics.indicate_coordinate()
v4 = [v3[0], v3[1], coord[2] - v0[2]]

box_crop = mimics.BoundingBox3d(
    origin=v0, first_vector=v1, second_vector=v2, third_vector=v4
)

print(box_aorta)
print(v0)
print(v3)
print(v4)
print(coord)
print(box_crop)

aorta = mimics.segment.crop_mask(aorta, box_crop)
aorta = mimics.segment.filter_mask(aorta, 1)
aorta.name = "Aorta"
