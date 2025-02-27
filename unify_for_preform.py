import trimatic

groupselection=[]
fullname = trimatic.get_project_filename() # get full path and file name of project
modelfolder = fullname.rsplit("\\",2)[1] # split the string into two parts at the last \, basically path and filename
modelfolder = modelfolder.rsplit(" ")[0] # get rid of the excess descriptor in the folder name
filepath = fullname.rsplit("\\",1)[0] + "\\"

msg = trimatic.message_box("Select which parts you'd like to unify", "Unify")
selected = trimatic.get_selection()
duplicated = trimatic.duplicate(selected)
for x in duplicated:
  groupselection.clear()
  if isinstance(x, trimatic.Group):
    if "Base" in x.name:
      pass
    else:
      for y in x.items:
        groupselection.append(y)
  union = trimatic.boolean_union(groupselection)
  union.name = modelfolder + "_Gift"
  newfile = filepath + modelfolder + "_" + x.name + ".stl"
  trimatic.exportSTL(union, newfile)




