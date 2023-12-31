#In this file we make an app of gui with the help of some python modules...


#-------Imported File------#

import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os

#-------Starter Code------#

win = tk.Tk()
win.title("GUI")

#-----Main Code-------#


#----For name
name_lable = ttk.Label(win,text="Enter your name:")
name_lable.grid(row=0,column=0,sticky=tk.W)
#----For Email
email_lable = ttk.Label(win,text="Enter your email:")
email_lable.grid(row=1,column=0,sticky=tk.W)
#----For Age
age_lable = ttk.Label(win,text="Enter your age:")
age_lable.grid(row=2,column=0,sticky=tk.W)
#----For Gender
gender_lable = ttk.Label(win,text="Enter your Gender:")
gender_lable.grid(row=3,column=0,sticky=tk.W)


#-----------Entry Box for name
name_var = tk.StringVar()
name_entry_box = ttk.Entry(win, width=16,textvariable= name_var)
name_entry_box.grid(row=0,column=1)
name_entry_box.focus()

#-----------Entry Box for Email
email_var = tk.StringVar()
email_entry_box = ttk.Entry(win, width=16,textvariable= email_var)
email_entry_box.grid(row=1,column=1)


#-----------Entry Box for age
age_var = tk.StringVar()
age_entry_box = ttk.Entry(win, width=16,textvariable= age_var)
age_entry_box.grid(row=2,column=1)

#----------Create Combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win, width=13, textvariable=gender_var,state='readonly')
gender_combobox['values'] = ('Male','Female','Other')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)

#-------------Create Radio Button
radiobutton_var = tk.StringVar()
radiobutton1 = ttk.Radiobutton(win, text='Student' ,value='Student',variable= radiobutton_var)
radiobutton1.grid(row=4,column=0)
radiobutton2 = ttk.Radiobutton(win, text='Teacher' ,value='Teacher',variable= radiobutton_var)
radiobutton2.grid(row=4,column=1)

#-----------Check Button
checkbtn_var = tk.IntVar()
check_btn = tk.Checkbutton(win, text="Check if you already have an account",variable= checkbtn_var)
check_btn.grid(row=5,columnspan=3)




#---------Action on the button
# def action():
#     user_name = name_var.get()
#     user_email = email_var.get()
#     user_age = age_var.get()
#     user_gender = gender_var.get()
#     print(f'The name of the user is {user_name} and he is {user_age} years old and his/her email is {user_email}.His/her gender is {user_gender}')
#     user_type = radiobutton_var.get()
#     if checkbtn_var == 0:
#         login = 'No'
#     else:
#         login = 'Yes'
#     print(f"{user_name} is a {user_type} and the login result is {login}")


#----------Store data in file

    # with open('user_info.txt', 'a') as f:
    #  f.write(f"{user_name},{user_age},{user_email},{user_gender},{user_type},{login}\n")

#-------To clear the textbox after adding the data in file
    # name_entry_box.delete(0,tk.END)
    # email_entry_box.delete(0,tk.END)
    # age_entry_box.delete(0,tk.END)

#--------To change the color of the lable
    # name_lable.configure(foreground='red')



#=================================================For CSV files======================================================

def action():
    user_name = name_var.get()
    user_email = email_var.get()
    user_age = age_var.get()
    user_gender = gender_var.get()
    user_type = radiobutton_var.get()
    if checkbtn_var == 0:
        login = 'No'
    else:
        login = 'Yes'

#--------CSV File Create and write
    with open('user_info.csv', 'a', newline="") as f:
        dict_writer = DictWriter(f, fieldnames=['user_name', 'user_age','user_email','user_gender','user_type','login'])
        if os.stat('user_info.csv').st_size == 0:
            dict_writer.writeheader()

        dict_writer.writerow({
            'user_name': user_name,
            'user_age' : user_age,
            'user_email' : user_email,
            'user_gender': user_gender,
            'user_type' : user_type,
            'login' : login
        })

    name_entry_box.delete(0,tk.END)
    email_entry_box.delete(0,tk.END)
    age_entry_box.delete(0,tk.END)

#----------Sudmit Button
sudmit_button = ttk.Button(win,text='Sudmit',command= action)
sudmit_button.grid(row=6,column=0,sticky=tk.W)

#------End Code-----#
win.mainloop()