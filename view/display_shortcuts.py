from tkinter import Toplevel, Text, mainloop
from tkinter.messagebox import showinfo, showerror

from core.clss import DbLauncher


class DisplayShortcuts:
    def __init__(self, bg, fg, accent):
        self.BG = bg
        self.FG = fg
        self.ACCENT = accent

        self.db = DbLauncher()

    def window_display_shortcuts(self, event=False):
        # region: WINDOW
        self.tl_display = Toplevel(bg=self.BG)
        self.tl_display.title("Mes raccourcis")
        self.tl_display.iconbitmap("img/icon.ico")
        self.tl_display.geometry("850x600")
        self.tl_display.resizable(False, False)
        self.tl_display.focus_force()
        # endregion: WINDOW

        # region: TEXT
        self.txt_shortcuts = Text(self.tl_display, bg=self.BG, fg=self.FG,
                                  insertbackground=self.FG, bd=0)
        # endregion: TEXT

        # region: PACK
        self.txt_shortcuts.pack(fill="both")
        # endregion: PACK

    def display_shortcuts(self, event=False):
        if len(self.db.display_shortcuts()) != 0:
            self.window_display_shortcuts()

            for insert in self.db.display_shortcuts():
                insert_shortcuts = ("racourcis: ", insert[0], "\n")
                insert_opening = ("Commande d'ouverture: ", insert[1], "\n\n")

                for shortcuts in insert_shortcuts:
                    self.txt_shortcuts.insert("insert", shortcuts)

                for opening in insert_opening:
                    self.txt_shortcuts.insert("insert", opening)

            self.txt_shortcuts.config(state="disabled")
            self.tl_display.mainloop()

        else:
            showerror("Erreur",  "Vous n'avez aucun raccourci à afficher")
