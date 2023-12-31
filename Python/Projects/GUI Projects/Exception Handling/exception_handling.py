import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox as m_box

win = tk.Tk()
win.title('Exception Handling')



label_box = ttk.LabelFrame(win, text="Enter your information below")
label_box.grid(row=0,column=0, pady=40,padx=80)


name_var =tk.StringVar()
label1 = ttk.Label(label_box, text="Enter you name:",font=('Helveltica', 10,'bold'))
label1.grid(row=0,column=0,sticky=tk.W,pady=5,padx=6)
entry1 = ttk.Entry(label_box, width=40, textvariable=name_var)
entry1.grid(row=1,column=0,sticky=tk.W,pady=19,padx=6)



age_var = tk.StringVar()
label2 = ttk.Label(label_box, text="Enter you age:",font=('Helveltica', 10,'bold'))
label2.grid(row=0, column=6,sticky=tk.W ,pady=8,padx=16)
entry2 = ttk.Entry(label_box, width=40, textvariable=age_var)
entry2.grid(row=1,column=6,pady=19,padx=6)


def sudmit():
    # m_box.showinfo('title','You contant show here')
    # m_box.showerror('title','You contant show here')
    # m_box.showwarning('title','You contant show here')
    name = name_var.get()
    age = age_var.get()
    if name=="" or age =="":
        m_box.showerror("Error","Please enter your name and age")
    elif name == "":
        m_box.showerror("Error","Please enter your name")
    elif age == "":
        m_box.showerror("Error","Please enter your age")

    try:
        age = int(age)
    except ValueError:
        m_box.showerror("Error","Please use numeric value")
    else:
        if age < 18:
            m_box.showwarning("Age Warning","You are under 18,Click ok if you want to login")
        else:
            print(f"The name of the user is {name} and the age of the user is {age}")


sudmit_btn = ttk.Button(label_box, text="Sudmit", command=sudmit)
sudmit_btn.grid(row=3,columnspan=7)











win.mainloop()