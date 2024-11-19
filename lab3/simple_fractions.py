"""
Блок 2:
Найти все простые несократимые дроби, заключенные между
0 и 1, знаменатели которых не превышают 9 (дробь
задается двумя натуральными числами - числителем и
знаменателем).
"""

MAX_N = 10


def simple_fractions():
    numerator0 = 1
    denominator0 = 2
    is_fraction = [[True] * MAX_N for _ in range(MAX_N)]

    for numerator in range(numerator0, MAX_N):
        for denominator in range(denominator0, MAX_N):
            if is_fraction[numerator][denominator]:
                for numerator2 in range(denominator, MAX_N):
                    is_fraction[numerator2][denominator] = False
                for k in range(2, (MAX_N + denominator - 1) // denominator):
                    is_fraction[numerator * k][denominator * k] = False

    ans = []
    for numerator in range(numerator0, MAX_N):
        for denominator in range(denominator0, MAX_N):
            if is_fraction[numerator][denominator]:
                ans.append(f'{numerator} / {denominator}')

    print('\n'.join(ans))


if __name__ == '__main__':
    simple_fractions()
