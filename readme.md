# MimicsScripts
This repository contains my Python scripts for automating tasks within Materialise Mimics and 3-matic. These scripts streamline repetitive processes and introduce greater consistency to my process. 
## Caveats
I'm a "fake" programmer, so an unhealthy amount of this code was written by LLMs. It lacks good error checking and documentation. It's also built very specifically for my personal use. They are provided as-is with no guarantees or formal support.
## Scripts Overview
### 3-Matic
- **`boolean_union.py`** - Merges selected parts into a single entity using the boolean union operation
- **`export3MF.py`** - Exports selected parts and groups as 3MFs. Renames parts based on project folder and group name
- **`hollow.py`** - Creates a hollow, saves the original solid to a Solids group
- **`cylinderbase.py`** - (INCOMPLETE) Creates a cylindrical base for the selected parts & groups. Labeling is currently broken
- **`exportPDF.py`** - Duplicates and reduces, then exports selected parts as 3D PDF in project folder and network folder
- **`move_to_trash.py`** - Checks for Trash group, creates & hides if it doesn't exist, moves selected parts
- **`set_part_colors.py`** - Recolor parts based on name`
- **`unify_for_preform`** - (INCOMPLETE) Create single STL for PreForm, since it doesn't read 3MF correctly
### Mimics
- **`airway.py`** - (INCOMPLETE) Automatically segment airway for heart prints
- **`hidden_UI.py`** - Adds a floating window to allow easier script execution
- **`mimics_color.py`** - Recolor parts & masks based on name
## Dependencies
   These scripts use the `trimatic` and `mimics` modules, which provide an interface with Mimics and 3-matic. Ensure they are accessible within your scripting environment. It also uses `tkinter`, `os`, `pickle`, `numpy`, `pygetwindow`, `time`, `threading`, and `subprocess`.