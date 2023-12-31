import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Menu-Bar")

menu_bar = tk.Menu(win)



def func():
    print("File Working")

#======================================Simple Menu Bar================================================
# win.config(menu = menu_bar)
# menu_bar.add_command( label='File', command=func)
# menu_bar.add_command( label='Edit', command=func)
# menu_bar.add_command( label='Selection', command=func)
# menu_bar.add_command( label='View', command=func)
# menu_bar.add_command( label='Go', command=func)

#=========================================Dropdown or sub menu bar=========================================




main_menu = tk.Menu(menu_bar)

#--------First Meun
file_menu = tk.Menu(main_menu,tearoff=0)
file_menu.add_command(label="Save", command=func)
file_menu.add_command(label="Save As", command=func)
file_menu.add_separator()
file_menu.add_command(label="OpenAs", command=func)

#Second Menu

edit_menu = tk.Menu(main_menu,tearoff=0)
edit_menu.add_command(label='Undo', command=func)
edit_menu.add_command(label='Redo', command=func)


#--------------For add main to sub
main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label="Edit", menu=edit_menu)





win.config(menu=main_menu)




win.mainloop()