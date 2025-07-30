import trimatic
import os.path
import add_prefix
import exportPDF

# Get current project file path (empty string if unsaved)
fullname = trimatic.get_project_filename()

# If unsaved, prompt user to save before continuing
if not fullname:
    trimatic.message_box(
        "Please save your project before exporting.", "Save Required"
    )
    trimatic.save_project_as()
    fullname = trimatic.get_project_filename()
    if not fullname:
        trimatic.message_box("Export canceled.", "No File Saved")
        raise SystemExit(0)

# Extract folder name and base path
modelfolder = fullname.rsplit("\\", 2)[1].rsplit(" ")[0]
filepath = fullname.rsplit("\\", 1)[0] + "\\"
newfile = ""
groupselection = []

# Get current selection
selected = trimatic.get_selection()
selmsg = "Current selection:\n"

# Build display string for selection summary
if len(selected) > 0:
    for x in selected:
        if isinstance(x, trimatic.Part):
            selmsg += "\n" + x.name
        elif isinstance(x, trimatic.Group):
            selmsg += "\nGroup: " + x.name
            for y in x.items:
                selmsg += "\n  - " + y.name
else:
    selmsg = ""

# Confirm with user
msg = trimatic.message_box(
    "Select the objects to which you'd like to export. Selected parts will be "
    "exported individually. Selected groups will be exported as single files."
    + "\n\n"
    + selmsg,
    "Export to 3MF",
    with_cancel=True,
)
if msg is False:
    raise SystemExit(0)

# Get updated selection
selected = trimatic.get_selection()
# Rename parts
add_prefix.rename(selected)

basepath = ""
result = "Performed the following operations:\n"

# Export PDF to both locations
exportPDF.exportPDF(selected)

# Export selected parts/groups
for x in selected:
    groupselection.clear()

    if isinstance(x, trimatic.Group):
        # if "Base" in x.name: basepath = ("C:\\Users\\bradened\\OneDrive - Arkansas Children's\\3D Files\\AMU\\Models\\ACH24-167 - Bases\\" + modelfolder + "_" + x.name + ".3mf")

        for y in x.items:
            groupselection.append(y)

    elif isinstance(x, trimatic.Part):
        groupselection.append(x)

    newfile = filepath + modelfolder + "_" + x.name + ".3mf"

    if os.path.isfile(newfile):
        msg = trimatic.message_box(
            "Overwriting existing file:\n"
            + newfile
            + "\nClick Cancel to skip this file",
            "Existing file",
        )
        if msg is True:
            trimatic.export_3mf(groupselection, newfile)
            if basepath:
                trimatic.export_3mf(groupselection, basepath)
                result += "\n- Exported " + basepath
            result += "\n- Replaced " + newfile
        elif msg is False:
            result += "\n- Skipped " + newfile
    else:
        trimatic.export_3mf(groupselection, newfile)
        if basepath:
            trimatic.export_3mf(groupselection, basepath)
            result += "\n- Exported " + basepath
        result += "\n- Exported " + newfile

# Show result summary
trimatic.message_box(result, "Result", False)
