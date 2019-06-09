from tkinter import *
from json import load, dump

def launch_command(file):
    with open(file, 'r') as f:
        run = load(f)
        for r in run:
            display_run.insert(INSERT, f"""
lnk: {r["lnk"]};
app: {r["app"]};
cmd: {r["cmd"]}
""")


with open("file\\theme.json", "r") as theme:
    th = load(theme)

color1 = th["my_theme"]["bg"]
color2 = th["my_theme"]["fg"]
color3 = th["my_theme"]["ft"]

tf = "consolas"

#WINDOW
window = Tk()
window.geometry("600x650")
window.minsize(600, 650)
window.title("Launch Command")
window.iconbitmap("img\\favicon.ico")
window.configure(cursor="pirate", bg=color1)

#TEXT
display_run = Text(bd=0, bg=color1, fg=color2, font=(tf, 10))

#PACK
display_run.pack(fill="y", expand="true")
launch_command("file\\run.json")

window.mainloop()
