import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,messagebox,filedialog
import os

#----------------------------------------------_Starter_---------------------------------------------------------------

#-----Head starter
main_application = tk.Tk()
main_application.title("Text Editor")

#----------------------------------------------_Main_MenuBar_-----------------------------------------------------------

main_menubar = tk.Menu()
main_application.config(menu =main_menubar)


#------------------------------------Funcnality of Menus.....

url = ''

#--------------For New File

def new_file(event=None):
    global url
    text_editor.delete(1.0, tk.END)

#--------------For open
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File',filetypes=(('Text File',"*.txt"),('All Files', '*.*')))
    try:
        with open (url, 'r') as rf:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, rf.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))


#-----------------------For Save File

def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.End))
            with open(url, 'w', encoding='utf-8') as f:
                f.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w',defaultextension='.txt',filetypes=(('Text File',"*.txt"),('All Files', '*.*')))
            content2 = text_editor.get(1.0, tk.End)
            url.write(content2)
            url.close()
    except:
        return
    

#------------------Save as


#----------File Menu
file = tk.Menu(main_menubar, tearoff=False)
file.add_command(label="New" ,accelerator="Ctrl+N", command =new_file)
file.add_command(label="Open",accelerator="Ctrl+O" ,command = open_file)
file.add_command(label="Save",accelerator="Ctrl+S", command= save_file)
file.add_command(label="Save As",accelerator="Ctrl+Alt+S")
file.add_command(label="Exit",accelerator="Ctrl+Q")

#----------Edit Menu
edit = tk.Menu(main_menubar, tearoff=False)
edit.add_command(label="Copy" ,accelerator="Ctrl+C")
edit.add_command(label="Page",accelerator="Ctrl+V")
edit.add_command(label="Cut",accelerator="Ctrl+X")
edit.add_command(label="Clear All",accelerator="Ctrl+Alt+X")
edit.add_command(label="Find",accelerator="Ctrl+F")

#----------View Menu
view = tk.Menu(main_menubar, tearoff=False)
view.add_checkbutton(label="Tool bar")
view.add_checkbutton(label="Status bar")

#----------Color Theme Menu
light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')

color_theme = tk.Menu(main_menubar, tearoff=False)

theme_choice = tk.StringVar()
color_icons = (light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon )
color_dict = {
    'Light Default': ("#000000", '#ffffff'),
    'Light Plus' : ('#474747','e0e0e0'),
    'Dark': ('#c4c4c4','2d2d2d'),
    'Red' : ('2d2d2d', '#ffe8e8'),
    'Monokai': ('#d3b774','#474747'),
    'Night Blue' : ('#ededed','#6b9dc2')
}
count = 0
for key in color_dict:
    color_theme.add_radiobutton(label= key, image=color_icons[count], variable= theme_choice, compound=tk.LEFT)
    count += 1


#--------------Add the menus
main_menubar.add_cascade(label="File", menu=file)
main_menubar.add_cascade(label="Edit", menu=edit)
main_menubar.add_cascade(label="View", menu=view)
main_menubar.add_cascade(label="Color", menu=color_theme)


















#----------------------------------------------_End_Menubar_------------------------------------------------------------


#----------------------------------------------_Start-Toolbar------------------------------------------------------------
tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)

#-------------For selection of font family
font_tupel = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar ,width=30, textvariable= font_family, state='readonly')
font_box['values'] = font_tupel
font_box.current(font_tupel.index('Arial'))
font_box.grid(row=0,column=0,padx=5)

#-------------For selction of font size
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=14, textvariable=size_var, state='readonly')
font_size['values']= tuple(range(8,100,2))
font_size.current(2)
font_size.grid(row=0, column=1,padx=4)

#-----------------Bold Button
bold_icon = tk.PhotoImage(file= 'icons2/bold.png')
bold_button = ttk.Button(tool_bar, image=bold_icon)
bold_button.grid(row=0,column=2,padx=5)
#------------------Italic Button
italic_icon = tk.PhotoImage(file= 'icons2/italic.png')
italic_button = ttk.Button(tool_bar, image=italic_icon)
italic_button.grid(row=0,column=3,padx=5)
#-----------------underline Button
underline_icon = tk.PhotoImage(file= 'icons2/underline.png')
underline_button = ttk.Button(tool_bar, image=underline_icon)
underline_button.grid(row=0,column=4,padx=5)
#------------------Font Color Button
font_color_icon = tk.PhotoImage(file='icons2/font_color.png')
font_color_btn = ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)
#------------------Font Align-Left Button
alignleft_icon = tk.PhotoImage(file='icons2/align_left.png')
alignleft_btn= ttk.Button(tool_bar,image=alignleft_icon)
alignleft_btn.grid(row=0,column=6,padx=5)
#------------------Font Align-Center Button
aligncenter_icon = tk.PhotoImage(file='icons2/align_center.png')
aligncenter_btn= ttk.Button(tool_bar,image=aligncenter_icon)
aligncenter_btn.grid(row=0,column=7,padx=5)
#------------------Font Align-right Button
alignright_icon = tk.PhotoImage(file='icons2/align_right.png')
alignright_btn= ttk.Button(tool_bar,image=alignright_icon)
alignright_btn.grid(row=0,column=8,padx=5)


#----------------------------------------------Functionalty Of buttons


#------Change Bold
def change_bold():
    text_property = tk.font.Font(font= text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font = (current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font = (current_font_family,current_font_size, 'normal'))

bold_button.config(command= change_bold)

#------Change Italic
def change_italic():
    text_property = tk.font.Font(font= text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font = (current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font = (current_font_family,current_font_size, 'roman'))

italic_button.config(command= change_italic)

#------Change underline
def change_underline():
    text_property = tk.font.Font(font= text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font = (current_font_family,current_font_size,'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font = (current_font_family,current_font_size, 'normal'))

underline_button.config(command= change_underline)

#-------------Change Font Color

def change_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command=change_color)

#-----------------Change Align to left

def align_left():
    text_contant = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, 'end')
    text_editor.insert(tk.INSERT, text_contant, 'left')


alignleft_btn.configure(command=align_left)

#-----------------Change Align to Center

def align_center():
    text_contant = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, 'end')
    text_editor.insert(tk.INSERT, text_contant, 'center')


aligncenter_btn.configure(command=align_center)

#-----------------Change Align to Right

def align_right():
    text_contant = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, 'end')
    text_editor.insert(tk.INSERT, text_contant, 'right')


alignright_btn.configure(command=align_right)


#----------------------------------------------_End-Toolbar-------------------------------------------------------------------

#----------------------------------------------Start_Text_Editor_-------------------------------------------------------------------


text_editor = tk.Text(main_application)
text_editor.config(wrap='word', relief=tk.FLAT)

scroll_bar = ttk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side = tk.RIGHT, fill= tk.Y)
text_editor.pack(expand=True, fill=tk.BOTH)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

#------------------------------------------Fuctionality of Text Editor




current_font_family = 'Arial'
current_font_size = 12
text_editor.configure(font=('Arial',12))

def font_change(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font = (current_font_family,current_font_size))

def fontsize_change(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font = (current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>", font_change)
font_size.bind("<<ComboboxSelected>>", fontsize_change)

#----------------------------------------------End_text_Editor_---------------------------------------------------------------------



#----------------------------------------------Start_Status_Bar----------------------------------------------------------------------------


status_bar = ttk.Label(main_application,text="Status Bar")
status_bar.pack(side=tk.BOTTOM)


#-------------------------Functionalty of Status Bar
text_changed = False
def changed(event= None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f"Characters : {characters} Words : {words}")
    text_editor.edit_modified(False)
text_editor.bind("<<Modified>>",changed)

#-----------------------------------------------End_Status_Bar--------------------------------------------------------------------------------













#----------------------------------------------_Ender_-----------------------------------------------------------
main_application.mainloop()