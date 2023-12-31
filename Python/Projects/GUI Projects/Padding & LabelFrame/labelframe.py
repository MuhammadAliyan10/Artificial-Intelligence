import tkinter as tk
from tkinter import ttk

#------------Starting Header
win = tk.Tk()
win.title("Lable Frames")


#--------------Main Body

lable_frame = ttk.LabelFrame(win,text="Enter you details below")
lable_frame.grid(row=0,column=0,padx=60)

#-----------Creating Lables

labels = ["What is your name:",'What is your age:','What is your gender:','Country:','City:','State:']

for i in range(len(labels)):
    label_var = 'label' + str(i)
    label_var = ttk.Label(lable_frame,text=labels[i])
    label_var.grid(row=i,column=0,sticky=tk.W)

#-----------Creating Entry Box
entry_box = tk.StringVar()
dict_box = {
    'name' : tk.StringVar(), 
    'age' : tk.StringVar(),
    'gender' : tk.StringVar(),
    'country' : tk.StringVar(),
    'city' : tk.StringVar(),
    'state' : tk.StringVar()
}
counter = 0
for i in dict_box:
    dict_entry = 'entry' + i
    dict_entry = ttk.Entry(lable_frame,width=16 ,textvariable = dict_box[i])
    dict_entry.grid(column=1,row=counter)
    counter += 1


#--------To print the value

def action():
    print(dict_box.get('name').get())
    print(dict_box.get('age').get())
    print(dict_box.get('gender').get())
    print(dict_box.get('country').get())
    print(dict_box.get('city').get())
    print(dict_box.get('state').get())



#------------To create a button
sudmit_button = ttk.Button(lable_frame,text="Sudmit", command=action)
sudmit_button.grid(row=7,column=0,sticky=tk.W)


#----------Child Method in lable frame
for child in lable_frame.winfo_children():
    child.grid_configure(padx=4,pady=4)



#------------End Of the body
win.mainloop()