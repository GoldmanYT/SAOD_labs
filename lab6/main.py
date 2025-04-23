from tkinter import *
from tkinter.ttk import *
from graph import *


class Window:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('800x600')

        self.notebook = Notebook()
        self.notebook.pack(expand=True, fill=BOTH)

        self.frame_graph = Frame(self.notebook)
        self.frame_algorithms = Frame(self.notebook)

        self.frame_graph.pack()
        self.frame_algorithms.pack()

        self.notebook.add(self.frame_graph, text='Представления')
        self.notebook.add(self.frame_algorithms, text='Алгоритмы')

        label_adj_struct = Label(
            master=self.frame_graph,
            text='Структура смежности'
        )
        label_adj_struct.pack()

        adjacency_structure = {
            'a': ['b', 'e', 'f'],
            'b': ['c'],
            'c': [],
            'd': ['c', 'g'],
            'e': ['d', 'f'],
            'f': ['d', 'g'],
            'g': ['c']
        }

        self.adj_struct_table = Treeview(
            master=self.frame_graph,
            columns=('0', '1'),
            show='headings'
        )
        self.adj_struct_table.pack(expand=True, fill=BOTH)
        for i, column in enumerate(('Вершина', 'Список рёбер')):
            self.adj_struct_table.heading(
                str(i), text=column
            )
        for _ in range(10):
            self.adj_struct_table.insert(
                '', END, values=[]
            )
        self.set_adj_struct(adjacency_structure)

        label_inc_matrix = Label(
            master=self.frame_graph,
            text='Матрица инциденций'
        )
        label_inc_matrix.pack()

        inc_matrix = get_incident_matrix_from_adjacency_structure(adjacency_structure)
        values = inc_matrix.values()
        edges = tuple(values.__iter__().__next__().keys())

        self.inc_matrix_table = Treeview(
            master=self.frame_graph,
            columns=list(str(i) for i in range(len(edges) + 1)),
            show='headings'
        )
        self.inc_matrix_table.pack(expand=True, fill=BOTH)
        self.inc_matrix_table.heading(
            '0', text='Вершина'
        )
        for i, (v1, v2) in enumerate(edges, start=1):
            self.inc_matrix_table.heading(
                str(i), text=f'({v1}, {v2})'
            )
            self.inc_matrix_table.column(
                str(i), width=10
            )
        for _ in range(10):
            self.inc_matrix_table.insert(
                '', END, values=[]
            )
        self.set_inc_matrix(inc_matrix)

        self.transform_button = Button(
            master=self.frame_graph,
            text='Переход',
            command=self.set_inc_matrix
        )
        self.transform_button.pack()

        self.root.mainloop()

    def set_adj_struct(
            self,
            adj_struct: dict[str, list[str]]
    ):
        for i, (vertex, vertices) in enumerate(adj_struct.items()):
            self.adj_struct_table.insert(
                '', i, values=[vertex, ','.join(vertices)]
            )

    def set_inc_matrix(
            self,
            inc_matrix: dict[str, dict[tuple[str, str], int]]
    ):
        for i, (vertex, incidents) in enumerate(inc_matrix.items()):
            values = [vertex] + list(incidents.values())
            self.inc_matrix_table.insert(
                '', i, values=values
            )


if __name__ == '__main__':
    window = Window()
