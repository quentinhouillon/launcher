import sqlite3
from datetime import datetime
from json import dump, load
from os import getcwd, chdir
from tkinter import *

from core.check_settings import *
from core.clss import *

class Launcher:
    def __init__(self, root):
        chdir(getcwd())

        self.root = root

        self.conn = sqlite3.connect("file/Launcher.db")
        self.cur = self.conn.cursor()
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
        self.frm_entry = Frame(self.root, bg=self.BG, pady=15)
        self.frm_result = Frame(self.root, bg=self.ACCENT)
        # endregion: FRAME

        # region: ENTRY
        self.ent = Entry(self.frm_entry, bg=self.BG, fg=self.FG, relief="flat",
                         justify="center", insertbackground=self.FG)

        self.ent.bind("<Return>", lambda x: self.execute(self.ent.get()))
        self.ent.focus()
        # endregion: ENTRY

        # region: PACK
        self.ent.pack(fill="x")
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

    def execute(self, value, event=False):
        print(value)

def main():
    check()
    root = Tk()
    launch = Launcher(root)
    root.mainloop()

if __name__ == "__main__":
    main()
