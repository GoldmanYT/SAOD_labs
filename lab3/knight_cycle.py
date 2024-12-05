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


def knight_cycle():
    s = {0: [(0, 0)]}
    a = []
    count = 0
    k = 0
    while k >= 0:
        while s[k]:
            x0, y0 = s[k].pop()
            a.append((x0, y0))
            if a[-1] == (n - 1, n - 1):
                count += 1
            k += 1
            s[k] = [
                (x, y) for dx, dy in ((1, 2), (2, 1))
                for sx in (1, -1) for sy in (1, -1)
                if on_field(x := x0 + dx * sx, y := y0 + dy * sy) and (x, y) not in a
            ]
        if a:
            a.pop()
        k -= 1
    print(count)


if __name__ == '__main__':
    knight_cycle()
