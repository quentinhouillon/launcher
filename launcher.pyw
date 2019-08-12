from datetime import datetime
from os import chdir, getcwd, startfile
from time import strftime
from tkinter import *

from core.clss import *

chdir(getcwd())

# CALLBACK
def run(event):
    launch = Launcher(e_input.get())
    enter = launch.execute_app()
    response.config(text=enter["text"], fg=enter["fg"])
    e_input.delete(0, END)


def change_theme(event):
    launch = Launcher(e_input.get())
    launch.theme_change()
    window.destroy()

    try:
        startfile("launcher.pyw")
    
    except:
        startfile("launcher.exe")


def hour():
    lbl_time.config(text=strftime("current time: %H:%M:%S"))
    window.after(1000, hour)


# FILE
with open("file\\theme.json", 'r') as theme:
    th = load(theme)

# VARIABLE
window = Tk()

color1 = th["my_theme"]["bg"]
color2 = th["my_theme"]["fg"]
color3 = th["my_theme"]["ft"]
    
font_type = "consolas"
var_entry = StringVar()
date = datetime.now()


# WINDOW
window.title("Launcher")
window.iconbitmap("img\\launch.ico")
window.geometry("350x90-1007+647")
window.minsize(350, 90)
window.configure(bg=color1, cursor="pirate")

# FRAME
main_frame = Frame(window, bg=color1)
footer = Frame(window, bg=color3)

# IMAGE
logo_theme = PhotoImage(file="img\\theme.png")

# LABEL
lab = Label(main_frame, text=".: LAUNCHER :.", bg=color1, fg=color2,
            anchor="center", font=font_type)

prompt = Label(main_frame, text=">>", bg=color1, fg=color2, font=font_type)
response = Label(window, text="if you need you can enter 'help'", bg=color1, 
                fg="blue", anchor="w", font=(font_type, 8))

lbl_time = Label(footer, text="current time: 00:00:00", bg=color3,
                    fg=color2)

lbl_theme = Label(footer, image=logo_theme, bg=color3, anchor="e")
lbl_theme.bind("<Button-1>", change_theme)
lbl_date = Label(footer, text=f"{date.year} - w4rmux", bg=color3, fg=color2)

# ENTRY
e_input = Entry(main_frame, bd=0, bg=color1, fg=color2,
                insertbackground=color2, textvariable=var_entry,
                font=font_type)

e_input.focus()
e_input.bind('<Return>', run)

# PACK
lab.pack(fill='x')
prompt.pack(side="left")
e_input.pack(fill='x')
main_frame.pack(fill='both')

response.pack(fill="x")

lbl_time.pack(side="left")
lbl_date.pack(side="right")
lbl_theme.pack(fill="x", side="right", padx="55")
footer.pack(fill="x", side="bottom")


if __name__ == "__main__":
    window.after(1000, hour)
    window.mainloop()
