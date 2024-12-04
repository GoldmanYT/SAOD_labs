"""
Блок 1:
Определить все возможные маршруты коня, начинающиеся
на одном заданном поле шахматной доски и оканчивающиеся
на другом. Никакое поле не должно встречаться в одном
маршруте дважды.
"""

n = 5


def on_field(x, y):
    return 0 <= x < n and 0 <= y < n


def main():
    stack = [(0, 0)]
    next_nodes = [[] for _ in range(n ** 2)]
    new_node = True
    count = 0
    while stack:
        count += 1
        x0, y0 = stack[-1]
        k = len(stack) - 1
        if new_node:
            next_nodes[k] = [
                (x, y) for dx, dy in ((1, 2), (2, 1))
                for sx in (1, -1) for sy in (1, -1)
                if on_field(x := x0 + dx * sx, y := y0 + dy * sy)
                and (x, y) not in stack]
        if next_nodes[k]:
            stack.append(next_nodes[k].pop())
            new_node = True
        else:
            stack.pop()
            new_node = False
    print(count)


if __name__ == '__main__':
    main()
