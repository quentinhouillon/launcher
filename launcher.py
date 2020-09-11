# from datetime import datetime
from json import load
from os import chdir, getcwd, path, startfile
from tkinter import (Canvas, Entry, Frame, Label, Menu, PhotoImage, Scrollbar,
                     Tk)

from PIL import ImageTk

from core.check_settings import check
from core.clss import LauncherCore
from view.add_profiles import AddProfiles
from view.add_shortcuts import AddShortcuts
from view.display_shortcuts import DisplayShortcuts
from view.update_delete_shortcuts import UpdateDeleteShortcuts


class Launcher:
    def __init__(self, root):
        chdir(getcwd())

        self.root = root

        # lists
        self.ls_frm = []
        self.ls_frm_shortcuts = []
        self.ls_name_app = []
        self.ls_shortcuts = []
        self.ls_opening = []
        self.app_icon = {}

        # constants
        WIDTH = 650
        HEIGHT = 455

        W_SCREEN = self.root.winfo_screenwidth()
        H_SCREEN = self.root.winfo_screenheight()

        W_CENTER = int(W_SCREEN/2 - WIDTH/2)
        H_CENTER = int(H_SCREEN/2 - HEIGHT/2)

        # date = datetime.now()
        # PROGRAM = "Launcher"
        # AUTHOR = "w4rmux"
        # VERSION = "1.0"
        # LICENSE = f" © {date.year} {PROGRAM}.Tous Droits Réservés"

        self.get_settings()

        self.core = LauncherCore()
        self.add_shortcuts = AddShortcuts(self.BG, self.FG, self.ACCENT)
        self.display_shortcuts = DisplayShortcuts(
            self.BG, self.FG, self.ACCENT)
        self.update_delete_shortcuts = UpdateDeleteShortcuts(
            self.BG, self.FG, self.ACCENT)
        self.add_profiles = AddProfiles(self.BG, self.FG, self.ACCENT)

        self.root.geometry(f"{WIDTH}x{HEIGHT}+{W_CENTER}+{H_CENTER}")
        self.root.resizable(False, False)
        self.root.config(bg=self.ACCENT)
        self.root.overrideredirect(True)
        self.root.wm_attributes("-transparentcolor", self.ACCENT)
        self.root.focus_force()

        # bindings
        self.root.bind("<Escape>", exit)
        self.root.bind("<Control-n>", self.add_shortcuts.window_add_shortcuts)
        self.root.bind(
            "<Control-l>", self.display_shortcuts.display_shortcuts)
        self.root.bind(
            "<Control-u>",
            self.update_delete_shortcuts.window_update_shortcuts)
        self.root.bind(
            "<Control-d>",
            self.update_delete_shortcuts.window_delete_shortcuts)
        self.root.bind("<Alt-n>", self.add_profiles.window_add_profiles)
        # self.root.bind(
        #     "<Alt-l>", self.display_profiles.display_profiles)
        # self.root.bind(
        #     "<Alt-u>", self.update_delete_profiles.window_update_profiles)
        # self.root.bind(
        #     "<Alt-d>", self.update_delete_profiles.window_delete_profiles)

        self.frm_entry = Frame(self.root, bg=self.BG, pady=12)
        self.frm_result = Frame(self.root, bg=self.ACCENT)

        self.canvas = Canvas(self.frm_result, bg=self.ACCENT,
                             bd=0, highlightthickness=0)
        self.frm_canvas = Frame(self.canvas, bg=self.ACCENT)

        self.frm_canvas.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.canvas.bind("<Configure>", self.on_configure)
        self._unbound_to_mousewheel(event=None)

        self.scrollbar = Scrollbar(
            self.frm_result, orient="vertical", command=self.canvas.yview,
            bg=self.BG)

        self.img_search = PhotoImage(file="img/search.png")

        self.lbl_search = Label(self.frm_entry, image=self.img_search,
                                bg=self.BG, cursor="hand2")

        self.lbl_search.bind("<ButtonRelease-1>",
                             lambda x: self.core.execute(self.ent.get()))

        self.lbl_add_shortcuts = Label(self.frm_entry, text="+", bg=self.BG,
                                       fg=self.FG, relief="flat",
                                       font=("monospace", 23), cursor="hand2")

        self.lbl_add_shortcuts.bind("<ButtonRelease-1>", self.popup)

        self.ent = Entry(self.frm_entry, bg=self.BG, fg=self.FG, relief="flat",
                         justify="center", insertbackground=self.FG,
                         font=("sans-serif", 14))

        self.ent.bind("<KeyRelease>",
                      lambda x: self.create_frame_search())

        self.ent.bind("<Return>", lambda x: self.core.execute(self.ent.get()))
        self.ent.focus()

        self.menu_popup = Menu(self.root, tearoff=0, bg=self.BG, fg=self.FG)
        self.menu_popup.add_command(
            label="Ajouter un raccourci",
            accelerator="Ctrl-N",
            command=self.add_shortcuts.window_add_shortcuts)

        self.menu_popup.add_command(
            label="Afficher un raccourci",
            accelerator="Ctrl-L",
            command=self.display_shortcuts.display_shortcuts)

        self.menu_popup.add_command(
            label="Modifier un raccourci",
            accelerator="Ctrl-U",
            command=self.update_delete_shortcuts.window_update_shortcuts)

        self.menu_popup.add_command(
            label="Supprimer un raccourci",
            accelerator="Ctrl-D",
            command=self.update_delete_shortcuts.window_delete_shortcuts)

        self.menu_popup.add_command(
            label="Ajouter un profiles",
            accelerator="Alt-N",
            command=self.add_profiles.window_add_profiles)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.create_window((0, 0), window=self.frm_canvas, anchor="nw")

        self.lbl_search.pack(side="left", padx=10)
        self.lbl_add_shortcuts.pack(side="right", padx=10)
        self.ent.pack(fill="x", anchor="center")
        self.frm_entry.pack(fill="x", side="top", pady=10)

        self.frm_result.pack(fill="both", expand=True)
        self.canvas.pack(fill="both", expand=True, side="left")

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

        except KeyError:
            pass

        for app in apps:
            if path.splitext(path.basename(app))[0] not in self.ls_name_app:
                self.ls_name_app.append(app)

        self.img_icon = PhotoImage(file="img/shortcut.png")

        if len(self.ls_name_app) + len(self.ls_shortcuts) > 8:
            self.scrollbar.pack(side="right", fill="y")
            self.frm_canvas.bind('<Enter>', self._bound_to_mousewheel)
            self.frm_canvas.bind('<Leave>', self._unbound_to_mousewheel)

        else:
            self.scrollbar.pack_forget()
            self.frm_canvas.bind('<Enter>', self._unbound_to_mousewheel)

        for index in range(len(self.ls_shortcuts)):
            self.ls_frm_shortcuts.append(Frame(self.frm_canvas, bg=self.BG,
                                               cursor="hand2"))

            self.lbl_icon = Label(self.ls_frm_shortcuts[index],
                                  image=self.img_icon,
                                  bg=self.BG, cursor="hand2")

            self.lbl_app = Label(self.ls_frm_shortcuts[index],
                                 text=self.ls_shortcuts[index],
                                 bg=self.BG, fg=self.FG, cursor="hand2",
                                 font=("monospace", 15), width=50)

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
            image = self.core.get_icon(self.ls_name_app[index], "large")
            self.app_icon[index] = ImageTk.PhotoImage(image)

            self.ls_frm.append(Frame(self.frm_canvas, bg=self.BG,
                                     cursor="hand2"))

            self.lbl_icon_app = Label(self.ls_frm[index],
                                      image=self.app_icon[index],
                                      bg=self.BG, cursor="hand2")

            self.lbl_app = Label(self.ls_frm[index],
                                 text=path.splitext(
                                     path.basename(
                                         self.ls_name_app[index]))[0],
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

            self.lbl_opening.bind(
                "<ButtonRelease-1>",
                lambda event, i=index:
                self.add_shortcuts.window_add_shortcuts(self.ls_name_app[i]))

            self.lbl_icon_app.pack(side="left", anchor="n", padx=5, pady=5)
            self.lbl_app.pack(side="left", anchor="n", fill="x")
            self.lbl_opening.pack(side="right", anchor="n", padx=10)
            self.ls_frm[index].pack(fill="x")

    def popup(self, event):
        self.menu_popup.tk_popup(event.x_root, event.y_root, 0)

    def on_configure(self, event):
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.create_window(
            (0, 0), width=event.width, window=self.frm_canvas, anchor="nw")

    def _on_mousewheel(self, event):
        """Add scroll mousewheel for canvas."""
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _bound_to_mousewheel(self, event):
        """Apply scroll with mousewheel of canvas."""
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbound_to_mousewheel(self, event):
        """Remove scroll with mousewheel of canvas."""
        self.canvas.unbind_all("<MouseWheel>")


def main():
    check()
    root = Tk()
    Launcher(root)
    root.mainloop()


if __name__ == "__main__":
    main()
