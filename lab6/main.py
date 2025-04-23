from tkinter import *
from tkinter.ttk import *


class Window:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('800x600')

        self.button = Button(text='Button')
        self.button.pack()

        self.root.mainloop()


if __name__ == '__main__':
    window = Window()
