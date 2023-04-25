from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
import os

root = Tk()
root.config(highlightthickness=0, background="#DFEEED")

window_width = 360
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.overrideredirect(True)

canvas = Canvas(root, width=360, height=344, highlightthickness=0) 
canvas.pack()
image = PhotoImage(file='images//logo.png')
canvas.create_image(180, 172, image=image)
canvas.config(background="#DFEEED") 

progress_label=Label(root, text="Loading... ", 
                     font=("Microsoft JhengHei", "11"), 
                     fg="#497687", bg="#DFEEED")
progress_label.place(relx=0.5, rely=0.87, anchor="center")

style = ttk.Style()
style.theme_use('clam')
style.configure("red.Horizontal.TProgressbar", 
                background='#DFEEED', troughcolor='#497687')

progress = Progressbar(root, orient=HORIZONTAL, 
                       length=300, mode='determinate', 
                       style="red.Horizontal.TProgressbar")
progress.place(relx=0.5, rely=0.93, anchor="center")

def openLoginAdmin():
    root.withdraw() 
    os.system("python login_admin.py")
    root.destroy()

def load():
    progress['value'] += 10
    if progress['value'] < 100:
        txt = "Loading... " + (str(int(progress['value']))+'%')
        progress_label.config(text=txt)
        root.after(1200, load)
    else:
        openLoginAdmin()

load()

root.resizable(False, False)
root.mainloop()
