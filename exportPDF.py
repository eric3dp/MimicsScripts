import trimatic
import os.path
import logging

# Path to shared PDF folder; may not always be available
PDF_FOLDER = "I:\\PDFs\\"


def exportPDF(selected):
    # Get full project file path (e.g., "C:\Projects\Model X\ModelX.mxp")
    fullname = trimatic.get_project_filename()

    # Extract folder name from path, stripping extra descriptors
    modelfolder = fullname.rsplit("\\", 2)[1].rsplit(" ")[0]

    # Folder path of the project (excluding the file name)
    filepath = fullname.rsplit("\\", 1)[0] + "\\"

    # Local PDF output path (same folder as project)
    newfile = filepath + modelfolder + ".pdf"

    # Shared PDF path (in PDF_FOLDER, named after the model folder)
    pdfpath = os.path.join(PDF_FOLDER, modelfolder + ".pdf")

    pdfgroup = []

    # Overwrite `selected` with currently selected parts/groups
    selected = trimatic.get_selection()

    # Duplicate all selected parts/groups into `pdfgroup`
    for x in selected:
        if isinstance(x, trimatic.Group):
            for y in x.items:
                pdfgroup.append(trimatic.duplicate(y))
        elif isinstance(x, trimatic.Part):
            pdfgroup.append(trimatic.duplicate(x))

    # Reduce group geometry (likely simplifies for export)
    trimatic.reduce(pdfgroup)

    try:
        # If a file already exists at newfile, ask before overwriting
        if os.path.isfile(newfile):
            msg = trimatic.message_box(
                "Overwriting existing file:\n"
                + newfile
                + "\nClick Cancel to skip this file",
                "Existing file",
            )
            if msg:
                trimatic.export_pdf(pdfgroup, newfile)
                # Only try shared export if folder is available
                if os.path.isdir(PDF_FOLDER):
                    trimatic.export_pdf(pdfgroup, pdfpath)
                else:
                    logging.warninga(
                        f"PDF folder '{PDF_FOLDER}' not found. "
                        "Skipping copy to shared location."
                    )
        else:
            # No existing file — export directly
            trimatic.export_pdf(pdfgroup, newfile)
            if os.path.isdir(PDF_FOLDER):
                trimatic.export_pdf(pdfgroup, pdfpath)
            else:
                logging.warning(
                    f"PDF folder '{PDF_FOLDER}' not found. "
                    "Skipping copy to shared location."
                )
    except Exception as e:
        # Log any unexpected export failure
        logging.error(f"Failed to export PDF: {e}")

    # Clean up temporary duplicated parts
    trimatic.delete(pdfgroup)
