import trimatic
import os.path

PDF_FOLDER = "I:\\PDFs\\"


# definition to be called from the export3MF.py script
def exportPDF(selected):
    fullname = trimatic.get_project_filename()  # get full path and file name
    modelfolder = fullname.rsplit("\\", 2)[
        1
    ]  # split the string into two parts at the last \, keep the folder name
    modelfolder = modelfolder.rsplit(" ")[
        0
    ]  # get rid of the excess descriptor in the folder name
    filepath = fullname.rsplit("\\", 1)[0] + "\\"
    newfile = ""
    pdfpath = PDF_FOLDER + modelfolder + ".pdf"
    pdfgroup = []

    selected = (
        trimatic.get_selection()
    )  # gather up the currently selected parts & groups
    for x in selected:  # loop through the selection and make a tuple of parts
        if isinstance(x, trimatic.Group):  # check if this item is a Group
            for y in x.items:  # loop through the items in the group
                pdfgroup.append(trimatic.duplicate(y))
                # pdfgroup.append(y) # add items in the group to the tuple
        elif isinstance(x, trimatic.Part):  # check if it's a part
            pdfgroup.append(trimatic.duplicate(x))  # add the part to the tuple
    newfile = filepath + modelfolder + ".pdf"
    trimatic.reduce(pdfgroup)
    if os.path.isfile(newfile):
        msg = trimatic.message_box(
            "Overwriting existing file:"
            + "\n"
            + newfile
            + "\nClick Cancel to skip this file",
            "Existing file",
        )
        if msg is True:
            trimatic.export_pdf(pdfgroup, newfile)
            trimatic.export_pdf(pdfgroup, pdfpath)
        # result = result + "\n- Replaced " + newfile
        # if msg is False:
        #     #result = result + "\n- Skipped " + newfile
    else:
        trimatic.export_pdf(pdfgroup, newfile)
        trimatic.export_pdf(pdfgroup, pdfpath)
    trimatic.delete(pdfgroup)
