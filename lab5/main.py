from tkinter import *
from tkinter import ttk
from methods import *
from math import ceil
from datetime import datetime as dt


class Window:
    column_count = 5
    experiment_count = 10
    step = 2000

    def __init__(self):
        self.root = Tk()
        self.root.geometry('1280x720')

        start_time = dt.now()

        columns = [str(i) for i in range(self.column_count + 1)]

        self.table = ttk.Treeview(self.root, columns=columns, show='headings', height=20)
        self.table.pack()

        self.table.heading('0', text='Метод')
        for i in range(1, self.column_count + 1):
            self.table.heading(str(i), text=f'n = {i * self.step}')

        table_data = [['Нет данных' for _ in range(self.column_count + 1)]
                      for _ in range(len(list_of_methods))]
        for i, name in enumerate(list_of_names):
            table_data[i][0] = name
        for i in range(1, self.column_count + 1):
            n = self.step * i
            array = methods.create_array(n)
            copy = methods.create_copy(n, array)
            results = [Result(0, 0) for _ in range(len(list_of_methods))]
            for k in range(self.experiment_count):
                methods.randomize_array(n, array)
                methods.copy_array(n, array, copy)
                for j, method in enumerate(list_of_methods):
                    if method == methods.quick_sort:
                        method(n, array, results[j], 0, n - 1)
                    else:
                        method(n, array, results[j])
                    methods.copy_array(n, copy, array)
            methods.delete_array(copy)
            methods.delete_array(array)
            for j in range(len(list_of_methods)):
                compares, swaps = results[j].compares, results[j].swaps
                if ceil(compares / self.experiment_count) >= 1e7:
                    sep = '\t'
                else:
                    sep = '\t\t'
                table_data[j][i] = sep.join(str(ceil(value / self.experiment_count))
                                            for value in (compares, swaps))

        for row in table_data:
            self.table.insert('', END, values=row)

        end_time = dt.now()
        print(end_time - start_time)

        self.root.mainloop()


if __name__ == '__main__':
    window = Window()
