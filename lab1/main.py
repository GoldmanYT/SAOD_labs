"""
САОД
Лабораторная работа 1
"""


OPERATIONS = '+-*/'


class Deque:
    """
    Очередь на основе массива:
    left: указатель на элемент левее начала дека
    right: указатель на элемент правее конца дека
    data: закольцованный массив с данными
    (m - 1): максимальное количество элементов
    """
    def __init__(self, m):
        self.m = m
        self.data = [None] * m
        self.left = 0
        self.right = 1

    def is_empty(self):
        return (self.left + 1) % self.m == self.right

    def push_left(self, x):
        self.data[self.left] = x
        self.left = (self.left - 1) % self.m
        if self.is_empty():
            raise OverflowError

    def push_right(self, x):
        self.data[self.right] = x
        self.right = (self.right + 1) % self.m
        if self.is_empty():
            raise OverflowError

    def pop_left(self):
        if self.is_empty():
            raise ValueError
        self.left = (self.left + 1) % self.m
        result = self.data[self.left]
        self.data[self.left] = None
        return result

    def pop_right(self):
        if self.is_empty():
            raise ValueError
        self.right = (self.right - 1) % self.m
        result = self.data[self.right]
        self.data[self.right] = None
        return result


def prefix_to_postfix(prefix):
    d = Deque(len(prefix) // 2 + 2)
    for c in reversed(prefix):
        if c in OPERATIONS:
            d.push_right(d.pop_right() + d.pop_right() + c)
        else:
            d.push_right(c)
    return d.pop_right()


def digits_at_the_end(text):
    result = []
    for s in text.split('\n'):
        d = Deque(len(s) + 1)
        ans = ''
        for c in s:
            if c.isdigit():
                d.push_right(c)
            else:
                ans += c
        while not d.is_empty():
            ans += d.pop_left()
        result.append(ans)
    return '\n'.join(result)


def main():
    prefix = '*-*-+ab*cde-fg+hi'
    print(f'prefix: {prefix}')
    posfix = prefix_to_postfix(prefix)
    print(f'postfix: {posfix}')
    print()

    text = 'some text 123\none - 1, two - 2, three - 3\n123 another text'
    print('text: ')
    print(text)
    print()
    print('transformed text:')
    print(digits_at_the_end(text))


if __name__ == '__main__':
    main()
