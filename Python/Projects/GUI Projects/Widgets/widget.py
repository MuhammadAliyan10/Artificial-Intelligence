import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
#------------Starring Header
win = tk.Tk()
win.title("Widget")

#----------Creating Labels

labels = ["What is your name:",'What is your age:','What is your gender:','Country:','City:','State:']

for i in range(len(labels)):
    label_var = 'label' + str(i)
    label_var = ttk.Label(win,text=labels[i])
    label_var.grid(row=i,column=0,sticky=tk.W,padx=3,pady=3)

#-------------Creating EntryBox
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
    dict_entry = ttk.Entry(win,width=16 ,textvariable = dict_box[i])
    dict_entry.grid(column=1,row=counter,padx=3,pady=3)
    counter += 1

#---------Making button Action



#--------To print the value

# def action():
#     print(dict_box.get('name').get())
#     print(dict_box.get('age').get())
#     print(dict_box.get('gender').get())
#     print(dict_box.get('country').get())
#     print(dict_box.get('city').get())
#     print(dict_box.get('state').get())


#-----To save the value in Csv file

def action():
    user_name = dict_box.get('name').get()
    user_age = dict_box.get('age').get()
    user_gender =dict_box.get('gender').get()
    user_country =dict_box.get('country').get()
    user_city = dict_box.get('city').get()
    user_state =dict_box.get('state').get()



    with open ('user_info.csv', 'a',newline="") as a:
        user_value = DictWriter(a, fieldnames= ['username','userage','usergender','usercountry','usercity','userstate'])
        if os.stat('user_info.csv').st_size == 0:
             user_value.writeheader()

        user_value.writerow({
        'username' : user_name,
        'userage': user_age,
        'usergender': user_gender,
        'usercountry': user_country,
        'usercity': user_city,
        'userstate': user_state
     })
    
    dict_entry.delete(0,tk.END)




#----------Making Button
sudmit_button = ttk.Button(win,text="Sudmit", command=action)
sudmit_button.grid(row=7,column=0,sticky=tk.W)




win.mainloop()