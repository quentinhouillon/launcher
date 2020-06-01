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

        self.ls_frm = []
        self.ls_value = []

        self.core = LauncherCore()
        self.db = Database()
        
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
        self.license = f" © {self.date.year} {self.program}.\
Tous Droits Réservés"

        # region: ROOT
        self.root.geometry(f"{WIDTH}x{HEIGHT}+{W_CENTER}+{H_CENTER}")
        self.root.resizable(False, False)
        self.root.config(bg=self.ACCENT)
        self.root.overrideredirect(True)
        self.root.wm_attributes("-transparentcolor", self.ACCENT)
        self.root.focus_force()
        self.root.bind("<Control-w>", exit)
        # endregion: ROOT

        # region: FRAME
        self.frm_entry = Frame(self.root, bg=self.BG, pady=12)
        # endregion: FRAME

        # region IMAGE
        self.img_search = PhotoImage(file="img/search.png")
        # endregion IMAGE

        # region: LABEL
        self.lbl_search = Label(self.frm_entry, image=self.img_search,
                                bg=self.BG, cursor="hand2")

        self.lbl_search.bind("<ButtonRelease-1>",
                             lambda x: self.core.execute(self.ent.get()))
        
        self.lbl_add_shortcuts = Label(self.frm_entry, text="+", bg=self.BG,
                                   fg=self.FG, relief="flat",
                                   font=("monospace", 23), cursor="hand2")
       
        self.lbl_add_shortcuts.bind("<ButtonRelease-1>", self.window_add)
        # endregion: LABEL

        # region: ENTRY
        self.ent = Entry(self.frm_entry, bg=self.BG, fg=self.FG, relief="flat",
                         justify="center", insertbackground=self.FG,
                         font=("sans-serif", 14))

        self.ent.bind("<KeyRelease>",
                      lambda x: self.create_frame_search())

        self.ent.bind("<Return>", lambda x: self.core.execute(self.ent.get()))
        self.ent.focus()
        # endregion: ENTRY

        # region: PACK
        self.lbl_search.pack(side="left", padx=10)
        self.lbl_add_shortcuts.pack(side="right", padx=10)
        self.ent.pack(fill="x", anchor="center")
        self.frm_entry.pack(fill="x", side="top", pady=10)
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

    def create_frame_search(self, event=False):
        for index in range(len(self.ls_value)):
            self.ls_frm[index].destroy()
        
        self.ls_frm = []
        self.ls_value = []

        for item in self.core.search(self.ent.get()):
            if item.split("\\")[-1][:-4] not in self.ls_value:
                self.ls_value.append(item)

        for index in range(len(self.ls_value)):
            self.ls_frm.append(Frame(self.root, bg=self.BG, cursor="hand2"))
            
            self.lbl_app = Label(self.ls_frm[index],
                                   text=self.ls_value[index].split("\\")[-1][:-4],
                                   bg=self.BG, fg=self.FG, cursor="hand2",
                                   font=("monospace", 15))

            self.lbl_opening = Label(self.ls_frm[index], text="+",
                                   bg=self.BG, fg=self.FG,font=("monospace", 23),
                                   cursor="hand2")

            self.ls_frm[index].bind("<ButtonRelease-1>",
                                    lambda event, i=index:
                                        startfile(self.ls_value[i]))
            
            self.lbl_app.bind("<ButtonRelease-1>",
                                 lambda event, i=index:
                                    startfile(self.ls_value[i]))

            self.lbl_opening.bind("<ButtonRelease-1>",
                                             lambda event, i=index:
                                             self.window_add(self.ls_value[i]))

            self.lbl_app.pack(side="left", anchor="n")
            self.lbl_opening.pack(side="right", anchor="n", padx=10)
            self.ls_frm[index].pack(fill="x")
    
    def window_add(self, name_opening=False, event=False):
        # region: WINDOW
        self.tl_add = Toplevel(bg=self.BG)
        self.tl_add.title("Ajouter un raccourcis")
        self.tl_add.iconbitmap("img/icon.ico")
        self.tl_add.geometry("360x150")
        self.tl_add.resizable(False, False)
        self.tl_add.focus_force()
        # endregion: WINDOW

        # region: ENTRY
        self.ent_shortcuts = Entry(self.tl_add, bg=self.ACCENT, fg=self.FG,
                                   insertbackground=self.FG, bd=0)

        self.ent_opening = Entry(self.tl_add, bg=self.ACCENT, fg=self.FG,
                                 insertbackground=self.FG, bd=0)


        self.ent_shortcuts.bind("<Return>", lambda event: self.ent_opening.focus())
        self.ent_opening.bind("<Return>", lambda event: self.add_shortcuts(
            self.ent_shortcuts.get(), self.ent_opening.get()))
        # endregion: ENTRY

        # region: LABEL
        self.lbl_shortcuts = Label(self.tl_add,
                                   text="Entrer le nom du raccourcis",
                                   bg=self.BG, fg=self.FG, anchor="w")

        self.lbl_opening = Label(self.tl_add,
                                 text="Entrer le chemin d'accès du fichier ou \
l'url du site internet",
                                 bg=self.BG, fg=self.FG, anchor="w")
        # endregion: LABEL

        # region: PACK
        self.lbl_shortcuts.pack(anchor="w", fill="x", padx=10, pady=5)
        self.ent_shortcuts.pack(anchor="w", fill="x", padx=10, pady=5)

        self.lbl_opening.pack(anchor="w", fill="x", padx=10, pady=5)
        self.ent_opening.pack(anchor="w", fill="x", padx=10, pady=5)
        # endregion: PACK

        self.autocompletion_window_app(name_opening)
        self.tl_add.mainloop()

    def autocompletion_window_app(self, name_opening=False):
        try:
            if len(name_opening) >= 1:
                self.ent_opening.insert(INSERT, name_opening)
                self.ent_shortcuts.focus()
        
        except:
            self.ent_shortcuts.focus()
    
    def add_shortcuts(self, name_shortcuts, name_opening):
        ls_value = (name_shortcuts, name_opening)
        self.db.add_shortcuts(ls_value)
        self.tl_add.destroy()
    
    def window_display(self, event=False):
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

        self.display_shortcuts()
        self.tl_display.mainloop()

    def display_shortcuts(self):
        for insert in self.db.display_shortcuts():
            insert_shortcuts = ("racourcis: ", insert[0], "\n")
            insert_opening = ("Commande d'ouverture: ", insert[1], "\n\n")

            for shortcuts in insert_shortcuts:
                self.txt_shortcuts.insert(INSERT, shortcuts)

            for opening in insert_opening:
                self.txt_shortcuts.insert(INSERT, opening)

    def update_shortcuts(self, name_shortcuts):
        pass

    def delete_shortcuts(self, name_shortcuts):
        pass

def main():
    check()
    root = Tk()
    launch = Launcher(root)
    root.mainloop()

if __name__ == "__main__":
    main()
