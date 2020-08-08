from datetime import datetime
from json import dump, load
from os import getcwd, chdir, startfile
from tkinter import *
from tkinter.messagebox import showinfo, showerror

from core.check_settings import *
from core.clss import *
from view.add_window import *
from view.display_window import *
from view.update_delete_window import *


class Launcher:
    def __init__(self, root):
        chdir(getcwd())

        self.root = root

        self.ls_frm = []
        self.ls_frm_shortcuts = []
        self.ls_name_app = []
        self.ls_shortcuts = []
        self.ls_opening = []

        self.get_settings()
        self.date = datetime.now()

        self.core = LauncherCore()
        self.db = Database()
        self.window_add = WindowAdd(self.BG, self.FG, self.ACCENT)

        WIDTH = 650
        HEIGHT = 455

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
        self.root.bind("<Escape>", exit)
        self.root.bind("<Control-n>", self.window_add.window_add)
        self.root.bind("<Control-l>", self.display_shortcuts)
        self.root.bind("<Control-u>", self.window_update)
        self.root.bind("<Control-d>", self.window_delete)
        # endregion: ROOT

        # region: FRAME
        self.frm_entry = Frame(self.root, bg=self.BG, pady=12)
        self.frm_result = Frame(self.root, bg=self.ACCENT)
        # endregion: FRAME

        # region: CANVAS
        self.canvas = Canvas(self.frm_result, bg=self.ACCENT,
                             bd=0, highlightthickness=0)
        self.frm_canvas = Frame(self.canvas, bg=self.ACCENT)

        self.frm_canvas.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        # endregion: CANVAS

        # region: SCROLLBAR
        self.scrollbar = Scrollbar(
            self.frm_result, orient="vertical", command=self.canvas.yview, bg=self.BG)
        # endregion: SCROLLBAR

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

        self.lbl_add_shortcuts.bind("<ButtonRelease-1>", self.popup)
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

        # region: MENU
        self.menu_popup = Menu(self.root, tearoff=0, bg=self.BG, fg=self.FG)
        self.menu_popup.add_command(label="Ajouter un raccourci",
                                    accelerator="Ctrl-N",
                                    command=self.window_add.window_add)

        self.menu_popup.add_command(label="Afficher un raccourci",
                                    accelerator="Ctrl-L",
                                    command=self.display_shortcuts)

        self.menu_popup.add_command(label="Modifier un raccourci",
                                    accelerator="Ctrl-U",
                                    command=self.window_update)

        self.menu_popup.add_command(label="Supprimer un raccourci",
                                    accelerator="Ctrl-D",
                                    command=self.window_delete)
        # endregion: MENU

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.create_window((0, 0), window=self.frm_canvas, anchor="nw")

        # region: PACK
        self.lbl_search.pack(side="left", padx=10)
        self.lbl_add_shortcuts.pack(side="right", padx=10)
        self.ent.pack(fill="x", anchor="center")
        self.frm_entry.pack(fill="x", side="top", pady=10)

        self.frm_result.pack(fill="both")
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(fill="both")
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
        for index in range(len(self.ls_frm)):
            self.ls_frm[index].destroy()

        for index in range(len(self.ls_frm_shortcuts)):
            self.ls_frm_shortcuts[index].destroy()

        self.ls_frm.clear()
        self.ls_frm_shortcuts.clear()
        self.ls_name_app.clear()
        self.ls_shortcuts.clear()
        self.ls_opening.clear()

        apps = self.core.search(self.ent.get())[0]
        shortcuts = self.core.search(self.ent.get())[1]

        try:
            self.ls_shortcuts.append(shortcuts["shortcut"])
            self.ls_opening.append(shortcuts["opening"])

        except:
            pass

        for app in apps:
            if app.split("\\")[-1][:-4] not in self.ls_name_app:
                self.ls_name_app.append(app)

        self.img_icon = PhotoImage(file="img/shortcut.png")

        for index in range(len(self.ls_shortcuts)):
            self.ls_frm_shortcuts.append(Frame(self.frm_canvas, bg=self.BG,
                                               cursor="hand2"))

            self.lbl_icon = Label(self.ls_frm_shortcuts[index],
                                  image=self.img_icon,
                                  bg=self.BG, cursor="hand2")

            self.lbl_app = Label(self.ls_frm_shortcuts[index],
                                 text=self.ls_shortcuts[index],
                                 bg=self.BG, fg=self.FG, cursor="hand2",
                                 font=("monospace", 15))

            self.ls_frm_shortcuts[index].bind("<ButtonRelease-1>",
                                              lambda event, i=index:
                                              startfile(self.ls_opening[i]))

            self.lbl_icon.bind("<ButtonRelease-1>",
                               lambda event, i=index:
                               startfile(self.ls_opening[i]))

            self.lbl_app.bind("<ButtonRelease-1>",
                              lambda event, i=index:
                              startfile(self.ls_opening[i]))

            self.lbl_icon.pack(side="left", anchor="n", padx=5, pady=5)
            self.lbl_app.pack(side="left", anchor="n")
            self.ls_frm_shortcuts[index].pack(fill="x")

        for index in range(len(self.ls_name_app)):
            # image = self.core.get_icon(self.ls_name_app[index], "large")
            # image.convert("RGBA").save(f"img/app_icon.png")
            # self.img_app_icon = PhotoImage(file=f"img/appp_icon.png"

            self.ls_frm.append(Frame(self.frm_canvas, bg=self.BG,
                                     cursor="hand2"))

            self.lbl_icon_app = Label(self.ls_frm[index],
                                      image=self.img_icon,
                                      bg=self.BG, cursor="hand2")

            self.lbl_app = Label(self.ls_frm[index],
                                 text=self.ls_name_app[index].split(
                                     "\\")[-1][:-4],
                                 bg=self.BG, fg=self.FG, cursor="hand2",
                                 font=("monospace", 15), width=50)

            self.lbl_opening = Label(self.ls_frm[index], text="+",
                                     bg=self.BG, fg=self.FG, font=(
                                         "monospace", 23),
                                     cursor="hand2")

            self.ls_frm[index].bind("<ButtonRelease-1>",
                                    lambda event, i=index:
                                        startfile(self.ls_name_app[i]))

            self.lbl_icon_app.bind("<ButtonRelease-1>",
                                   lambda event, i=index:
                                   startfile(self.ls_name_app[i]))

            self.lbl_app.bind("<ButtonRelease-1>",
                              lambda event, i=index:
                              startfile(self.ls_name_app[i]))

            self.lbl_opening.bind("<ButtonRelease-1>",
                                  lambda event, i=index:
                                  self.window_add.window_add(self.ls_name_app[i]))

            self.lbl_icon_app.pack(side="left", anchor="n", padx=5, pady=5)
            self.lbl_app.pack(side="left", anchor="n", fill="x")
            self.lbl_opening.pack(side="right", anchor="n", padx=10)
            self.ls_frm[index].pack(fill="x")

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

    def display_shortcuts(self, event=False):
        if len(self.db.display_shortcuts()) != 0:
            self.window_display()

            for insert in self.db.display_shortcuts():
                insert_shortcuts = ("racourcis: ", insert[0], "\n")
                insert_opening = ("Commande d'ouverture: ", insert[1], "\n\n")

                for shortcuts in insert_shortcuts:
                    self.txt_shortcuts.insert(INSERT, shortcuts)

                for opening in insert_opening:
                    self.txt_shortcuts.insert(INSERT, opening)

            self.tl_display.mainloop()

        else:
            showerror("Erreur",  "Vous n'avez aucun raccourci à afficher")

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

    def popup(self, event):
        self.menu_popup.tk_popup(event.x_root, event.y_root, 0)


def main():
    check()
    root = Tk()
    launch = Launcher(root)
    root.mainloop()


if __name__ == "__main__":
    main()
