from tkinter import *
from json import dump, load

def main_show():
    # FILE
    with open("file\\run.json", "r") as run:
        run = load(run)

    with open("file\\theme.json", "r") as theme:
        th = load(theme)

    # CALLBACK
    def _show():
        for r in run:
            display_run.insert(INSERT, f"""
    app: {r["app"]}
    lnk: {r["lnk"]}
    cmd: {r["cmd"]}
    """)

    # VARIABLE
    color1 = th["my_theme"]["bg"]
    color2 = th["my_theme"]["fg"]
    color3 = th["my_theme"]["ft"]

    window = Tk()
    var_text = StringVar()
    tf = "consolas"

    # WINDOW
    window.geometry("600x650")
    window.minsize(600, 650)
    window.title("show - cmd")
    window.iconbitmap("img\\launch.ico")
    window.configure(bg=color1)

    # FRAME
    main = Frame(window, bg=color1)

    # TEXT
    display_run = Text(main, bd=0, bg=color1, fg=color2, font=(tf, 10))

    # PACK
    display_run.pack(fill="y", expand="true")
    main.pack(fill="y", expand="true")

    _show()

