from json import dump, load
from os import startfile, system


class Launcher:
    def __init__(self, command):
        self.command = command
        self.text = ""
        self.color = ""

    def execute_app(self):
        with open("file\\run.json", 'r') as js:
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

    def theme_change(self):
        with open("file\\theme.json", 'r') as th:
            self.theme = load(th)

        for i in self.theme["bg_theme"]:
            if self.theme["my_theme"]["bg"] == self.theme["bg_theme"]["black"]:
                self.theme["my_theme"]["bg"] = self.theme["bg_theme"]["white"]
                self.theme["my_theme"]["fg"] = self.theme["fg_theme"]["black"]
                self.theme["my_theme"]["ft"] = self.theme["bg_theme"]["ft_white"]
    
            else:
                self.theme["my_theme"]["bg"] = self.theme["bg_theme"]["black"]
                self.theme["my_theme"]["fg"] = self.theme["fg_theme"]["white"]
                self.theme["my_theme"]["ft"] = self.theme["bg_theme"]["ft_black"]
            
            break
    
        with open("file/theme.json", 'w') as save:
            dump(self.theme, save, indent=4)

