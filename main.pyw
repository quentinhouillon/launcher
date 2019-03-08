from tkinter import *
from datetime import datetime
from time import strftime
from os import getcwd, chdir

from module.clss import *

chdir(getcwd())

window = Tk()

with open("file/theme.json", 'r') as th:
    data = load(th)

color = data["my_theme"]["bg"]
color2 = data["my_theme"]["fg"]
color3= data["my_theme"]["ft"]

font_type = "consolas"
var_entry = StringVar()
date = datetime.now()


def run(event):
    launch = Launcher(e_input.get(), response)
    launch.execute_app()
    e_input.delete(0, END)


def hour():
    lbl_time.config(text=strftime("current time: %H:%M:%S"))
    window.after(1000, hour)


# WINDOW
window.title("Launcher")
window.iconbitmap("img\\favicon.ico")
window.geometry("350x90-1007+647")
window.minsize(350, 90)
window.configure(bg=color, cursor="pirate")

# FRAME
main_frame = Frame(window, bg=color)
footer = Frame(window, bg=color3)

# LABEL
lab = Label(main_frame, text=".: LAUNCHER :.", bg=color, fg=color2,
            anchor="center", font=font_type)

prompt = Label(main_frame, text=">>", bg=color, fg=color2, font=font_type)
response = Label(window, bg=color, fg=color2, anchor="w", font=(font_type, 8))
lbl_time = Label(footer, text="current time: 00:00:00", bg=color3, fg=color2)
lbl_date = Label(footer, text=f"{date.year} - w4rmux", bg=color3, fg=color2)

# ENTRY
e_input = Entry(main_frame, bd=0, bg=color, fg=color2,
                insertbackground=color2, textvariable=var_entry, font=font_type)

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
footer.pack(fill="x", side="bottom")


if __name__ == "__main__":
    window.after(1000, hour)
    window.mainloop()
