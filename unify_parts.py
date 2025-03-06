import trimatic

fullname = trimatic.get_project_filename()  # get full path and file name
modelfolder = fullname.rsplit("\\", 2)[
    1
]  # split the string into two parts at the last \, basically path and filename
modelfolder = modelfolder.rsplit(" ")[
    0
]  # get rid of the excess descriptor in the folder name

msg = trimatic.message_box("Select which parts you'd like to unify", "Unify")
selected = trimatic.get_selection()
duplicated = trimatic.duplicate(selected)
union = trimatic.boolean_union(duplicated)
union.name = modelfolder + "_Unified"
