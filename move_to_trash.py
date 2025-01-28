# move to trash
import trimatic

selected = []
selected = trimatic.get_selection()
trash = []
trash = trimatic.find_group("trash")
if trash:
    trash.name = "Trash"
else:   
    trash = trimatic.find_group("Trash")
if not trash:
    trash = trimatic.create_group("Trash",selected)
    trash.visible = False
else:
    trash.add_items(selected)