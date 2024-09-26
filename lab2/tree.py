from dataclasses import dataclass
from typing import Any
from collections import deque


class Node:
    def __init__(self, info=None, left=None, right=None):
        self.info: Any = info
        self.left: Any = left
        self.right: Any = right

    def __str__(self):
        return str(self.info)

    def __repr__(self):
        return repr(self.info)


class Tree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        if self.root is None:
            return ''
        stack = deque([(0, self.root)])
        blank = ' ┬├─┼╞╟┤╝╢╖╕╣╗╝╜╛┐└┴┬┬├─┼╞╟╚╔╩чЫ╦╠═╬╫╨╤╥╙╘╒╓'
        line = '─'
        mid = '├'
        end = '└'
        result = []
        while stack:
            depth, node = stack.pop()
            string = [' ' for _ in range(depth)]
            for d, _ in stack:
                if depth - 1 == d:
                    string[d] = '├'
                elif d < depth:
                    string[d] = '│'
            result.append(''.join(string) + node.info)
            if node.right is not None:
                stack.append((depth + 1, node.right))
            if node.left is not None:
                stack.append((depth + 1, node.left))
        return '\n'.join(result)
