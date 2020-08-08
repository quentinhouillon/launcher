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
        self.window_display = WindowDisplay(self.BG, self.FG, self.ACCENT)
        self.window_update_delete = WindowUpdateDelete(
            self.BG, self.FG, self.ACCENT)

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
        self.root.bind("<Control-l>", self.window_display.display_shortcuts)
        self.root.bind("<Control-u>", self.window_update_delete.window_update)
        self.root.bind("<Control-d>", self.window_update_delete.window_delete)
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
            self.frm_result, orient="vertical", command=self.canvas.yview,
            bg=self.BG)
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
                                    command=self.window_display.display_shortcuts)

        self.menu_popup.add_command(label="Modifier un raccourci",
                                    accelerator="Ctrl-U",
                                    command=self.window_update_delete.window_update)

        self.menu_popup.add_command(label="Supprimer un raccourci",
                                    accelerator="Ctrl-D",
                                    command=self.window_update_delete.window_delete)
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

    def popup(self, event):
        self.menu_popup.tk_popup(event.x_root, event.y_root, 0)


def main():
    check()
    root = Tk()
    launch = Launcher(root)
    root.mainloop()


if __name__ == "__main__":
    main()
