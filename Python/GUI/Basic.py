import tkinter as tk

window = tk.Tk()
window.title("Basic")

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")


window_width = 800
window_height = 600
center_window(window, window_width, window_height)

# Create widgets inside the frame
label1 = tk.Label(window, text="Label 1", bg="lightblue")
label1.pack()

label2 = tk.Label(window, text="Label 2", bg="lightgreen")
label2.pack()

# Position widgets relative to each other
label1.pack(side="left",padx=10)

def submit():
    value = entry.get()
    print("Submitted:", value)

entry = tk.Entry(window, width=30)
entry.pack(pady=10)
label2.pack(side="left",pady=20)

submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack()


window.config(bg='lightblue')
window.mainloop()