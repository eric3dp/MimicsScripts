import trimatic
from colors import colormap
selected = trimatic.get_selection()
for (
    x
) in (
    selected
):  # loop through the selection and set the color when the key string matches
    if isinstance(x, trimatic.Group):
        for y in x.items:
            for key, value in colormap.items():
                if y.name.lower().startswith(key.lower()):
                    y.color = value

    else:
        for key, value in colormap.items():
            if x.name.lower().startswith(key.lower()):
                x.color = value
