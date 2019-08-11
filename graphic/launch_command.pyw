from tkinter import *
from json import load, dump

# CALLBACK
def run(file):
    from os import startfile; startfile(file)
    window.destroy()

def condition(event):
    if cmd.get() == "show":
        run("graphic\\show_cmd.pyw")
    
    elif cmd.get() == "add":
        run("graphic\\add_cmd.pyw")

# FILE
with open("file\\theme.json", "r") as theme:
    th = load(theme)

# VARIABLE
color1 = th["my_theme"]["bg"]
color2 = th["my_theme"]["fg"]
color3 = th["my_theme"]["ft"]

window = Tk()
var_text = StringVar()
tf = "consolas"

# WINDOW
window.title("list - command")
window.iconbitmap("img\\launch.ico")
window.configure(cursor="pirate", bg=color1)

# FRAME
main = Frame(window, bg=color1)

# LABEL
lbl = Label(main, text="add or show", bg=color1, fg=color2, font=tf)
prompt = Label(main, text=">>", bg=color1, fg=color2, font=tf, anchor="w")

# ENTRY
cmd = Entry(main, bg=color1, fg=color2, font=tf, bd=0, textvariable=var_text, 
            insertbackground=color2)

cmd.focus()
cmd.bind("<Return>", condition)

# GRID
lbl.pack(fill="x")
prompt.pack(side="left")
cmd.pack(fill="x")
main.pack(fill="x")

window.mainloop()
