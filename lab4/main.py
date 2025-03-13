from tkinter import *
from tkinter import ttk
from methods import *
from random import randrange, shuffle


class Window:
    column_count = 5
    experiment_count = 1000
    step = 20000

    def __init__(self):
        self.root = Tk()
        self.root.geometry('1280x720')

        methods = [
            # LinearSearch,
            BinarySearch,
            HomogeneousBinarySearch,
            InterpolationSearch,
            BinaryTree,
            AVLTree,
            DigitSearch,
            HashTableSearch,
        ]

        columns = [str(i) for i in range(self.column_count + 1)]

        self.table = ttk.Treeview(self.root, columns=columns, show='headings', height=20)
        self.table.pack()

        self.table.heading('0', text='Метод')
        for i in range(1, self.column_count + 1):
            self.table.heading(str(i), text=f'n = {i * self.step}')

        for method_class in methods:
            compare_count_row = [method_class.name + '\t\tЧС']
            time_row = ['\t\t\tВРМ']
            rotation_row = ['\t\t\tВРЩ']
            for i in range(1, len(columns)):
                n = self.step * i
                array = [i for i in range(2, 2 * n + 1, 2)]
                method = method_class(n=n, array=array)
                if method.type == TREE:
                    temp_array = array[:]
                    shuffle(temp_array)
                    for value in temp_array:
                        method.insert(value)

                for k in range(self.experiment_count * 2):
                    if k < self.experiment_count:
                        value = randrange(2, 2 * n + 1, 2)
                    else:
                        value = randrange(1, 2 * n + 2, 2)
                    if method.type == ARRAY:
                        method.search(array, value)
                    elif method.type == TREE:
                        method.search(value)

                compare_count = method.get_compare_count()
                time = method.get_time()
                compare_count_row.append('\t\t'.join(str(v) for v in compare_count.values()))
                time_row.append('\t\t'.join(str(v) for v in time.values()))

                if isinstance(method, AVLTree):
                    rotation_count = method.get_rotation_count()
                    rotation_row.append('\t\t'.join(str(v) for v in rotation_count.values()))

            self.table.insert('', END, values=compare_count_row)
            self.table.insert('', END, values=time_row)

            if len(rotation_row) > 1:
                self.table.insert('', END, values=rotation_row)

        self.root.mainloop()


if __name__ == '__main__':
    window = Window()
