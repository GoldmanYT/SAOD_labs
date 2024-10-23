from tkinter import *
from tkinter.ttk import *
from tree import Tree, Node
from random import randint


class MainWindow:
    def __init__(self):
        root = Tk()
        root.geometry('800x600')

        self.tree_view = Treeview(
            root,
            show='tree'
        )
        self.tree_view.place(
            relx=0.05,
            rely=0.05,
            relwidth=0.9,
            relheight=0.75
        )

        button_generate = Button(
            root,
            text='Сгенерировать дерево',
            command=self.generate_tree
        )
        button_generate.place(
            relx=0.05,
            rely=0.8,
            relwidth=0.9,
            relheight=0.05
        )

        Label(
            root,
            text='Элемент:'
        ).place(
            relx=0.05,
            rely=0.85,
            relwidth=0.45,
            relheight=0.05
        )

        self.string_element = StringVar()
        self.string_element.trace('w', self.compute_count)
        entry_element = Entry(
            root,
            textvariable=self.string_element,
        )
        entry_element.place(
            relx=0.05,
            rely=0.9,
            relwidth=0.45,
            relheight=0.05
        )

        Label(
            root,
            text='Число вхождений:'
        ).place(
            relx=0.5,
            rely=0.85,
            relwidth=0.45,
            relheight=0.05
        )

        self.string_result = StringVar()
        entry_result = Entry(
            root,
            textvariable=self.string_result,
            state="readonly"
        )
        entry_result.place(
            relx=0.5,
            rely=0.9,
            relwidth=0.45,
            relheight=0.05
        )

        self.tree = Tree()
        self.generate_tree()

        root.mainloop()

    def generate_tree(self):
        self.tree.root = Node(0, get_value())
        n = 10
        for i in range(1, n + 1):
            value = get_value()
            node = self.tree.root
            placed = False
            while not placed:
                if value <= node.value:
                    if node.left is None:
                        node.left = Node(i, value, parent=node.id)
                        placed = True
                    else:
                        node = node.left
                else:
                    if node.right is None:
                        node.right = Node(i, value, parent=node.id)
                        placed = True
                    else:
                        node = node.right
        self.show_tree()

    def show_tree(self):
        node = self.tree.root
        stack = [None]
        self.tree_view.delete(*self.tree_view.get_children())

        while node is not None:
            self.tree_view.insert(
                parent='' if node is self.tree.root else node.parent,
                index=END,
                iid=node.id,
                text=node.value,
                open=True
            )
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                node = node.left
            else:
                node = stack.pop()

    def compute_count(self, *_):
        count = 0
        node = self.tree.root
        stack = [None]
        value = self.string_element.get()

        while node is not None:
            if node.value == value:
                count += 1

            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                node = node.left
            else:
                node = stack.pop()

        self.string_result.set(count)


def get_value():
    return str(randint(0, 9))


if __name__ == '__main__':
    MainWindow()
