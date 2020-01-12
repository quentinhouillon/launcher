from tkinter import *
from json import dump, load

def main_show():
    # FILE
    with open("../file/launcher.json", "r") as run:
        run = load(run)

    with open("../file/settings.json", "r") as settings:
        SETT = load(settings)

    # CALLBACK
    def _show():
        for r in run:
            display_run.insert(INSERT, f"""
    app: {r["app"]}
    lnk: {r["lnk"]}
    cmd: {r["cmd"]}
    """)

    # VARIABLE
    COLOR1 = SETT["my_theme"]["bg"]
    COLOR2 = SETT["my_theme"]["fg"]
    COLOR3 = SETT["my_theme"]["ft"]

    window = Tk()
    var_text = StringVar()
    TF = SETT["my_theme"]["font"]

    # WINDOW
    window.geometry("600x650")
    window.minsize(600, 650)
    window.title("show - cmd")
    window.iconbitmap("launch.ico")
    window.configure(bg=COLOR1)
    window.focus_force()

    # FRAME
    main = Frame(window, bg=COLOR1)

    # TEXT
    display_run = Text(main, bd=0, bg=COLOR1, fg=COLOR2, font=(TF, 10))

    # PACK
    display_run.pack(fill="y", expand="true")
    main.pack(fill="y", expand="true")

    _show()

