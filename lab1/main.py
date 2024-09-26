"""
САОД
Лабораторная работа 1
"""

from deque import DequeList as Deque

OPERATIONS = '+-*/'


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


def test_prefix_to_postfix(prefix):
    print(f'prefix: {prefix}')
    postfix = prefix_to_postfix(prefix)
    print(f'postfix: {postfix}')
    print()


def test_digits_at_the_end(text):
    print('text: ')
    print(text)
    print()
    print('transformed text:')
    print(digits_at_the_end(text))


def main():
    prefix = '*-*-+ab*cde-fg+hi'
    test_prefix_to_postfix(prefix)

    text = 'some text 123\none - 1, two - 2, three - 3\n123 another text'
    test_digits_at_the_end(text)


if __name__ == '__main__':
    main()
