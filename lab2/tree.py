from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    id: int
    value: Any = None
    left: Any = None
    right: Any = None
    parent: Any = None


class Tree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        res = []
        node = self.root
        stack = [None]
        while node is not None:
            res.append(f'{node.id}: {node.left.id} {node.right.id}')
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                node = node.left
            else:
                node = stack.pop()
        return '\n'.join(res)
