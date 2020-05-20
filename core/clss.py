import sqlite3
import os

class LauncherCore:
    def __init__(self):
        self.conn = sqlite3.connect("file/Launcher.db")
        self.cur = self.conn.cursor()
    
    def list_disrectory(self, path):
        file = []
        for root, dirs, files in os.walk(path):
            for i in files:
                file.append(os.path.join(root, i))
        return file

    def search_app_data(self):
        self.ls_app_data = self.list_disrectory(
            os.environ["AppData"] + r"\Microsoft\Windows\Start Menu\Programs")
        return self.ls_app_data

    def search_program_data(self):
        self.ls_program_data = self.list_disrectory(
            r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs")
        return self.ls_program_data

    def listing_app(self):
        self.ls_apps= []
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

        if len(value) <= 2:
            pass

        else:
            for i in self.listing_app():
                if value in i[0]:
                    cmd = i[1]
                    result.append(cmd)
        return result

    def execute(self, value):
        print(value)
