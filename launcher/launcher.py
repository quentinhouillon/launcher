from datetime import datetime
from os import chdir, getcwd, startfile, system
from time import strftime
from tkinter import *
from json import load

from core.clss import *
from core.check_settings import *

def launcher():
    chdir(f"{getcwd()}/../launcher")

    # CALLBACK
    def _del_root():
        root.destroy()

    def run(event):
        global v_entry
        launch = Launcher(e_input.get())
        v_entry = e_input.get()
        e_input.delete(0, END)
        enter = launch.execute_app()
        try:
            response.config(text=enter["text"], fg=enter["fg"])
            response.bind("<Button-1>", starter)

        except:
            pass

    def starter(event):
        if "not found" in response["text"]:
            if COLOR2 == "white":
                startfile(f"https://www.qwant.com/?q={v_entry}&t=web&theme=1")

            else:
                startfile(f"https://www.qwant.com/?q={v_entry}&t=web")

    def change_theme(event):
        launch = Launcher(e_input.get())
        launch.theme_change()
        root.destroy()
        launcher()

    def hour():
        try:
            lbl_time.config(text=strftime("time: %H:%M:%S"))
            root.after(1000, hour)

        except:
            lbl_time.config(text="time: 00:00:00")
            root.after(1000, hour)

    # FILE
    with open("../file/settings.json", 'r') as setttings:
        SETT = load(setttings)

    # VARIABLE
    root = Tk()

    COLOR1 = SETT["my_theme"]["bg"]
    COLOR2 = SETT["my_theme"]["fg"]
    COLOR3 = SETT["my_theme"]["ft"]

    WIDTH = 350
    HEIGHT = 120

    W_SCREEN = root.winfo_screenwidth()
    H_SCREEN = root.winfo_screenheight()

    W_CENTER = int(W_SCREEN-WIDTH-9)
    H_CENTER = int(H_SCREEN/2 + HEIGHT+110)

    TF = SETT["my_theme"]["font"]
    var_entry = StringVar()
    date = datetime.now()

    # ROOT
    root.title("Launcher")
    root.iconbitmap("launch.ico")
    root.geometry(f"{WIDTH}x{HEIGHT}-{W_CENTER}+{H_CENTER}")
    root.minsize(WIDTH, HEIGHT)
    root.configure(bg=COLOR1, padx=5, pady=5)
    root.focus_force()

    # FRAME
    main_frame = Frame(root, bg=COLOR1)
    footer = Frame(root, bg=COLOR1)

    # IMAGE
    logo_theme = PhotoImage(file="img/theme.png")

    # LABEL
    lab = Label(main_frame, text=".: launcher :.".upper(), bg=COLOR1, fg=COLOR2,
                anchor="center", font=TF, pady=8)

    response = Label(root, text="Si besoin, tapez 'help' ou 'about'",
                     bg=COLOR1, fg=COLOR2, anchor="w", font=(TF, 8), pady=8)

    lbl_time = Label(footer, text="time: 00:00:00", bg=COLOR3,
                     fg=COLOR2, font=(TF, 9))

    lbl_theme = Label(footer, image=logo_theme, bg=COLOR1, anchor="center")
    lbl_theme.bind("<Button-1>", change_theme)
    lbl_date = Label(
        footer, text=date.year, bg=COLOR3, fg=COLOR2, font=(TF, 10))

    # ENTRY
    e_input = Entry(main_frame, bd=0, bg=COLOR3, fg=COLOR2,
                    insertbackground=COLOR2, textvariable=var_entry,
                    font=TF)

    e_input.focus()
    e_input.bind('<Return>', run)

    # PACK
    lab.pack()
    e_input.pack(fill='x')
    main_frame.pack(fill='both')

    response.pack(anchor="w")

    lbl_time.pack(side="left")
    lbl_date.pack(side="right")
    lbl_theme.pack(anchor="center")
    footer.pack(fill="x", side="bottom")

    root.after(1000, hour)
    root.mainloop()


if __name__ == "__main__":
    checking()
    launcher()
