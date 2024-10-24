"""
Блок 3:
Имеется конечное множество заказов, каждый из ко-
торых требует ровно одну единицу времени для сво-
его выполнения. Для каждого заказа известны срок
выполнения и штраф за невыполнение к сроку. Требу-
ется найти порядок выполнения заказов, при котором
сумма штрафов будет наименьшей.
"""

from tkinter import *
from tkinter.ttk import *
from consts import ORDERS_TITLE


class MainWindow:
    def __init__(self):
        root = Tk()
        root.geometry('800x600')
        root.title(ORDERS_TITLE)

        root.mainloop()


if __name__ == '__main__':
    MainWindow()
