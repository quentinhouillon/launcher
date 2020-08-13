import win32gui
import win32ui
import win32con
import win32api
from PIL import Image, ImageTk
from win32com.shell import shell, shellcon
import sqlite3
import os


class LauncherCore:
    def __init__(self):
        self.db = DbLauncher()

    def list_directory(self, path):
        file = []
        for root, dirs, files in os.walk(path):
            for i in files:
                file.append(os.path.join(root, i))
        return file

    def search_app_data(self):
        self.ls_app_data = self.list_directory(
            os.environ["AppData"] + r"\Microsoft\Windows\Start Menu\Programs")
        return self.ls_app_data

    def search_program_data(self):
        self.ls_program_data = self.list_directory(
            r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs")
        return self.ls_program_data

    def listing_app(self):
        self.ls_apps = []
        for i in self.search_app_data():
            files = i.split("\\")[-1]
            if ".ini" not in files:
                self.ls_apps.append((files[:-4].lower(), i))

        for i in self.search_program_data():
            files = i.split("\\")[-1]
            if ".ini" not in files:
                self.ls_apps.append((files[:-4].lower(), i))
        return self.ls_apps

    def search(self, value):
        cmd = ''
        result = []
        shortcut = {}

        db_shortcut = self.db.get_shortcuts(value)

        if len(value) <= 1:
            pass

        else:
            for i in self.listing_app():
                if value.lower() in i[0]:
                    cmd = i[1]
                    result.append(cmd)

            for index in db_shortcut:
                if index != 0:
                    shortcut["shortcut"] = index[0]
                    shortcut["opening"] = index[1]

        return (result, shortcut)

    def execute(self, value):
        try:
            os.startfile(self.search(value)[1]["opening"])

        except:
            os.startfile(self.search(value)[0][0])

    def get_icon(self, PATH, size="large"):
        SHGFI_ICON = 0x000000100
        SHGFI_ICONLOCATION = 0x000001000
        if size == "small":
            SHIL_SIZE = 0x00001
        elif size == "large":
            SHIL_SIZE = 0x00002
        else:
            raise TypeError(
                "Invalid argument for 'size'. Must be equal to 'small' or 'large'")

        ret, info = shell.SHGetFileInfo(
            PATH, 0, SHGFI_ICONLOCATION | SHGFI_ICON | SHIL_SIZE)
        hIcon, iIcon, dwAttr, name, typeName = info
        ico_x = win32api.GetSystemMetrics(win32con.SM_CXICON)
        hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
        hbmp = win32ui.CreateBitmap()
        hbmp.CreateCompatibleBitmap(hdc, ico_x, ico_x)
        hdc = hdc.CreateCompatibleDC()
        hdc.SelectObject(hbmp)
        hdc.DrawIcon((0, 0), hIcon)
        win32gui.DestroyIcon(hIcon)

        bmpinfo = hbmp.GetInfo()
        bmpstr = hbmp.GetBitmapBits(True)
        img = Image.frombuffer(
            "RGBA",
            (bmpinfo["bmWidth"], bmpinfo["bmHeight"]),
            bmpstr, "raw", "BGRA", 0, 1
        )

        if size == "small":
            img = img.resize((16, 16), Image.ANTIALIAS)
        return img


class DbLauncher:
    def add_shortcuts(self, ls_values):
        self.conn = sqlite3.connect("file/Launcher.db")
        self.cur = self.conn.cursor()

        self.cur.execute("INSERT INTO Launcher VALUES (NULL, ?, ?)", ls_values)
        self.conn.commit()

        self.conn.close()

    def display_shortcuts(self):
        self.conn = sqlite3.connect("file/Launcher.db")
        self.cur = self.conn.cursor()

        self.cur.execute("SELECT shortcut, opening FROM Launcher")

        to_return = self.cur.fetchall()
        self.conn.close()

        return to_return

    def delete_shortcuts(self, name_shortcuts):
        self.conn = sqlite3.connect("file/Launcher.db")
        self.cur = self.conn.cursor()

        self.cur.execute("DELETE FROM Launcher WHERE shortcut=?",
                         (name_shortcuts,))

        self.conn.commit()
        self.conn.close()

    def update_shortcuts(self, ls_values):
        self.conn = sqlite3.connect("file/Launcher.db")
        self.cur = self.conn.cursor()

        self.cur.execute(
            "UPDATE Launcher SET shortcut=?, opening=? WHERE shortcut=?",
            ls_values)

        self.conn.commit()
        self.conn.close()

    def get_shortcuts(self, name_shortcuts):
        self.conn = sqlite3.connect("file/Launcher.db")
        self.cur = self.conn.cursor()

        self.cur.execute(
            "SELECT Shortcut, opening FROM Launcher WHERE shortcut=?",
            (name_shortcuts,))

        to_return = self.cur.fetchall()
        self.conn.close()

        return to_return

class DbProfile:
    def add_profile(self, ls_values):
        self.conn = sqlite3.connect("file/Launcher.db")
        self.cur = self.conn.cursor()

        self.cur.execute("INSERT INTO Launcher VALUES (NULL, ?, ?)", ls_values)
        self.conn.commit()

        self.conn.close()

    def display_profile(self):
        self.conn = sqlite3.connect("file/Launcher.db")
        self.cur = self.conn.cursor()

        self.cur.execute("SELECT shortcut, profile FROM Launcher")

        to_return = self.cur.fetchall()
        self.conn.close()

        return to_return

    def delete_profile(self, name_profile):
        self.conn = sqlite3.connect("file/Launcher.db")
        self.cur = self.conn.cursor()

        self.cur.execute("DELETE FROM Launcher WHERE shortcut=?",
                         (name_profile,))

        self.conn.commit()
        self.conn.close()

    def update_profile(self, ls_values):
        self.conn = sqlite3.connect("file/Launcher.db")
        self.cur = self.conn.cursor()

        self.cur.execute(
            "UPDATE Launcher SET shortcut=?, profile=? WHERE shortcut=?",
            ls_values)

        self.conn.commit()
        self.conn.close()

    def get_profile(self, name_profile):
        self.conn = sqlite3.connect("file/Launcher.db")
        self.cur = self.conn.cursor()

        self.cur.execute(
            "SELECT Shortcut, profile FROM Launcher WHERE shortcut=?",
            (name_profile,))

        to_return = self.cur.fetchall()
        self.conn.close()

        return to_return
