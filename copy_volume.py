import trimatic
import pyperclip
selected = trimatic.get_selection()
i = 0
for x in selected:
    if isinstance(x, trimatic.Group):
        for y in x.items:
            i = y.volume + i
    else:
        i = x.volume + i

pyperclip.copy(int(i))