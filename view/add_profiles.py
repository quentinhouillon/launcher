from tkinter import Button, Entry, Frame, Label, Text, Tk, Toplevel
from tkinter.filedialog import askopenfilenames
from tkinter.messagebox import showerror, showinfo

from core.clss import DbProfile


class AddProfiles:
    def __init__(self, bg, fg, accent):
        self.BG = bg
        self.FG = fg
        self.ACCENT = accent

        self.db = DbProfile()

    def window_add_profiles(self, event=False):
        # region: WINDOW
        self.tl_add = Toplevel(bg=self.BG)
        self.tl_add.title("Ajouter un profile")
        self.tl_add.iconbitmap("img/icon.ico")
        self.tl_add.focus_force()
        # endregion: WINDOW

        # region: FRAME
        self.frm_main = Frame(self.tl_add, bg=self.BG)
        self.frm_entry = Frame(self.tl_add, bg=self.BG)
        self.frm_footer = Frame(self.tl_add, bg=self.BG)
        # endregion: FRAME

        # region: LABEL
        self.lbl_profile = Label(self.tl_add,
                                 text="Ajouter vos applications pour créer un profile",
                                 bg=self.BG, fg=self.FG)
        self.lbl_name_profile = Label(self.frm_entry,
                                      text="Entrer le non du profile",
                                      bg=self.BG, fg=self.FG)
        # endregion: LABEL

        # region: ENTRY
        self.ent_profile_name = Entry(self.frm_entry, bg=self.ACCENT,
                                      insertbackground=self.FG,
                                      fg=self.FG, bd=0)
        # endregion: ENTRY

        # region: TEXT
        self.txt_profile = Text(self.frm_main, bg=self.ACCENT, fg=self.FG,
                                bd=0, insertbackground=self.FG,
                                state="disabled")
        # endregion: TEXT

        # region: BUTTON
        self.btn_add = Button(self.frm_main, text="+ Ajouter", bg=self.ACCENT,
                              fg=self.FG, relief="flat", command=self.openfile)
        self.btn_save = Button(self.frm_footer, text="Enregistrer", bg=self.ACCENT,
                               fg=self.FG, relief="flat",
                               command=lambda: self.add_profiles(
                                   self.ent_profile_name.get(),
                                   self.txt_profile.get(0.1, "end")))
        self.btn_cancel = Button(self.frm_footer, text="Annuler", bg=self.ACCENT,
                                 fg=self.FG, relief="flat", command=self.tl_add.destroy)
        # endregion: BUTTON

        # region: PACK
        self.lbl_profile.pack(fill="x", padx=10, pady=10, side="top")

        self.lbl_name_profile.pack(fill="x", side="left", anchor="n")
        self.ent_profile_name.pack(fill="x", expand="true", padx=10)
        self.frm_entry.pack(fill="x", expand="true", side="top",
                            padx=10, pady=10)

        self.btn_save.pack(side="right", anchor="s", padx=10, pady=10)
        self.btn_cancel.pack(side="right", anchor="s", padx=10, pady=10)
        self.frm_footer.pack(side="bottom", fill="x")

        self.txt_profile.pack(fill="x", padx=10, expand="true")
        self.btn_add.pack(fill="x", padx=10, pady=10, expand="true")
        self.frm_main.pack(fill="x", expand="true", side="bottom", anchor="w")
        # endregion: PACK

        self.tl_add.mainloop()

    def add_profiles(self, name_profile, name_opening):
        list_profile = list()
        for add_shortcuts in self.db.display_profiles():
            list_profile.append(add_shortcuts[0])

        if name_profile not in list_profile:
            ls_value = (name_profile, name_opening)
            self.db.add_profiles(ls_value)
            showinfo("Ajout", "Votre profile a bien été ajouté")
            self.tl_add.destroy()

        else:
            showerror("Erreur", "Ce profile existe déjà")
            self.tl_add.destroy()

    def openfile(self):
        open_file = askopenfilenames()
        self.txt_profile.config(state="normal")

        for of in open_file:
            self.txt_profile.insert("insert", f"{of}\n")

        self.txt_profile.config(state="disabled")
