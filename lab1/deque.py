from dataclasses import dataclass
from typing import Any


class DequeArray:
    """
    Дек на основе массива:
        left:
            указатель на элемент левее начала дека
        right:
            указатель на элемент правее конца дека
        data:
            закольцованный массив с данными
        (m - 1):
            максимальное количество элементов
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

    def __str__(self):
        if self.left < self.right:
            return str([self.data[i] for i in range(self.left + 1, self.right)])
        return str([self.data[i] for i in range(self.left + 1, self.m)] +
                   [self.data[i] for i in range(0, self.right)])


@dataclass
class Element:
    """
    Элемент связвного списка:
        info:
            поле с данными
        prev:
            предыдущий элемент
        next:
            следующий элемент
    """
    info: Any
    prev: Any
    next: Any

    def __str__(self):
        return str(self.info)

    def __repr__(self):
        return repr(self.info)


class DequeList:
    """
    Дек с заголовком на основе связного списка:
        header:
            заголовок дека
            info: не используется
            prev: последний элемент дека
            next: первый элемент дека
    """

    def __init__(self, *_):
        self.header = Element(None, None, None)

    def is_empty(self):
        return self.header.next is None and self.header.prev is None

    def push_left(self, x):
        new_elem = Element(x, None, self.header.next)
        first_elem = self.header.next
        if first_elem is not None:
            first_elem.prev = new_elem
        self.header.next = new_elem
        if self.header.prev is None:
            self.header.prev = new_elem

    def push_right(self, x):
        new_elem = Element(x, self.header.prev, None)
        last_elem = self.header.prev
        if last_elem is not None:
            last_elem.next = new_elem
        self.header.prev = new_elem
        if self.header.next is None:
            self.header.next = new_elem

    def pop_left(self):
        if self.is_empty():
            return ValueError
        first_elem = self.header.next
        self.header.next = first_elem.next
        new_first_elem = self.header.next
        if new_first_elem is None:
            self.header.prev = None
        else:
            new_first_elem.prev = None
        return first_elem.info

    def pop_right(self):
        if self.is_empty():
            return ValueError
        last_elem = self.header.prev
        self.header.prev = last_elem.prev
        new_last_elem = self.header.prev
        if new_last_elem is None:
            self.header.next = None
        else:
            new_last_elem.next = None
        return last_elem.info

    def __str__(self):
        result = [self.header.next]
        while (elem := result[-1]) is not None:
            result.append(elem.next)
        return str(result[:-1])


def test():
    d = DequeList()
    operations = [
        ('+', 1),
        ('+', 2),
        ('-', None),
        ('+', 3),
        ('-', None),
        ('-', None),
    ]
    for c, x in operations:
        if c == '+':
            d.push_right(x)
        elif c == '-':
            d.pop_right()
        print(d)


if __name__ == '__main__':
    test()
