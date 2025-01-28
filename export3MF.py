
import trimatic
import os.path
import add_prefix
import exportPDF

fullname = trimatic.get_project_filename() # get full path and file name of project
modelfolder = fullname.rsplit("\\",2)[1] # split the string into two parts at the last \, basically path and filename, keep the folder name
modelfolder = modelfolder.rsplit(" ")[0] # get rid of the excess descriptor in the folder name
filepath = fullname.rsplit("\\",1)[0] + "\\"
newfile = ""
groupselection = []

selected = trimatic.get_selection() # gather up the currently selected parts & groups
selmsg = "Current selection:\n"
if len(selected)>0: # build a string of what is selected for the upcoming message box
    for x in selected:
        if isinstance(x,trimatic.Part): # check if it's a part
            selmsg = selmsg + "\n" + x.name
        elif isinstance(x, trimatic.Group): # else check if it's a group
            selmsg = selmsg + "\nGroup: " + x.name
            for y in x.items: # loop through the group and add part names under the Group heading
                selmsg = selmsg + "\n  - " + y.name
else:
    selmsg = ""
msg = trimatic.message_box("Select the objects to which you'd like to export. Selected parts will be exported individually. Selected groups will be exported as single files." + "\n\n" + selmsg,"Export to 3MF",with_cancel= True)
if msg is False:
    raise SystemExit(0)

selected = trimatic.get_selection() # get the selected parts into a tuple 
add_prefix.rename(selected)
basepath = ""
result = "Performed the following operations:\n"
exportPDF.exportPDF(selected)
for x in selected: # loop through the selection, check if the file exists, check if it's a group or multiple parts, then export them
    groupselection.clear()
    if isinstance(x, trimatic.Group):
        if "Base" in x.name:
            basepath = "C:\\Users\\bradened\\OneDrive - Arkansas Children's\\3D Files\AMU\Models\\ACH24-167 - Bases\\" + modelfolder + "_" + x.name + ".3mf"
        for y in x.items:
            groupselection.append(y)
    elif isinstance(x, trimatic.Part):
        groupselection.append(x)
    newfile = filepath + modelfolder + "_" + x.name + ".3mf"
    if os.path.isfile(newfile):
        msg = trimatic.message_box("Overwriting existing file:" + "\n" + newfile + "\nClick Cancel to skip this file", "Existing file")
        if msg is True:
            trimatic.export_3mf(groupselection, newfile)
            if len(basepath)>0:
                result = result + "\n- Exported " + basepath
                trimatic.export_3mf(groupselection, basepath)
            result = result + "\n- Replaced " + newfile
        if msg is False:
            result = result + "\n- Skipped " + newfile
    else:
        trimatic.export_3mf(groupselection, newfile)
        if len(basepath)>0:
            result = result + "\n- Exported " + basepath
            trimatic.export_3mf(groupselection, basepath)
        result = result + "\n- Exported " + newfile

trimatic.message_box(result, "Result", False)

