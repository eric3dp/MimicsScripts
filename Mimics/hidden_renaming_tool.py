# Import packages

import mimics
import pickle
import os.path
import numpy as np
import tkinter as tk
from tkinter.colorchooser import *

# Function needed later in the script to transform a color value from an hex format to a rgb format
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

# path to this script file
pathtofile =  os.path.dirname(sys.argv[0]) + r"\data_renaming.p"

# creation of the class RenamingTool in which the tool interface will be described
class RenamingTool:
    def __init__(self, master):
        self.master = master
        self.opened = 0
        master.title = "Renaming Tool"

        frame_liste = tk.Frame(master)
        frame_liste.grid(row = 0, column = 0)

        class Name:
            def __init__(self, name, name_color):
                self.name = name
                self.name_color = name_color

        # when opening the tool, it is checked if a file with a list of names already exist. If not, the tool is open with a list of default names.
        file_exist = os.path.isfile(pathtofile)
        if file_exist:
            data = pickle.load(open(pathtofile, 'rb'))
            liste_names = data[0]
            liste_colors = data[1]
        else:
            liste_names = ["Right Heart", "Left Heart", "Bone", "Stent"]  # Default list of names when opening the tool.
            liste_colors = ["","","",""]


        list_name = tk.Listbox(frame_liste, selectmode = tk.SINGLE, activestyle = "dotbox", selectbackground = "white", selectforeground = "black")
        list_name.pack()

        ind = 0
        for i in liste_names:
            list_name.insert(tk.END, "  " + i)
        for i in liste_colors:
            if i != '':
                list_name.itemconfig(ind, {'bg': i})
                list_name.itemconfig(ind, {'selectbackground': i})
            ind = ind + 1


        def change_name(event):
            if self.opened == 0:
                new_name_index = list_name.curselection()
                new_name = list_name.get(new_name_index[0])
                color = list_name.itemcget(new_name_index[0], "bg")
                if color != "":
                    color_rgb = np.divide(hex_to_rgb(color),255)
                    colour = tuple(color_rgb)

                for i in mimics.data.masks:
                    if i.selected == True:
                        i.name = new_name
                        if color != "":
                            i.color = (float(colour[0]), float(colour[1]), float(colour[2]))

        def open_modify_window():

            frame_modification.grid(row = 0, column = 1)
            button_modify.config(state = 'disabled')
            self.opened = 1

        def close_modify_window():

            frame_modification.grid_forget()
            button_modify.config(state='normal')
            data = [liste_names, liste_colors]
            pickle.dump(data, open(pathtofile, 'wb'))
            self.opened = 0

        ################ Frame modification #######################################################

        frame_modification = tk.Frame(master)


        def add_name():
            new_name = entry.get()
            list_name.insert(tk.END, "  " + new_name)
            liste_names.append(new_name)
            liste_colors.append("")
            entry.delete(0, tk.END)

        def delete_name():
            selection = list_name.curselection()
            del liste_names[selection[0]]
            del liste_colors[selection[0]]
            list_name.delete(selection)

        def getColor():
            color = askcolor()
            index = list_name.curselection()
            list_name.itemconfig(index[0], {'bg': color[1]})
            list_name.itemconfig(index[0], {'selectbackground': color[1]})
            liste_colors[index[0]] = color[1]



        entry = tk.Entry(frame_modification)
        entry.grid(row = 0, column = 0)

        button_add = tk.Button(frame_modification, text = "Add", command = add_name)
        button_add.grid(row = 0, column = 1)

        button_delete = tk.Button(frame_modification, text = "Delete", command = delete_name)
        button_delete.grid(row = 1, column = 0, columnspan = 2)

        button_color = tk.Button(frame_modification, text="Modify Color", command=getColor)
        button_color.grid(row = 2, column = 0, columnspan = 2)

        button_close = tk.Button(frame_modification, text="Ok", command=close_modify_window)
        button_close.grid(row=3, column=0, columnspan = 2)


        #############################################################################################

        button_modify = tk.Button(frame_liste, text = "Modify the list", command = open_modify_window)
        button_modify.pack()

        list_name.bind('<<ListboxSelect>>', change_name)


root = tk.Tk()
renaming_tool = RenamingTool(root)
root.wm_attributes("-topmost", 1)
root.mainloop()