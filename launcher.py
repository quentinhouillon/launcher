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
        self.root.overrideredirect(True)
        self.root.wm_attributes("-transparentcolor", self.ACCENT)
        self.root.focus_force()
        self.root.bind("<Control-w>", exit)
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
                                   command=self.window_add)
        # region: BUTTON

        # region: ENTRY
        self.ent = Entry(self.frm_entry, bg=self.BG, fg=self.FG, relief="flat",
                         justify="center", insertbackground=self.FG,
                         font=("sans-serif", 14))

        self.ent.bind("<KeyRelease>",
                      lambda x: self.create_button_search())
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

    def create_button_search(self, event=False):
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
    
    def window_add(self):
        # region: window
        self.tl_add = Toplevel(bg=self.BG)
        self.tl_add.title("Add Shortcuts")
        self.tl_add.iconbitmap("img/icon.ico")
        self.tl_add.geometry("450x200")
        self.tl_add.resizable(False, False)
        self.tl_add.focus_force()
        # endregion: window

        # region: ENTRY
        self.ent_app = Entry(self.tl_add, bg=self.ACCENT, fg=self.FG,
                             insertbackground=self.FG, bd=0)

        self.ent_shortcuts = Entry(self.tl_add, bg=self.ACCENT, fg=self.FG,
                                   insertbackground=self.FG, bd=0)

        self.ent_opening = Entry(self.tl_add, bg=self.ACCENT, fg=self.FG,
                                 insertbackground=self.FG, bd=0)


        self.ent_app.bind("<Return>", lambda event: self.ent_shortcuts.focus())
        self.ent_shortcuts.bind("<Return>", lambda event: self.ent_opening.focus())
        # self.ent_app.bind("<Return>", lambda event: self.ent_shortcuts.focus())
        # endregion: ENTRY

        # region: LABEL
        self.lbl_add = Label(self.tl_add, text="Enter app's name", bg=self.BG,
                             fg=self.FG, anchor="w")

        self.lbl_shortcuts = Label(self.tl_add, text="Enter shortcut's name",
                                   bg=self.BG, fg=self.FG, anchor="w")

        self.lbl_opening = Label(self.tl_add,
                                 text="Enter link's opening or URL",
                                 bg=self.BG, fg=self.FG, anchor="w")
        # endregion: LABEL

        # region: PACK
        self.lbl_add.pack(anchor="w", fill="x", padx=10, pady=5)
        self.ent_app.pack(anchor="w", fill="x", padx=10, pady=5)

        self.lbl_shortcuts.pack(anchor="w", fill="x", padx=10, pady=5)
        self.ent_shortcuts.pack(anchor="w", fill="x", padx=10, pady=5)

        self.lbl_opening.pack(anchor="w", fill="x", padx=10, pady=5)
        self.ent_opening.pack(anchor="w", fill="x", padx=10, pady=5)
        # endregion: PACK

        self.tl_add.mainloop()

def main():
    check()
    root = Tk()
    launch = Launcher(root)
    root.mainloop()

if __name__ == "__main__":
    main()
