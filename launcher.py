from datetime import datetime
from os import chdir, getcwd, startfile, system
from time import strftime
from tkinter import *
from json import load

from core.clss import *


def launcher():
    chdir(getcwd())

    # CALLBACK
    def _del_window():
        window.destroy()

    def run(event):
        global v_entry
        launch = Launcher(e_input.get())
        v_entry = e_input.get()
        e_input.delete(0, END)
        enter = launch.execute_app()
        try:
            response.config(text=enter["text"], fg=enter["fg"])
            if "not found" in enter["text"]:
                response.bind("<Button-1>", starter)

        except:
            pass

    def starter(event):
        if color2 == "white":
            startfile(f"https://www.qwant.com/?q={v_entry}&t=web&theme=1")
        else:
            startfile(f"https://www.qwant.com/?q={v_entry}&t=web")

    def change_theme(event):
        launch = Launcher(e_input.get())
        launch.theme_change()
        window.destroy()
        launcher()

    def hour():
        try:
            lbl_time.config(text=strftime("time: %H:%M:%S"))
            window.after(1000, hour)

        except:
            lbl_time.config(text="time: 00:00:00")
            window.after(1000, hour)

    # FILE
    with open("file\\theme.json", 'r') as theme:
        th = load(theme)

    # VARIABLE
    window = Tk()

    color1 = th["my_theme"]["bg"]
    color2 = th["my_theme"]["fg"]
    color3 = th["my_theme"]["ft"]

    width = 350
    height = 90

    w_screen = window.winfo_screenwidth()
    h_screen = window.winfo_screenheight()

    w_center = int(w_screen-width-9)
    h_center = int(h_screen/2 + height+170)

    tf = "consolas"
    var_entry = StringVar()
    date = datetime.now()

    # WINDOW
    window.title("Launcher")
    window.iconbitmap("img\\launch.ico")
    window.geometry(f"{width}x{height}-{w_center}+{h_center}")
    window.minsize(width, height)
    window.configure(bg=color1)
    window.focus_force()

    # FRAME
    main_frame = Frame(window, bg=color1)
    footer = Frame(window, bg=color3)

    # IMAGE
    logo_theme = PhotoImage(file="img\\theme.png")

    # LABEL
    lab = Label(main_frame, text=".: laucher :.".upper(), bg=color1, fg=color2,
                anchor="center", font=tf)

    prompt = Label(main_frame, text=">>", bg=color1, fg=color2, font=tf)
    response = Label(window, text="if you need you can enter 'help' or 'about'",
                     bg=color1, fg=color2, anchor="w", font=(tf, 8))

    lbl_time = Label(footer, text="time: 00:00:00", bg=color3,
                     fg=color2, font=(tf, 9))

    lbl_theme = Label(footer, image=logo_theme, bg=color3, anchor="center")
    lbl_theme.bind("<Button-1>", change_theme)
    lbl_date = Label(
        footer, text=date.year, bg=color3, fg=color2, font=(tf, 10))

    # ENTRY
    e_input = Entry(main_frame, bd=0, bg=color1, fg=color2,
                    insertbackground=color2, textvariable=var_entry,
                    font=tf)

    e_input.focus()
    e_input.bind('<Return>', run)

    # PACK
    lab.pack()
    prompt.pack(side="left")
    e_input.pack(fill='x')
    main_frame.pack(fill='both')

    response.pack(anchor="w")

    lbl_time.pack(side="left")
    lbl_date.pack(side="right")
    lbl_theme.pack(anchor="center")
    footer.pack(fill="x", side="bottom")

    window.after(1000, hour)
    window.mainloop()


if __name__ == "__main__":
    launcher()
