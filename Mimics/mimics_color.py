import mimics
from colors import colormap

selected = mimics.data.masks
for (
    x
) in (
    selected
):  # loop through the selection and set
    # the color when the key string matches
    for key, value in colormap.items():
        if type(x) is tuple:
            for y in x:
                if y.name.startswith(key):
                    y.color = value
        else:
            if x.name.startswith(key):
                x.color = value
