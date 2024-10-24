"""
Блок 2:
Найти все простые несократимые дроби, заключен-
ные между 0 и 1, знаменатели которых не превы-
шают 9 (дробь задается двумя натуральными числами -
числителем и знаменателем).
"""

from tkinter import *
from tkinter.ttk import *
from consts import FRACTIONS_TITLE

MAX_N = 10


class MainWindow:
    def __init__(self):
        root = Tk()
        root.geometry('800x600')
        root.title(FRACTIONS_TITLE)

        Label(
            root,
            text='Ответ:'
        ).pack(anchor='nw')

        self.string_ans = StringVar()
        ans = Label(
            root,
            textvariable=self.string_ans
        )
        ans.pack(anchor='nw')

        self.solve()

        root.mainloop()

    def solve(self):
        numerator0 = 1
        denominator0 = 2
        is_fraction = [[True] * MAX_N for _ in range(MAX_N)]

        for numerator in range(numerator0, MAX_N):
            for denominator in range(denominator0, MAX_N):
                if is_fraction[numerator][denominator]:
                    for numerator2 in range(denominator, MAX_N):
                        is_fraction[numerator2][denominator] = False
                    for k in range(2, MAX_N // denominator):
                        is_fraction[numerator * k][denominator * k] = False

        ans = []
        for numerator in range(numerator0, MAX_N):
            for denominator in range(denominator0, MAX_N):
                if is_fraction[numerator][denominator]:
                    ans.append(f'{numerator}/{denominator}')

        self.string_ans.set(', '.join(ans))


if __name__ == '__main__':
    MainWindow()
