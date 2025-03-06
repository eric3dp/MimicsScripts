import trimatic
import move_to_trash

final_name = ""
selected = trimatic.get_selection()

for x in selected:
    if isinstance(x, trimatic.Group):
        for y in x.items:
            final_name = final_name + "," + y.name
    else:
        final_name = final_name + "," + x.name

duplicates = trimatic.duplicate(selected)
move_to_trash.move_to_trash(duplicates)

selected = trimatic.boolean_union(selected)
names = final_name.split(",")
final_name = "-".join(names) + "_union"
selected.name = final_name
