# colors.py

darkblue = (0, 0.501960784, 1)
lightblue = (0.501960784, 1, 1)
red = (1, 0, 0)
lilac = (0.8235294117647059, 0.8235294117647059, 1)
orange = (1, 0.501960784, 0)
yellow = (1, 1, 0)
green = (0, 1, 0)
white = (1, 1, 1)

# canonical mapping: one entry per structure
base_colormap = {
    "Pulmonary Artery": darkblue,
    "Aorta": red,
    "Right Atrium": lightblue,
    "Left Atrium": orange,
    "Left Ventricle": yellow,
    "Right Ventricle": lilac,
    "PDA": white,
    "Airway": green,
    "Coronary": red,
    "Label": white,
}

# alias groups point to the canonical key
aliases = {
    "Pulmonary Artery": ["PA", "Pulmonary-A", "Pulmonary A"],
    "Aorta": ["AO", "Ao"],
    "Right Atrium": ["RA", "Right_Atrium"],
    "Left Atrium": ["LA", "Left_Atrium"],
    "Left Ventricle": ["LV", "Left_Ventricle"],
    "Right Ventricle": ["RV", "Right_Ventricle"],
    "Coronary": ["Coronar"],
}

# build the full colormap dynamically
colormap = {}
for canonical, color in base_colormap.items():
    colormap[canonical] = color
    for alias in aliases.get(canonical, []):
        colormap[alias] = color
