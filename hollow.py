import trimatic
import tkinter as tk
from tkinter import messagebox

# parameters
hollow_distance = 2  # in mm
hollow_smallest_detail = 0.3
hollow_smooth_factor = 0.5


def validate_input():
    global hollow_distance
    try:
        value = float(entry.get())
        if value < 1.00:
            if not messagebox.askyesno(
                "Warning", "Thin walls may cause issues in printing. Continue?"
            ):
                return
        elif value > 5.00:
            if not messagebox.askyesno("!!!", "That's very thick. You sure?"):
                return
        input_box.destroy()
        hollow_distance = value
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")


def on_window_open():
    """
    Ensures the input field gains focus and
    highlights text after the window is shown.
    """
    entry.focus()
    entry.icursor(tk.END)  # Move cursor to the end
    entry.selection_range(0, tk.END)  # Highlight all text


# input box to get hollow thickness
input_box = tk.Tk()
input_box.title("Enter Thickness")

tk.Label(input_box, text="Enter thickness (mm):").pack(pady=5)

entry = tk.Spinbox(
    input_box,
    from_=0.1,
    to=10,
    increment=0.25,
    format="%.2f",
    width=10
    )
entry.pack(
    pady=10,
    padx=5
    )
entry.delete(
    0,
    tk.END
    )
entry.insert(
    0,
    "2.00"
    )

input_box.after(100, on_window_open)

submit_button = tk.Button(
    input_box,
    text="Submit",
    command=validate_input
    )
submit_button.pack(
    pady=10
    )

input_box.mainloop()

selected = trimatic.get_selection()

parts_to_solids_folder = trimatic.duplicate(selected)
solid_to_merge_back_into_hollow = trimatic.invert_normal(
    trimatic.duplicate(selected)
    )

hollow_part = trimatic.hollow(
    entities=selected,
    hollow_type=trimatic.HollowType.Outside,
    distance=hollow_distance,
    smallest_detail=hollow_smallest_detail,
    smooth_factor=hollow_smooth_factor,
)
if isinstance(solid_to_merge_back_into_hollow, trimatic.Part):
    final_part = trimatic.merge([hollow_part, solid_to_merge_back_into_hollow])
    final_part.name = final_part.name[:-1] + "_hollow"
else:
    for x, merge_list in zip(selected, solid_to_merge_back_into_hollow):
        final_part = trimatic.merge([x, merge_list])
        final_part.name = final_part.name[:-1] + "_hollow"

solids = trimatic.find_group("Solids")
if not solids:
    solids_group = trimatic.create_group("Solids", parts_to_solids_folder)
    solids_group.visible = False

else:
    solids.add_items(parts_to_solids_folder)
