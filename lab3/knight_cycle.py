"""
Блок 1:
Определить все возможные маршруты коня, начи-
нающиеся на одном заданном поле шахматной дос-
ки и оканчивающиеся на другом. Никакое поле не
должно встречаться в одном маршруте дважды.
"""

from tkinter import *
from tkinter.ttk import *
from consts import KNIGHT_TITLE


class MainWindow:
    def __init__(self):
        root = Tk()
        root.geometry('800x600')
        root.title(KNIGHT_TITLE)

        root.mainloop()


if __name__ == '__main__':
    MainWindow()
