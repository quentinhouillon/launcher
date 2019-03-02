import time
from datetime import datetime
from tkinter import *

from module.clss import *

COLOR = "black"
COLOR2 = "#1e272e"
FONT = 'Consolas'
window = Tk()
date =  datetime.now()
launch = Launcher()

var_text = StringVar()

def callback(event):
    response.config(text=f'run {input_usr.get()}')
    launch.execute_app(input_usr.get())
    input_usr.delete(0, END)


# function which changes time on Label
def update_time():
    # change text on Label
    lbl_time['text'] = time.strftime('Current time: %H:%M:%S')

    # run `update_time` again after 1000ms (1s)
    window.after(1000, update_time)  # function name without ()


content = Frame(window, bg=COLOR)
title = Label(content, text='.: Launcher :.',
              bg=COLOR,
              fg='white',
              font=(FONT, 16),
              anchor='center')
title.pack(fill='x')

frm_form = Frame(content, bg=COLOR)
prompt = Label(frm_form, text='>>',
               bg=COLOR,
               fg='white',
               font=(FONT, 8),
               anchor='w')
prompt.pack(side=LEFT)

input_usr = Entry(frm_form,
                  bg=COLOR,
                  textvariable=var_text,
                  font=(FONT, 10),
                  fg='white',
                  relief='solid',
                  bd=0,
                  insertbackground='white')
input_usr.pack(fill='x')
input_usr.bind('<Return>', callback)
input_usr.focus()
frm_form.pack(fill='x')

response = Label(window,
                  bg=COLOR,
                  fg="white",
                  font=(FONT, 10, 'italic'), 
                  anchor="w")

content.pack(fill='both')
response.pack(fill="x")

footer = Frame(window, bg=COLOR2)
lbl_time = Label(footer, text='Current time: 00:00:00',
                 bg=COLOR2,
                 fg='white',
                 font=(FONT, 8))
lbl_time.pack(side=LEFT)

copyright = Label(footer, text=f'{date.year} - W4rmux ',
                  fg="white",
                  bg=COLOR2,
                  font=(FONT, 8, 'italic'))
copyright.pack(side=RIGHT)
footer.pack(fill='x', side=BOTTOM)


if __name__ == "__main__":
    window.title('Launcher W4rmux (o_O)')
    window.geometry('350x90')
    window.minsize(350, 90)
    window.iconbitmap("img/favicon.ico")
    window.config(bg=COLOR, cursor='pirate')
    window.after(1000, update_time)
    window.mainloop()
