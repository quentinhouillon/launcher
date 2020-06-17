import sqlite3
import os


class LauncherCore:
    def __init__(self):
        self.db = Database()

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


class Database:
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
