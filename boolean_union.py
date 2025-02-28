import trimatic
import move_to_trash

selected = trimatic.get_selection()

duplicates = trimatic.duplicate(selected)
move_to_trash.move_to_trash(duplicates)

selected = trimatic.boolean_union(selected)