from tkinter import *
from tkinter import messagebox
import random


answers = ["   Yes",
"   No",
"   Maybe",
'''It is up
to you''',
" I'm sure",
'''   try 
   again''',
'''  god
  knows''',
'''definitely
yes''',
''' obviously
  no''']


window = Tk()
window.title("8 ball")
window.configure(background='PaleTurquoise')
canvas = Canvas(window, width=500, height=550)
Label(window, text='Enter Your Question & hit Enter Key', fg="Blue", font="Courier 15").pack(pady=20)
canvas.configure(background='Turquoise')
canvas.create_oval(5, 5, 500, 500, outline="blue",fill="black", width=2)
canvas.create_oval(130, 130, 370, 370, outline="silver", width=4)
canvas.create_polygon([140, 210], [360, 210], [250, 370], fill="DarkBlue", outline="white")
lbl = Label(window, text="", fg="white", bg="DarkBlue", font="Courier 14")

def ask_the_ball(question):
    question = e1.get()
    if "?" in question:
        lbl["text"] = random.choice(answers)
        lbl.place(x=190, y=300)
    else:
        return messagebox.showinfo("Sorry","I don't see a question :(")


e1 = Entry(window, width=70)
e1.bind('<Return>', ask_the_ball)
e1.place(x=50, y=580)

canvas.pack()

window.mainloop()
