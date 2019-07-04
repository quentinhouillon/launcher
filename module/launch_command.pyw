from tkinter import *
from json import load, dump

def open_js(file):
    with open(file, 'r') as f:
        global run
        run = load(f)

def show():
    open_js("file\\run.json")
    
    for r in run:
        display_run.insert(INSERT, f"""
lnk: {r["lnk"]};
app: {r["app"]};
cmd: {r["cmd"]}
""")

def add():
    from os import startfile; startfile("module\\add_cmd.pyw")

def condition(event):
    if cmd.get() == "show":
        show()
    
    elif cmd.get() == "add":
        add()

with open("file\\theme.json", "r") as theme:
    th = load(theme)

color1 = th["my_theme"]["bg"]
color2 = th["my_theme"]["fg"]
color3 = th["my_theme"]["ft"]

window = Tk()
tf = "consolas"
var_text = StringVar()

#WINDOW
window.geometry("600x650")
window.minsize(600, 650)
window.title("Launch")
window.iconbitmap("img\\favicon.ico")
window.configure(cursor="pirate", bg=color1)

#FRAME
main = Frame(window, bg=color1)

#LABEL
lbl = Label(main, text="add or show", bg=color1, fg=color2, font=tf)
prompt = Label(main, text=">>", bg=color1, fg=color2, font=tf, anchor="w")

#TEXT
display_run = Text(bd=0, bg=color1, fg=color2, font=(tf, 10))

# ENTRY
cmd = Entry(main, bd=0, bg=color1, fg=color2, font=tf, textvariable=var_text,
            insertbackground=color2)
cmd.focus()
cmd.bind('<Return>', condition)

#GRID
lbl.pack(fill="x")
prompt.pack(side="left")
cmd.pack(fill="x")
main.pack(fill="x")

display_run.pack(fill="y", expand="true")

window.mainloop()
