import tkinter as tk
from tkinter import filedialog

def choose_file(filetypes=None):
    """
    Opens a file picker dialog and returns the selected file path.

    Parameters:
        filetypes (list of tuples, optional): e.g., [("CSV files", "*.csv"), ("Text files", "*.txt")]

    Returns:
        str: Path to selected file, or empty string if cancelled.
    """
    if filetypes is None:
        filetypes = [("All files", "*.*")]

    root = tk.Tk() # make an empty window
    root.withdraw() # hide it
    path = filedialog.askopenfilename(filetypes=filetypes)
    root.destroy() # destroy the empty window
    return path
