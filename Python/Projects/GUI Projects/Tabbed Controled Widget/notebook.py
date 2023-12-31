import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Note Book')

nb = ttk.Notebook(win)
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)

nb.add(page1,text="User Info")
nb.add(page2, text='User Login')
# nb.grid(row=0,column=0)
nb.pack(expand=True, fill="both")

label1 = ttk.Label(page1, text="Enter your first name:")
label1.grid(row=0,column=0)

entry1 = ttk.Entry(page1,width=16)
entry1.grid(row=0,column=1)

label2 = ttk.Label(page2, text="Enter your ID:")
label2.grid(row=0,column=0)

entry2 = ttk.Entry(page2,width=16)
entry2.grid(row=0,column=1)











win.mainloop()