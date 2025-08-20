import mimics

darkblue = (0, 0.501960784, 1)
lightblue = (0.501960784, 1, 1)
red = (1, 0, 0)
lilac = (0.8235294117647059, 0.8235294117647059, 1)
orange = (1, 0.501960784, 0)
yellow = (1, 1, 0)
green = (0, 1, 0)
white = (1, 1, 1)
colormap = {  # list of common parts and their associated colors
    "PA": darkblue,
    "AO": red,
    "Ao": red,
    "Aorta": red,
    "RA": lightblue,
    "LA": orange,
    "LV": yellow,
    "RV": lilac,
    "PDA": white,
    "Airway": green,
    "Left Ventricle": yellow,
    "Right Ventricle": lilac,
    "Coronar": red,
    "Label": white,
    "Left Atrium": orange,
    "Right Atrium": lightblue,
    "Pulmonary": darkblue,
}
selected = mimics.data.masks
for (
    x
) in (
    selected
):  # loop through the selection and set the color when the key string matches
    for key, value in colormap.items():
        if type(x) is tuple:
            for y in x:
                if y.name.startswith(key):
                    y.color = value
        else:
            if x.name.startswith(key):
                x.color = value

#     if isinstance(x, trimatic.Group):
#         for y in x.items:
#             for key,value in colormap.items():
#                 if y.name.startswith(key):
#                     y.color = value
#     else:
#         for key,value in colormap.items():
#             if x.name.startswith(key):
#                 x.color = value
