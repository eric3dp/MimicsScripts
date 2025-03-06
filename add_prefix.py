import trimatic


def rename(selected):
    existing = []
    fullname = trimatic.get_project_filename()  # get full path and file name
    modelfolder = fullname.rsplit("\\", 2)[
        1
    ]  # split the string into two parts at the last \,keep folder
    modelfolder = modelfolder.rsplit(" ")[
        0
    ]  # get rid of the excess descriptor in the folder name

    if len(selected) == 0:  # if nothing is selected, exit the script
        trimatic.message_box(
            "Nothing selected, script aborted",
            "Nothing selected",
            with_cancel=False
        )
        raise SystemExit(0)

    for x in selected:
        if isinstance(x, trimatic.Part):  # check if it's a part
            if (
                modelfolder
            ) not in x.name:  # check to see if it's already named correctly
                x.name = x.name.split(" ")[0]  # keep anything after a space
                x.name = modelfolder + "_" + x.name  # rename the part
            else:
                existing.append(
                    x.name
                )  # if it's already named correctly, add it to a list
        elif isinstance(x, trimatic.Group):  # check if it's a group
            for y in x.items:
                if (modelfolder + "_" + x.name) not in y.name:
                    y.name = y.name.split(" ")[0]
                    y.name = (
                        modelfolder + "_" + x.name + "_" + y.name
                    )  # rename the part with the group name as well
                else:
                    existing.append(y.name)
