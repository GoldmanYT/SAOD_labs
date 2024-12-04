"""
Блок 3:
Имеется конечное множество заказов, каждый из которых
требует ровно одну единицу времени для своего
выполнения. Для каждого заказа известны срок выполнения
и штраф за невыполнение к сроку. Требуется найти порядок
выполнения заказов, при котором сумма штрафов будет
наименьшей.
"""
from math import inf
from random import randint
from dataclasses import dataclass

from typing import List


@dataclass()
class Order:
    deadline: int
    fine: int


def get_orders(n: int) -> List[Order]:
    a, b = 1, 9
    return [Order(
        deadline=randint(a, b), fine=randint(a, b)
    ) for _ in range(n)]


def best_order_of_order():
    n = 10
    orders: List[Order] = get_orders(n)
    next_orders = {}
    stack: List[Order] = [orders[0]]
    current_fine = 0
    best_solution = inf
    new_order = True
    for i, order in enumerate(orders, 1):
        print(f'Заказ №{i}: срок - {order.deadline}, штраф - {order.fine}')
    while stack:
        k = len(stack) - 1
        if len(stack) == n:
            best_solution = min(best_solution, current_fine)
        if current_fine >= best_solution:
            next_orders[k] = []
        elif new_order:
            next_orders[k] = [
                order for order in orders
                if order not in stack
            ]
        if next_orders[k]:
            new_order = True
            order = next_orders[k].pop()
            stack.append(order)
            if len(stack) > order.deadline:
                current_fine += order.fine
        else:
            new_order = False
            order = stack.pop()
            if len(stack) + 1 > order.deadline:
                current_fine -= order.fine
    print(current_fine)
    print(f'Минимальный штраф: {best_solution}')


if __name__ == '__main__':
    best_order_of_order()
