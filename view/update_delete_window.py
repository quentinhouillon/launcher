from tkinter import *
from tkinter.messagebox import showinfo, showerror

from core.clss import Database

class WindowUpdateDelete:
    def __init__(self, bg, fg, accent):
        self.BG = bg
        self.FG = fg
        self.ACCENT = accent

        self.db = Database()

    def window_update_delete(self, function, event=False):
        # region: WINDOW
        self.tl_update_delete = Toplevel(bg=self.BG)
        self.tl_update_delete.title("Choisis un raccourci")
        self.tl_update_delete.geometry("250x100")
        self.tl_update_delete.resizable(False, False)
        self.tl_update_delete.focus_force()
        # endregion: WINDOW

        # region: FRAME
        self.frm_choose = Frame(self.tl_update_delete, bg=self.BG)
        self.frm_update = Frame(self.tl_update_delete, bg=self.BG)
        # endregion: FRAME

        # region: LABEL
        self.lbl_update_shortcut = Label(self.frm_update,
                                         text="Entrer un nouveau raccourci",
                                         bg=self.BG, fg=self.FG)

        self.lbl_update_opening = Label(self.frm_update,
                                        text="Entrer une nouvelle URL \
ou un nouveau chemin d'accès",
                                        bg=self.BG, fg=self.FG)

        self.lbl_instruction = Label(self.frm_update,
                                     text="Si aucune modification n'est \
inscrite, l'ancien nom sera conservé",
                                     bg=self.BG, fg="green",
                                     font=("monospace", 8), anchor="w")

        self.lbl_choose = Label(self.frm_choose,
                                text="Entrer le nom d'un raccourci",
                                bg=self.BG, fg=self.FG, anchor="center")
        # endregion: LABEL

        # region: ENTRY
        self.ent_update_shortcut = Entry(self.frm_update, bg=self.ACCENT,
                                         fg=self.FG, bd=0, insertbackground=self.FG,
                                         justify="center")

        self.ent_update_opening = Entry(self.frm_update, bg=self.ACCENT,
                                        fg=self.FG, bd=0, insertbackground=self.FG,
                                        justify="center")

        self.ent_choose = Entry(self.frm_choose, bg=self.ACCENT,
                                fg=self.FG, bd=0, insertbackground=self.FG,
                                justify="center")

        self.ent_choose.bind("<Return>", function)
        self.ent_update_shortcut.bind("<Return>",
                                      lambda event: self.ent_update_opening.focus())

        self.ent_update_opening.bind("<Return>", self.update_shortcuts)
        self.ent_choose.focus()
        # endregion: ENTRY

        # region: PACK
        self.lbl_choose.pack(fill="x", padx=10, pady=10)
        self.ent_choose.pack(fill="x", padx=10, pady=10)
        self.frm_choose.pack(fill="x")

        self.lbl_update_shortcut.pack(fill="x", pady=10)
        self.ent_update_shortcut.pack(fill="x", pady=10)

        self.lbl_update_opening.pack(fill="x", pady=10)
        self.ent_update_opening.pack(fill="x", pady=10)

        self.lbl_instruction.pack(side="bottom")
        # endregion: PACK

        self.tl_update_delete.mainloop()

    def window_update(self, event=False):
        self.window_update_delete(self.update_window_shortcuts)

    def update_window_shortcuts(self, event=False):
        self.result_get = self.db.get_shortcuts(self.ent_choose.get())
        if len(self.result_get) != 0:
            self.frm_choose.pack_forget()
            self.tl_update_delete.geometry("400x190")
            self.frm_update.pack()
            self.ent_update_shortcut.focus()

        else:
            showerror("Erreur", "Ce raccourci n'existe pas")
            self.tl_update_delete.focus_force()
            self.ent_choose.focus()

    def update_shortcuts(self, event=False):
        ls_value = []

        if len(self.ent_update_shortcut.get()) != 0:
            ls_value.append(self.ent_update_shortcut.get())

        else:
            for index in self.result_get:
                ls_value.append(index[0])

        if len(self.ent_update_opening.get()) != 0:
            ls_value.append(self.ent_update_opening.get())

        else:
            for index in self.result_get:
                ls_value.append(index[1])

        for index in self.result_get:
            ls_value.append(index[0])

        self.db.update_shortcuts(ls_value)
        showinfo("Mise à jour", "Votre raccourci a bien été mis à jour")
        self.tl_update_delete.destroy()

    def window_delete(self, event=False):
        self.window_update_delete(self.delete_shortcuts)

    def delete_shortcuts(self, event=False):
        self.result_get = self.db.get_shortcuts(self.ent_choose.get())

        if len(self.result_get) != 0:
            self.db.delete_shortcuts(self.ent_choose.get())
            showinfo("Suppression", "Votre raccourci a bien été supprimé")
            self.tl_update_delete.destroy()

        else:
            showerror("Erreur", "Ce raccourci n'existe pas")
            self.tl_update_delete.focus_force()
            self.ent_choose.focus()