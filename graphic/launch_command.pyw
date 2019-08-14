from tkinter import *
from json import load
from datetime import datetime
from graphic.add_cmd import *
from graphic.show_cmd import *

def cmd_main():
    # FILE
    with open("file\\theme.json", "r") as theme:
        th = load(theme)
        
    with open("file\\run.json", 'r') as file:
        run = load(file)
            
    # VARIABLE
    color1 = th["my_theme"]["bg"]
    color2 = th["my_theme"]["fg"]
    color3 = th["my_theme"]["ft"]
    
    tf = "consolas"
    date = datetime.now()
    
    window_cmd = Tk()
    var_text = StringVar()


    # CALLBACK
    def _run_cmd(file):
        from os import startfile; startfile(file)
        window_cmd.destroy()


    def _condition_cmd(event):
        if cmd.get() == "show":
            main_show()
        
        elif cmd.get() == "add":
            main_add()
        
        else:
            error.config(text=f"error {cmd.get()}")


    # WINDOW
    window_cmd.title("list - cmd")
    window_cmd.iconbitmap("img\\launch.ico")
    window_cmd.configure(bg=color1)

    # FRAME
    main_cmd = Frame(window_cmd, bg=color1)
    footer_cmd = Frame(window_cmd, bg=color3)

    # LABEL
    lbl = Label(main_cmd, text="add or show", bg=color1, fg=color2, font=tf)
    prompt = Label(main_cmd, text=">>", bg=color1, fg=color2, font=tf,
                anchor="w")

    error = Label(window_cmd, bg=color1, fg="red", font=tf)

    time = Label(footer_cmd, text=f"w4rmux - {date.year}", bg=color3,
                fg=color2, font=tf)

    # ENTRY
    cmd = Entry(main_cmd, bg=color1, fg=color2, font=tf, bd=0,
                textvariable=var_text, insertbackground=color2)

    cmd.focus()
    cmd.bind("<Return>", _condition_cmd)

    # PACK
    lbl.pack(fill="x")
    prompt.pack(side="left")
    cmd.pack(fill="x")
    main_cmd.pack(fill="x")

    error.pack(fill="x", anchor="w")

    time.pack(side="right", fill="x")
    footer_cmd.pack(fill="x", side="bottom")

    window_cmd.mainloop()
