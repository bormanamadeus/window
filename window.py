#! /usr/bin/python3

from tkinter import *
from dialogTable import *
from quitter import *

def Main():
    topic = Toplevel()

    widget = Button(text='Spam', padx=10, pady=10)
    widget.pack(padx=20, pady=20)
    widget.config(cursor='gumby')
    widget.config(bd=8, relief=RAISED)
    widget.config(bg='dark green', fg='white')
    widget.config(font=('helvetics', 20, 'underline italic'))

    Demo(topic)

    mainloop()


class Demo(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        Label(self, text="Basic demos").pack()

        for key in demos:
            func = (lambda key=key: self.printit(key))
            Button(self, text=key, command=func).pack(side=TOP, fill=BOTH)
        Quitter(self).pack(side=TOP, fill=BOTH)

    def printit(self, name):
        print(name, 'returns =>', demos[name]())


if __name__ == '__main__':
   Main() 
