from datetime import datetime
from json import dump, load
from os import getcwd, chdir, startfile
from tkinter import *

from core.check_settings import *
from core.clss import *

class Launcher:
    def __init__(self, root):
        chdir(getcwd())

        self.root = root
        self.ls_btn = []
        self.ls_value = []
        self.core = LauncherCore()
        
        self.get_settings()
        self.date = datetime.now()

        WIDTH = 650
        HEIGHT = 400

        W_SCREEN = self.root.winfo_screenwidth()
        H_SCREEN = self.root.winfo_screenheight()

        W_CENTER = int(W_SCREEN/2 - WIDTH/2)
        H_CENTER = int(H_SCREEN/2 - HEIGHT/2)

        self.program = "Launcher"
        self.author = "w4rmux"
        self.version = "1.0"
        self.license = f" © {self.date.year} {self.program}. \
Tous Droits Réservés"

        # region: ROOT
        self.root.geometry(f"{WIDTH}x{HEIGHT}+{W_CENTER}+{H_CENTER}")
        self.root.resizable(False, False)
        self.root.config(bg=self.ACCENT)
        self.root.overrideredirect(1)
        self.root.wm_attributes("-transparentcolor", self.ACCENT)
        self.root.focus_force()
        # endregion: ROOT

        # region: FRAME
        self.frm_entry = Frame(self.root, bg=self.BG, pady=16)
        self.frm_result = Frame(self.root, bg=self.ACCENT)
        # endregion: FRAME

        # region IMAGE
        self.img_search = PhotoImage(file="img/search.png")
        # endregion IMAGE

        # region: LABEL
        self.lbl_search = Label(self.frm_entry, image=self.img_search,
                                bg=self.BG, cursor="hand2")

        self.lbl_search.bind("<ButtonRelease-1>",
                             lambda x: self.core.execute(self.ent.get()))
        # endregion: LABEL

        # region: BUTTON
        self.btn_add_site = Button(self.root, text="+", bg=self.BG,
                                   fg=self.FG, relief="flat",
                                   font=("monospace", 23), cursor="hand2",
                                   command=self.add_site)
        # region: BUTTON

        # region: ENTRY
        self.ent = Entry(self.frm_entry, bg=self.BG, fg=self.FG, relief="flat",
                         justify="center", insertbackground=self.FG,
                         font=("sans-serif", 14))

        self.ent.bind("<KeyRelease>",
                      lambda x: self.create_button_search(self.ent.get()))
        self.ent.bind("<Return>", lambda x: self.core.execute(self.ent.get()))
        self.ent.focus()
        # endregion: ENTRY

        # region: PACK
        self.lbl_search.pack(side="left", padx=10)
        self.ent.pack(fill="x")
        self.btn_add_site.pack(side="right", anchor="n")
        self.frm_entry.pack(fill="x", side="top")

        self.frm_result.pack(fill="both", side="top")
        # endregion: PACK
    
    def get_settings(self):
        with open("file/config.json", "r") as config:
            self.CONFIG = load(config)
        
        with open("file/theme.json", "r") as theme:
            self.THEME = load(theme)
        
        # with open("file/language.json", "r") as language:
        #     self.LANGUAGE = load(language)
        
        self.MYTHEME = self.CONFIG["settings"]["theme"]
        # self.MYLANGUAGE = self.CONFIG["settings"]["language"]

        self.BG = self.THEME[self.MYTHEME]["bg"]
        self.FG = self.THEME[self.MYTHEME]["fg"]
        self.ACCENT = self.THEME[self.MYTHEME]["accent"]

    def create_button_search(self, value, event=False):
        for index in range(len(self.ls_value)):
            self.ls_btn[index].destroy()
        
        self.ls_value = []
        self.ls_btn = []

        for item in self.core.search(self.ent.get()):
            if item.split("\\")[-1][:-4] not in self.ls_value:
                self.ls_value.append(item)

        for index in range(len(self.ls_value)):
            self.ls_btn.append(Button(self.root,
                                text=self.ls_value[index].split("\\")[-1][:-4],
                                bg=self.BG, fg=self.FG, relief="flat",
                                font=("sans serif", 13), cursor="hand2",
                                command=lambda i=index: startfile(
                                    self.ls_value[i])))

            self.ls_btn[index].pack(fill="x")

    def add_site(self):
        print("add site")

def main():
    check()
    root = Tk()
    launch = Launcher(root)
    root.mainloop()
    print(launch.ls_value)

if __name__ == "__main__":
    main()
