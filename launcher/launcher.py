from datetime import datetime
from os import chdir, getcwd, startfile, system
from time import strftime
from tkinter import *
from json import load

from core.clss import *
from core.check_settings import *

class Launcher:
    def __init__(self, root):
        chdir(f"{getcwd()}/../launcher")

        self.root = root

        self.get_settings()

        WIDTH = 350
        HEIGHT = 120

        W_SCREEN = self.root.winfo_screenwidth()
        H_SCREEN = self.root.winfo_screenheight()

        W_CENTER = int(W_SCREEN-WIDTH-9)
        H_CENTER = int(H_SCREEN/2 + HEIGHT+110)

        self.var_entry = StringVar()
        self.date = datetime.now()

        # ROOT
        self.root.title("Launcher")
        self.root.iconbitmap("launch.ico")
        self.root.geometry(f"{WIDTH}x{HEIGHT}-{W_CENTER}+{H_CENTER}")
        self.root.minsize(WIDTH, HEIGHT)
        self.root.configure(bg=self.BG, padx=5, pady=5)
        self.root.focus_force()

        # FRAME
        self.frm_main = Frame(self.root, bg=self.BG)
        self.frm_footer = Frame(self.root, bg=self.BG)

        # IMAGE
        self.logo_theme = PhotoImage(file="img/theme.png")

        # LABEL
        self.lbl_title = Label(self.frm_main, text=".: launcher :.".upper(),
                               bg=self.BG, fg=self.FG, anchor="center",
                               font=self.TF, pady=8)

        self.lbl_resonse = Label(
            self.root, text="Si besoin, tapez 'help' ou 'about'",
            bg=self.BG, fg=self.FG, anchor="w", font=(self.TF, 8),
            pady=8)

        self.lbl_time = Label(self.frm_footer, text="time: 00:00:00", bg=self.FT,
                         fg=self.FG, font=(self.TF, 9))

        self.lbl_theme = Label(
            self.frm_footer, image=self.logo_theme, bg=self.BG,
            anchor="center")

        self.lbl_date = Label(
            self.frm_footer, text=self.date.year, bg=self.FT, fg=self.FG,
            font=(self.TF, 10))

        self.lbl_theme.bind("<Button-1>", self.change_theme)

        # ENTRY
        self.ent = Entry(self.frm_main, bd=0, bg=self.FT, fg=self.FG,
                        insertbackground=self.FG, textvariable=self.var_entry,
                        font=self.TF)

        self.ent.focus()
        self.ent.bind('<Return>', self.run)

        # PACK
        self.lbl_title.pack()
        self.ent.pack(fill='x')
        self.frm_main.pack(fill='both')

        self.lbl_resonse.pack(anchor="w")

        self.lbl_time.pack(side="left")
        self.lbl_date.pack(side="right")
        self.lbl_theme.pack(anchor="center")
        self.frm_footer.pack(fill="x", side="bottom")

        self.root.after(1000, self.hour)
        self.root.mainloop()

    def run(self, event):
        self.core = Core(self.ent.get())
        self.v_entry = self.ent.get()
        self.ent.delete(0, END)
        enter = self.core.execute_app()
        try:
            self.lbl_resonse.config(text=enter["text"], fg=enter["fg"])
            self.lbl_resonse.bind("<Button-1>", self.starter)

        except:
            pass

    def starter(self, event):
        if "not found" in self.lbl_resonse["text"]:
            if self.FG == "white":
                startfile(
                    f"https://www.qwant.com/?q={self.v_entry}&t=web&theme=1")

            else:
                startfile(f"https://www.qwant.com/?q={self.v_entry}&t=web")

    def change_theme(self, event):
        self.core = Core(self.ent.get())
        self.core.theme_change()
        self.root.destroy()
        main()

    def hour(self):
        try:
            self.lbl_time.config(text=strftime("time: %H:%M:%S"))
            self.root.after(1000, self.hour)

        except:
            self.lbl_time.config(text="time: 00:00:00")
            self.root.after(1000, self.hour)

    def get_settings(self):
        with open("../file/settings.json", 'r') as setttings:
            SETT = load(setttings)

        self.BG = SETT["my_theme"]["bg"]
        self.FG = SETT["my_theme"]["fg"]
        self.FT = SETT["my_theme"]["ft"]
        self.TF = SETT["my_theme"]["font"]

def main():
    root = Tk()
    checking()
    launch = Launcher(root)

if __name__ == "__main__":
    main()
