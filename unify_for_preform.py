import trimatic  # trimatic is the API for Materialise 3-Matic

fullname = trimatic.get_project_filename()  # get full path and file name
modelfolder = fullname.rsplit("\\", 2)[
    1
]  # Grab the folder name from the full path by splitting at the last \
modelfolder = modelfolder.rsplit(" ")[
    0
]  # get rid of descriptor in the folder name after space
filepath = (
    fullname.rsplit("\\", 1)[0] + "\\"
)  # The full path to the folder where the stl will be saved
MAX_POLYCOUNT = 100000  # maximum polycount for the model

msg = trimatic.message_box("Select which parts you'd like to unify", "Unify")
if not msg:
    print("User cancelled the operation")
    raise SystemExit

# Loop through selection and add a duplicate of each item to a list
selected = trimatic.get_selection()
groupselection = []
for x in selected:
    if isinstance(  # iterate through the items in the group
        x, trimatic.Group
    ):
        if "Base" in x.name:  # skip the base
            pass
        else:
            for y in x.items:
                groupselection.append(
                    trimatic.duplicate(y)
                )  # add a duplicate of each item in the group to the list
    else:
        groupselection.append(
            trimatic.duplicate(x)
        )  # add a duplicate of each ungrouped item to the list
union = trimatic.boolean_union(groupselection)  # put them all together

# Check the polycount and reduce if over max
polycount = union.number_of_triangles
if polycount > MAX_POLYCOUNT:
    union = trimatic.reduce(union)

union.name = modelfolder + "_Gift"  # ACHYY-XXX_Gift
trimatic.export_stl_binary(union, filepath)  # export the model
