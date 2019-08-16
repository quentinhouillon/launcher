from tkinter import *
from datetime import datetime
from json import load


def about_launcher():
    # FILE
    with open("file\\theme.json", "r") as theme:
        th = load(theme)

    # VARIABLE
    color1 = th["my_theme"]["bg"]
    color2 = th["my_theme"]["fg"]
    color3 = th["my_theme"]["ft"]
    tf = "consolas"

    window_about = Toplevel()
    date = datetime.now()

    author = "w4rmux"
    name = "Launcher"
    version = "1.0"
    license = "All Right Reserved"

    info = f"L'application open source {name} vous permet de lancer \
vos applications et sites web avec vos mots clés personnalisés que \
vous configuez facilements"

    # CALLBACK
    def _del_window():
        window_about.destroy()

    # WINDOW
    window_about.title("About - Launcher")
    window_about.iconbitmap("img\\launch.ico")
    window_about.geometry("560x300")
    window_about.resizable(False, False)
    window_about.configure(bg=color1)

    # FRAME
    main_about = Frame(window_about, bg=color1)
    footer_about = Frame(window_about, bg=color3)

    # LABEL
    lbl_title = Label(window_about, text="About", bg=color1, fg=color2,
                      font=(tf, 14))

    lbl_author = Label(main_about, text=f"\n\nauthor: {author}", bg=color1,
                       fg=color2, font=tf, anchor="w")

    lbl_name = Label(main_about, text=f"name: {name}", bg=color1, fg=color2,
                     font=tf, anchor="w")

    lbl_version = Label(main_about, text=f"version: {version}", bg=color1,
                        fg=color2, font=tf, anchor="w")

    lbl_license = Label(main_about, text=f"license: {license} \t", bg=color1,
                        fg=color2, font=tf, anchor="w")

    lbl_info = Message(main_about, text=info, bg=color1, fg=color2, font=tf)

    lbl_date = Label(footer_about, text=date.year, bg=color3, fg=color2,
                     font=tf)

    # PACK
    lbl_title.pack(side="top", anchor="center", fill="x")

    lbl_info.pack(side="right", fill="y")
    lbl_author.pack(anchor="w", fill="x")
    lbl_name.pack(anchor="w", fill="x")
    lbl_version.pack(anchor="w", fill="x")
    lbl_license.pack(anchor="w", fill="x")
    main_about.pack(fill="x")

    lbl_date.pack(fill="x", side="right")
    footer_about.pack(fill="x", side="bottom")

    window_about.protocol("WM_DELETE_WINDOW", _del_window)
    window_about.mainloop()


if __name__ == "__main__":
    about_launcher()
