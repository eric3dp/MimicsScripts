
import trimatic

selected = trimatic.get_selection()
for x in selected:
    for y in x.items:
        print (y.name)