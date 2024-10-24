"""
Блок 1:
Определить все возможные маршруты коня, начи-
нающиеся на одном заданном поле шахматной дос-
ки и оканчивающиеся на другом. Никакое поле не
должно встречаться в одном маршруте дважды.

Блок 2:
Найти все простые несократимые дроби, заключен-
ные между 0 и 1, знаменатели которых не превы-
шают 9 (дробь задается двумя натуральными числами -
числителем и знаменателем).

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
from knight_cycle import MainWindow as KnightWindow
from simple_fractions import MainWindow as FractionsWindow
from orders import MainWindow as OrdersWindow
from consts import *


class MainWindow:
    windows = {
        KNIGHT_TITLE: KnightWindow,
        FRACTIONS_TITLE: FractionsWindow,
        ORDERS_TITLE: OrdersWindow
    }

    def __init__(self):
        root = Tk()
        root.geometry('800x600')
        root.title('Лабораторная работа 3')

        Label(
            root,
            text='Выберите блок:'
        ).pack()

        self.string_combobox = StringVar()
        combobox = Combobox(
            root,
            state='readonly',
            values=list(self.windows.keys()),
            textvariable=self.string_combobox
        )
        combobox.pack()

        button = Button(
            root,
            text='Перейти',
            command=self.launch
        )
        button.pack()

        root.mainloop()

    def launch(self):
        window = self.windows.get(self.string_combobox.get())
        if window is not None:
            window()


if __name__ == '__main__':
    MainWindow()
