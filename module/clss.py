from os import system, chdir, getcwd, startfile
from json import load, dump

class Launcher:
    def __init__(self, command):
        self.command = command
        self.text = ""
        self.color = ""
        chdir(getcwd())

    def execute_app(self):
        with open("file/run.json", 'r') as js:
            self.data = load(js)

        for i in self.data:
            if self.command == i["lnk"] or self.command == i["app"]:
                app = i["app"]
                try:
                    startfile(i["cmd"])
                    self.text = f"run {app}"
                    self.color = "green"

                except:
                    self.text = f"error {app}"
                    self.color = "red"

                break

            elif self.command == "exit":
                exit()
            
            elif self.command == "shutdown":
                system("shutdown -p")
            
            elif self.command == "restart":
                system("shutdown -r")
            
            else:
                self.text = f"not found {self.command}"
                self.color = "orange"

        return {"text": self.text,
                "fg": self.color}
