from tkinter import *
from tkinter import ttk
from methods import *
from random import randrange


class Window:
    column_count = 5
    experiment_count = 1000
    step = 20000

    def __init__(self):
        self.root = Tk()
        self.root.geometry('1280x720')

        array_methods = [LinearSearch(), BinarySearch()]

        columns = [str(i) for i in range(self.column_count + 1)]

        self.table = ttk.Treeview(self.root, columns=columns, show='headings')
        self.table.pack()

        self.table.heading('0', text='Метод')
        for i in range(1, self.column_count + 1):
            self.table.heading(str(i), text=f'n = {i * self.step}')

        for method in array_methods:
            row = [method.name]
            for i in range(1, len(columns)):
                n = 2 * self.step
                array = [i for i in range(2, 2 * n + 1, 2)]
                for k in range(self.experiment_count):
                    value = randrange(2 - (k < self.experiment_count // 2), 2 * n + 1, 2)
                    method.search(array, value)
                result = method.get_result()
                row.append('\t'.join(str(v) for v in result.values()))

            self.table.insert('', END, values=row)

        self.root.mainloop()


if __name__ == '__main__':
    window = Window()
