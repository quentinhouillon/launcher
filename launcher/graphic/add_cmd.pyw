from tkinter import *
from tkinter import filedialog
from json import dump, load

def main_add():
    with open("../file/launcher.json", 'r') as file:
        launcher = load(file)

    with open("../file/settings.json", 'r') as settings:
        SETT = load(settings)
    
    def browse_file():
        try:
            file = filedialog.askopenfile(title='Choose a file')
            cmd_e.insert(INSERT, file.name)

        except:
            print(file.name)

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
                    if ("/" or ".com" or "www.") in get_cmd:
                        to_append = {
                            "app": get_app,
                            "lnk": get_lnk,
                            "cmd": get_cmd}
                    
                        with open("file\\launcher.json", 'w') as file:
                            launcher.append(to_append)
                            dump(launcher, file, indent=4)
                            window_add.destroy()
                    else:
                        to_append = {
                            "app": get_app,
                            "lnk": get_lnk,
                            "cmd": f"shortcuts\{get_cmd}.lnk"}
                    
                        with open("../file/launcher.json", 'w') as file:
                            launcher.append(to_append)
                            dump(launcher, file, indent=4)
                            window_add.destroy()
                else:
                    answer.config(text="complete cmd", bg=COLOR1, fg="red")
            else:
                answer.config(text="complete lnk", bg=COLOR1, fg="red")
        
        else:
            answer.config(text="complete app", bg=COLOR1, fg="red")

    # VARIABLE
    COLOR1 = SETT["my_theme"]["bg"]
    COLOR2 = SETT["my_theme"]["fg"]
    COLOR3 = SETT["my_theme"]["ft"]
    TF = SETT["my_theme"]["font"]

    window_add = Tk()
    app_text = StringVar()
    lnk_text = StringVar()
    cmd_text = StringVar()

    # WINDOW
    window_add.title("add - command")
    # window_add.geometry("300x100")
    window_add.resizable(False, False)
    window_add.iconbitmap("img\\launch.ico")
    window_add.configure(padx=10, pady=10, bg=COLOR1)
    window_add.focus_force()

    # LABEL
    app = Label(window_add, text="Nom de l'application ou site:", 
                bg=COLOR1, fg=COLOR2, font=TF, anchor="w")
    
    lnk = Label(window_add, text="\nNom du raccourcis que vous voulez:",
                bg=COLOR1, fg=COLOR2, font=TF, anchor="w")
    
    cmd = Label(window_add, text="\nURL ou chemin d'accès:", bg=COLOR1, 
                fg=COLOR2, font=TF, anchor="w")

    answer = Label(window_add, bg=COLOR1, anchor="w")

    # ENTRY
    app_e = Entry(window_add, bd=0, bg=COLOR3, fg=COLOR2,
                  insertbackground=COLOR2, textvariable=app_text, font=TF)

    lnk_e = Entry(window_add, bd=0, bg=COLOR3, fg=COLOR2,
                  insertbackground=COLOR2, textvariable=lnk_text, font=TF)

    cmd_e = Entry(window_add,bd=0, bg=COLOR3, fg=COLOR2,
                  insertbackground=COLOR2, textvariable=cmd_text, font=TF)

    app_e.focus()
    app_e.bind('<Return>', execute_app)
    lnk_e.bind('<Return>', execute_lnk)
    cmd_e.bind('<Return>', execute_cmd)

    # BUTTON
    browse = Button(window_add, text="parcourir", bg=COLOR3, fg=COLOR2,
                       font=TF, command=browse_file)

    # PACK
    app.pack(fill="x", anchor="w")
    app_e.pack(fill="x")

    lnk.pack(fill="x", anchor="w")
    lnk_e.pack(fill="x")

    cmd.pack(fill="x", anchor="w")
    cmd_e.pack(fill="x")

    answer.pack(fill="x", anchor="w")
    browse.pack(anchor="e")

    window_add.mainloop()
