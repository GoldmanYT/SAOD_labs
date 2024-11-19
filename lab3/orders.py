"""
Блок 3:
Имеется конечное множество заказов, каждый из которых
требует ровно одну единицу времени для своего
выполнения. Для каждого заказа известны срок выполнения
и штраф за невыполнение к сроку. Требуется найти порядок
выполнения заказов, при котором сумма штрафов будет
наименьшей.
"""

from random import randint
from dataclasses import dataclass


@dataclass()
class Order:
    deadline: int
    fine: int


def get_orders(n: int) -> list[Order]:
    a, b = 10, 99
    return [Order(
        deadline=randint(a, b), fine=randint(a, b)
    ) for _ in range(n)]


def best_order_of_order():
    n = 10
    orders: list[Order] = get_orders(n)
    k = 0
    while k >= 0:
        pass


if __name__ == '__main__':
    best_order_of_order()
