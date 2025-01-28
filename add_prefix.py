import trimatic

def rename(selected):
    existing = []
    unchanged = ""
    fullname = trimatic.get_project_filename() # get full path and file name of project
    modelfolder = fullname.rsplit("\\",2)[1] # split the string into two parts at the last \, basically path and filename
    modelfolder = modelfolder.rsplit(" ")[0] # get rid of the excess descriptor in the folder name

    if len(selected) == 0: # if nothing is selected, exit the script with a message
        trimatic.message_box("Nothing selected, script aborted", "nothing selected", with_cancel=False)
        raise SystemExit(0)

    for x in selected: 
        if isinstance(x,trimatic.Part): # check if it's a part
            if (modelfolder) not in x.name:  # check to see if it's already named correctly
                x.name = x.name.split(" ")[0] # split out anything after a space (like "Aorta 1" from Mimics), only keeping the part before the space
                x.name = modelfolder + "_" + x.name # rename the part
            else:
                existing.append(x.name) # if it's already named correctly, add it to a list to report when done
        elif isinstance(x, trimatic.Group): # check if it's a group
            for y in x.items: 
                if (modelfolder + "_" + x.name) not in y.name:
                    y.name = y.name.split(" ")[0] 
                    y.name = modelfolder + "_" + x.name + "_"+ y.name # rename the part with the group name as well
                else:
                    existing.append(y.name)

    # make a message box asking for a selection. If "cancel" the script stops
#    selected = trimatic.get_selection()
#    selmsg = "Current selection:"
#    if len(selmsg)>0:
#        for x in selected:
#            selmsg = selmsg + "\n" + x.name
#    else:
#        selmsg = ""
#    msg = trimatic.message_box("Select the objects to which you'd like to prepend '" + modelfolder + "'\n\n" + selmsg,"Rename",with_cancel= True)
#    if msg is False:
#        raise SystemExit(0)

    # the selected objects go into the 'selected" tuple
#    selected = trimatic.get_selection()

    # if len(selected) == 0: # if nothing is selected, exit the script with a message
    #     trimatic.message_box("Nothing selected, script aborted", "nothing selected", with_cancel=False)
    #     raise SystemExit(0)

    # for x in selected: 
    #     if isinstance(x,trimatic.Part): # check if it's a part
    #         if (modelfolder) not in x.name:  # check to see if it's already named correctly
    #             x.name = x.name.split(" ")[0] # split out anything after a space (like "Aorta 1" from Mimics), only keeping the part before the space
    #             x.name = modelfolder + "_" + x.name # rename the part
    #         else:
    #             existing.append(x.name) # if it's already named correctly, add it to a list to report when done
    #     elif isinstance(x, trimatic.Group): # check if it's a group
    #         for y in x.items: 
    #             if (modelfolder + "_" + x.name) not in y.name:
    #                 y.name = y.name.split(" ")[0] 
    #                 y.name = modelfolder + "_" + x.name + "_"+ y.name # rename the part with the group name as well
    #             else:
    #                 existing.append(y.name)

    # let user know which items (if any) didn't get renamed
#    if len(existing)>0:
#        for x in existing:
#            unchanged = unchanged + "\n" + x
#        trimatic.message_box("The following items were not changed:" + "\n" + unchanged, str(len(existing)) + " unchanged items")
