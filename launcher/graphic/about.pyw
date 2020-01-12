from tkinter import *
from datetime import datetime
from json import load


def about_launcher():
    # FILE
    with open("../file/settings.json", "r") as settings:
        SETT = load(settings)

    # VARIABLE
    color1 = SETT["my_theme"]["bg"]
    color2 = SETT["my_theme"]["fg"]
    color3 = SETT["my_theme"]["ft"]
    TF = SETT["my_theme"]["font"]

    WIDTH = "560"
    HEIGHT = "300"

    window_about = Toplevel()
    date = datetime.now()

    author = "w4rmux"
    name = "Launcher"
    version = "2.3"
    license = "(C) Tous Droits Réservés"

    info = f"L'application open source {name} vous permet de lancer \
vos applications et sites web avec vos propre mots clés que \
vous personnalisés facilements"

    # CALLBACK
    def _del_window():
        window_about.destroy()

    # WINDOW
    window_about.title("About - Launcher")
    window_about.iconbitmap("launch.ico")
    window_about.geometry(f"{WIDTH}x{HEIGHT}")
    window_about.resizable(False, False)
    window_about.configure(bg=color1)
    window_about.focus_force()

    # FRAME
    main_about = Frame(window_about, bg=color1)
    footer_about = Frame(window_about, bg=color3)

    # LABEL
    lbl_title = Label(window_about, text="About", bg=color1, fg=color2,
                      font=(TF, 14))

    lbl_author = Label(main_about, text=f"\n\nAuteur: {author}", bg=color1,
                       fg=color2, font=TF, anchor="w")

    lbl_name = Label(main_about, text=f"Programme: {name}", bg=color1, fg=color2,
                     font=TF, anchor="w")

    lbl_version = Label(main_about, text=f"version: {version}", bg=color1,
                        fg=color2, font=TF, anchor="w")

    lbl_license = Label(main_about, text=f"license: {license} \t", bg=color1,
                        fg=color2, font=TF, anchor="w")

    lbl_info = Message(main_about, text=info, bg=color1, fg=color2, font=TF)

    lbl_date = Label(footer_about, text=date.year, bg=color3, fg=color2,
                     font=TF)

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
