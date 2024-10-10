class Node:
    def __init__(self, info=None, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right
        self.depth = 0

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
        stack = [(0, self.root)]
        blank = ' '
        vert = '│'
        line = '─'
        mid = '├'
        end = '└'
        result = []
        visited = []
        while stack:
            depth, node = stack.pop()
            node.depth = depth
            s = [blank for _ in range(depth)]
            for d, n in visited:
                if d < depth:
                    s[d] = vert
            for d, n in visited:
                if node is n.left and n.right is not None:
                    s[d] = mid
                elif node is n.left or node is n.right:
                    s[d] = end
            for d, n in set(visited):
                if node is n.left and n.right is None or node is n.right:
                    visited.remove((d, n))
            s += node.info
            if node.right is not None:
                stack.append((depth + 1, node.right))
            if node.left is not None:
                stack.append((depth + 1, node.left))
            result.append(''.join(s))
            visited.append((depth, node))
        return '\n'.join(result)
