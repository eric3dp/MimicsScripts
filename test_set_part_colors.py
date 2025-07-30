import types

# Mock trimatic module
class MockItem:
    def __init__(self, name):
        self.name = name
        self.color = None

class MockGroup:
    def __init__(self, items):
        self.items = items

# The function extracted from your script logic
def set_colors(selected):
    darkblue = (0, 0.501960784, 1)
    lightblue = (0.501960784, 1, 1)
    red = (1, 0, 0)
    lilac = (0.8235294117647059, 0.8235294117647059, 1)
    orange = (1, 0.501960784, 0)
    yellow = (1, 1, 0)
    green = (0, 1, 0)
    white = (1, 1, 1)

    colormap = {
        "PA": darkblue,
        "AO": red,
        "Ao": red,
        "Aorta": red,
        "RA": lightblue,
        "LA": orange,
        "LV": yellow,
        "RV": lilac,
        "PDA": white,
    }

    for x in selected:
        if isinstance(x, MockGroup):
            for y in x.items:
                for key, value in colormap.items():
                    if y.name.startswith(key):
                        y.color = value
        else:
            for key, value in colormap.items():
                if x.name.startswith(key):
                    x.color = value

def test_color_assignment():
    pa = MockItem("PA_main")
    lv = MockItem("LV_wall")
    unknown = MockItem("ABC")

    group = MockGroup([lv])
    selection = [pa, group, unknown]

    set_colors(selection)

    assert pa.color == (0, 0.501960784, 1)
    assert lv.color == (1, 1, 0)
    assert unknown.color is None
