
#-----------------------------------------------------------For Importing Modules---------------------------------------------------------------#

import tkinter as tk
from tkinter import ttk

#------------------------------------------------------------Starting Header------------------------------------------------------------------#

win = tk.Tk()
win.title("VS Code")
menu_bar = tk.Menu(win)

#--------------------------------------------------------------For Menu Bar--------------------------------------------------------------------#

main_menu = tk.Menu(menu_bar)
win.config(menu=main_menu)

#--------------Fuction
def file1():
    pass


#-----------First Menu
file_menu = tk.Menu(main_menu,tearoff=0)
file_menu.add_command(label="New Text File", command=file1)
file_menu.add_command(label="New File", command=file1)
file_menu.add_command(label="New Window", command=file1)
file_menu.add_separator()
file_menu.add_command(label="Open File", command=file1)
file_menu.add_command(label="Open Folder", command=file1)


#-----------Second Menu
edit_menu = tk.Menu(main_menu,tearoff=0)
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")
edit_menu.add_separator()
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")


#-----------Third Menu
selection_menu = tk.Menu(main_menu,tearoff=0)
selection_menu.add_command(label="Select All")
selection_menu.add_command(label="Expend Selection")
selection_menu.add_command(label="Shrink Selection")
selection_menu.add_separator()
selection_menu.add_command(label="Copy line Up")
selection_menu.add_command(label="Copy line down")

#-----------Second Menu
view_menu = tk.Menu(main_menu,tearoff=0)
view_menu.add_command(label="Command Palatte")
view_menu.add_command(label="Open View")
view_menu.add_separator()
view_menu.add_command(label="Apperence")
view_menu.add_command(label="Edit Layout")
view_menu.add_separator()
view_menu.add_command(label="Apperence")


#-----------Second Menu
go_menu = tk.Menu(main_menu,tearoff=0)
go_menu.add_command(label="Back")
go_menu.add_command(label="Forwad")
go_menu.add_command(label="Last Edit Location")
go_menu.add_separator()
go_menu.add_command(label="Switch Editor")
go_menu.add_command(label="Switch Group")


#-----------Second Menu
help_menu = tk.Menu(main_menu,tearoff=0)
help_menu.add_command(label="Welcome")
help_menu.add_command(label="Show All Commands")
help_menu.add_command(label="Docomentation")
help_menu.add_command(label="Editor Playground")
help_menu.add_command(label="Show Realase Notes")

#-----------Add cascade
main_menu.add_cascade(label="File", menu= file_menu)
main_menu.add_cascade(label="Edit", menu=edit_menu)
main_menu.add_cascade(label="Section", menu=selection_menu)
main_menu.add_cascade(label="View", menu=view_menu)
main_menu.add_cascade(label="Go", menu=go_menu)
main_menu.add_cascade(label="Help", menu=help_menu)


#-----------------------------------------------------------------------------------------------------------------------------------------------#












#-------------------------------------------------------------Closing Header-----------------------------------------------------------#
win.mainloop()