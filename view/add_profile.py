from tkinter import Label, Text, Frame, Tk, Button
from tkinter.messagebox import showinfo, showerror

from core.clss import DbProfile


class AddProfile:
    def __init__(self, bg, fg, accent):
        self.BG = bg
        self.FG = fg
        self.ACCENT = accent

        self.db = DbProfile()

    def window_add_profile(self):
        # region: WINDOW
        self.tl_add = Toplevel(bg=self.BG)
        self.tl_add.title("Ajouter un profile")
        self.tl_add.iconbitmap("img/icon.ico")
        self.tl_add.resizable(False, False)
        self.tl_add.focus_force()
        # endregion: WINDOW

        # region: LABEL
        self.lbl_profile = Label(self.tl_add,
                            text="Ajouter vos applications pour créer un profile",
                            bg=self.BG, fg=self.FG)
        # endregion: LABEL

        # region: TEXT
        self.txt_profile = Text(self.tl_add, bg=self.ACCENT, fg=self.FG,
                                bd=0, insertbackground=self.FG,
                                state="disabled")
        # endregion: TEXT

        # region: BUTTON
        self.btn_add = Button(self.tl_add, text="+ Ajouter", bg=self.ACCENT, 
                              fg=self.FG, relief="flat")
        self.btn_save = Button(self.tl_add, text="Enregistrer", bg=self.ACCENT,
                               fg=self.FG, relief="flat")
        self.btn_cancel = Button(self.tl_add, text="Annuler", bg=self.ACCENT,
                               fg=self.FG, relief="flat", command=self.tl_add.destroy)
        # endregion: BUTTON

        # region: PACK
        self.lbl_profile.pack(fill="x", padx=10, pady=10)
        self.txt_profile.pack(fill="x", padx=10)
        self.btn_add.pack(fill="x", padx=10, pady=10)
        self.btn_save.pack(side="right", anchor="s", padx=10, pady=10)
        self.btn_cancel.pack(side="right", anchor="s", padx=10, pady=10)
        # endregion: PACK

        self.tl_add.mainloop()
    
    def add_profile(self, name_profile, name_opening):
        list_profile = list()
        for add_shortcuts in self.db.display_profile():
            list_profile.append(add_shortcuts[0])

        if name_profile not in list_profile:
            ls_value = (name_profile, name_opening)
            self.db.add_profile(ls_value)
            showinfo("Ajout", "Votre profile a bien été ajouté")
            self.tl_add.destroy()

        else:
            showerror("Erreur", "Ce profile existe déjà")
            self.tl_add.destroy()
