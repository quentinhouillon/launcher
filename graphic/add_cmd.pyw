from tkinter import *
from json import dump, load

def main_add():
    with open("file\\run.json", 'r') as file:
        run = load(file)

    with open("file\\theme.json", 'r') as theme:
        th = load(theme)

    def execute_app(event):
        lnk_e.focus()

    def execute_lnk(event):
        cmd_e.focus()

    def execute_cmd(event):
        get_app = app_e.get()
        get_lnk = lnk_e.get()
        get_cmd = cmd_e.get()

        if get_app:
            if get_lnk:
                if get_cmd:
                    to_append = {
                        "app": get_app,
                        "lnk": get_lnk,
                        "cmd": get_cmd}
                
                    with open("file\\run.json", 'w') as file:
                        run.append(to_append)
                        dump(run, file, indent=4)
                        exit()
                else:
                    answer.config(text="complete cmd", bg=color1, fg="red")
            else:
                answer.config(text="complete lnk", bg=color1, fg="red")
        
        else:
            answer.config(text="complete app", bg=color1, fg="red")

    # VARIABLE
    color1 = th["my_theme"]["bg"]
    color2 = th["my_theme"]["fg"]
    color3 = th["my_theme"]["ft"]
    tf = "consolas"

    window_add = Tk()
    app_text = StringVar()
    lnk_text = StringVar()
    cmd_text = StringVar()

    # WINDOW
    window_add.title("add - command")
    # window_add.geometry("300x100")
    window_add.resizable(False, False)
    window_add.iconbitmap("img\\launch.ico")
    window_add.configure(cursor="pirate", bg=color1)

    # LABEL
    app = Label(window_add, text="nom de l'application ou du site: ", 
                bg=color1, fg=color2, font=tf, anchor="w")
    
    lnk = Label(window_add, text="nom du raccourcis: ", bg=color1, 
                fg=color2, font=tf, anchor="w")
    
    cmd = Label(window_add, text="chemin d'accès ou url: ", bg=color1, 
                fg=color2, font=tf, anchor="w")

    answer = Label(window_add, bg=color1, anchor="w")

    # ENTRY
    app_e = Entry(window_add, bd=0, bg=color1, fg=color2,
                  insertbackground=color2, textvariable=app_text, font=tf)

    lnk_e = Entry(window_add, bd=0, bg=color1, fg=color2,
                  insertbackground=color2, textvariable=lnk_text, font=tf)

    cmd_e = Entry(window_add,bd=0, bg=color1, fg=color2,
                  insertbackground=color2, textvariable=cmd_text, font=tf)

    app_e.focus()
    app_e.bind('<Return>', execute_app)
    lnk_e.bind('<Return>', execute_lnk)
    cmd_e.bind('<Return>', execute_cmd)

    # PACK
    app.pack(fill="x", anchor="w")
    app_e.pack(fill="x")

    lnk.pack(fill="x", anchor="w")
    lnk_e.pack(fill="x")

    cmd.pack(fill="x", anchor="w")
    cmd_e.pack(fill="x")

    answer.pack(fill="x", anchor="w")

    window_add.mainloop()
