# move to trash
import trimatic

trash = []


def move_to_trash(input):
    trash = trimatic.find_group("trash")
    if trash:
        trash.name = "Trash"
    else:
        trash = trimatic.find_group("Trash")
    if not trash:
        trash = trimatic.create_group("Trash", input)
        trash.visible = False
    else:
        trash.add_items(input)


if __name__ == "__main__":
    input = trimatic.get_selection()
    move_to_trash(input)
