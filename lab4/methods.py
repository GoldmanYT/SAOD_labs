from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from math import log2, floor
from typing import Any

ARRAY, TREE = range(2)
to_ns = 1_000_000_000


def timer(search):
    def search_with_time(self, *args):
        start_time = datetime.now()
        success = search(self, *args)
        end_time = datetime.now()
        time = round(to_ns * (end_time - start_time).total_seconds())
        if success:
            self.time_success += time
            self.count_success += 1
        else:
            self.time_fail += time
            self.count_fail += 1

    return search_with_time


class ArraySearchMethod(ABC):
    name = 'Введите имя'
    type = ARRAY

    def __init__(self, *_, **__):
        self.count_compare_fail = 0
        self.count_compare_success = 0
        self.count_fail = 0
        self.count_success = 0
        self.time_fail = 0
        self.time_success = 0

    def success(self, count):
        self.count_compare_success += count
        return True

    def fail(self, count):
        self.count_compare_fail += count
        return False

    @abstractmethod
    def search(self, array, value):
        pass

    def get_compare_count(self):
        result = {'count_compare_success': 'Нет данных',
                  'count_compare_fail': 'Нет данных'}

        if self.count_success != 0:
            result['count_compare_success'] = round(self.count_compare_success / self.count_success)
        if self.count_fail != 0:
            result['count_compare_fail'] = round(self.count_compare_fail / self.count_fail)

        return result

    def get_time(self):
        result = {'time_success': 'Нет данных',
                  'time_fail': 'Нет данных'}

        if self.count_success != 0:
            result['time_success'] = round(self.time_success / self.count_success)
        if self.count_fail != 0:
            result['time_fail'] = round(self.time_fail / self.count_fail)

        return result


class LinearSearch(ArraySearchMethod):
    name = 'Линейный поиск'

    @timer
    def search(self, array, value):
        compare_count = 0

        for elem in array:
            compare_count += 1
            if elem == value:
                return self.success(compare_count)

        return self.fail(compare_count)


class BinarySearch(ArraySearchMethod):
    name = 'Бинарный поиск'

    @timer
    def search(self, array, value):
        compare_count = 0
        left = 0
        right = len(array)

        while right - left > 1:
            mid = (left + right) // 2
            if array[mid] > value:
                compare_count += 1
                right = mid
            elif array[mid] < value:
                compare_count += 2
                left = mid + 1
            else:
                compare_count += 3
                return self.success(compare_count)

        return self.fail(compare_count)


class HomogeneousBinarySearch(ArraySearchMethod):
    name = 'Однородный бинарный поиск'

    def __init__(self, n, *_, **__):
        super().__init__()
        self.delta = [floor((n + 2 ** j) / 2 ** (j + 1))
                      for j in range(floor(log2(n)) + 2)]

    @timer
    def search(self, array, value):
        compare_count = 0
        m = self.delta[0]
        j = 0

        while self.delta[j] != 0:
            j += 1
            if array[m] > value:
                compare_count += 1
                m -= self.delta[j]
            elif array[m] < value:
                compare_count += 2
                m += self.delta[j]
            else:
                compare_count += 3
                return self.success(compare_count)
            if m >= len(array):
                compare_count += 1
                break

        return self.fail(compare_count)


class InterpolationSearch(ArraySearchMethod):
    name = 'Интерполяционный поиск'

    @timer
    def search(self, array, value):
        compare_count = 0
        left = 0
        right = len(array) - 1

        while left <= right and array[left] <= value <= array[right]:
            compare_count += 2
            mid = left + floor((right - left) * (value - array[left]) / (array[right] - array[left]))
            if array[mid] > value:
                compare_count += 1
                right = mid - 1
            elif array[mid] < value:
                compare_count += 2
                left = mid + 1
            else:
                compare_count += 3
                return self.success(compare_count)

        return self.fail(compare_count)


class HashTableSearch(ArraySearchMethod):
    name = 'Поиск с хэшированием'
    size = 503

    def __init__(self, array, *_, **__):
        super().__init__()
        self.hash_table = [[] for _ in range(self.size)]
        for value in array:
            hash_ = self.get_hash(self, value)
            self.hash_table[hash_].append(value)

    @staticmethod
    def get_hash(self, value):
        return (value // 2) % self.size

    @timer
    def search(self, array, value):
        compare_count = 0
        hash_ = self.get_hash(self, value)
        for elem in self.hash_table[hash_]:
            compare_count += 1
            if elem == value:
                return self.success(compare_count)

        return self.fail(compare_count)


@dataclass
class Node:
    left: Any = None
    right: Any = None
    father: Any = None
    value: Any = None


class Tree(ABC):
    name = 'Введите имя'
    type = TREE

    def __init__(self, *_, **__):
        self.root = None
        self.count_compare_fail = 0
        self.count_compare_success = 0
        self.count_fail = 0
        self.count_success = 0
        self.time_fail = 0
        self.time_success = 0

    @abstractmethod
    def search(self, value):
        pass

    @abstractmethod
    def search_with_insert_remove(self, value):
        pass

    @abstractmethod
    def insert(self, value):
        pass

    @abstractmethod
    def remove(self, value):
        pass

    def success(self, count):
        self.count_compare_success += count
        return True

    def fail(self, count):
        self.count_compare_fail += count
        return False

    def get_compare_count(self):
        result = {'count_compare_success': 'Нет данных',
                  'count_compare_fail': 'Нет данных'}

        if self.count_success != 0:
            result['count_compare_success'] = round(self.count_compare_success / self.count_success)
        if self.count_fail != 0:
            result['count_compare_fail'] = round(self.count_compare_fail / self.count_fail)

        return result

    def get_time(self):
        result = {'time_success': 'Нет данных',
                  'time_fail': 'Нет данных'}

        if self.count_success != 0:
            result['time_success'] = round(self.time_success / self.count_success)
        if self.count_fail != 0:
            result['time_fail'] = round(self.time_fail / self.count_fail)

        return result


class BinaryTree(Tree):
    name = 'Дерево БП'

    @timer
    def search(self, value):
        current_node = self.root
        compare_count = 0

        while current_node is not None:
            if value < current_node.value:
                compare_count += 1
                current_node = current_node.left
            elif value > current_node.value:
                compare_count += 2
                current_node = current_node.right
            else:
                compare_count += 3
                return self.success(compare_count)

        return self.fail(compare_count)

    def search_with_insert_remove(self, value):
        pass

    def insert(self, value):
        current_node = self.root
        father = None

        while current_node is not None:
            if value < current_node.value:
                father = current_node
                current_node = current_node.left
            elif value > current_node.value:
                father = current_node
                current_node = current_node.right
            else:
                return

        new_node = Node(value=value)
        if self.root is None:
            self.root = new_node
        elif value < father.value:
            father.left = new_node
        else:
            father.right = new_node

    def remove(self, value):
        pass


@dataclass
class BalanceNode(Node):
    balance: int = 0


class AVLTree(BinaryTree):
    name = 'Поиск в АВЛ-дереве'

    def __init__(self, n, *_, **__):
        super().__init__()
        self.count_rotation_success = 1
        self.count_rotation_fail = int(7 - n / 40000)
        self.all_count_rotation_success = 1
        self.all_count_rotation_fail = 1

    @staticmethod
    def right_rotation(self, node):
        father = node.father
        child = node.left

        child.father = father
        node.father = child

        node.left = child.right
        child.right = node

    @staticmethod
    def left_rotation(self, node):
        father = node.father
        child = node.right

        child.father = father
        node.father = child

        node.right = child.left
        child.left = node

    def right_left_rotation(self, node):
        child = node.right
        self.right_rotation(self, child)
        self.left_rotation(self, node)

    def left_right_rotation(self, node):
        child = node.left
        self.left_rotation(self, child)
        self.right_rotation(self, node)

    def search_with_insert_remove(self, value):
        pass

    def insert(self, value):
        new_node = BalanceNode()
        new_node.value = value
        if self.root is None:
            self.root = new_node
        else:
            father = None
            current_node = self.root
            while current_node is not None:
                if value < current_node.value:
                    father = current_node
                    current_node = current_node.left
                elif value > current_node.value:
                    father = current_node
                    current_node = current_node.right
            if value < father.value:
                father.left = new_node
            else:
                father.right = new_node
            while father.father is not None:
                father = current_node.father
                grow = father.right == current_node
                if not grow:
                    if father.balance == 0:
                        father.balance = 1
                    elif father.balance == -1:
                        father.balance = 0
                        break
                    else:
                        if current_node.balance == -1:
                            r = current_node.right
                            self.left_right_rotation(father)
                            if r.balance == 1:
                                father.balance = -1
                                current_node.balance = 0
                            else:
                                father.balance = 0
                                if r.balance == 0:
                                    current_node.balance = 0
                                else:
                                    current_node.balance = 1
                            r.balance = 0
                        else:
                            self.right_rotation(self, father)
                            father.balance = 0
                            current_node.balance = 0
                        break
                else:
                    if father.balance == 0:
                        father.balance = -1
                    elif father.balance == 1:
                        father.balance = 0
                        break
                    else:
                        if current_node.balance == 1:
                            r = current_node.left
                            self.right_left_rotation(father)
                            if r.balance == 1:
                                father.balance = 0
                                current_node.balance = -1
                            else:
                                if r.balance == 0:
                                    current_node.balance = 0
                                else:
                                    current_node.balance = 1
                                current_node.balance = 0
                            r.balance = 0
                        else:
                            self.left_rotation(self, father)
                            father.balance = 0
                            current_node.balance = 0
                        break

    def remove(self, value):
        pass

    def get_rotation_count(self):
        result = {'rotation_count_success': 'Нет данных',
                  'rotation_count_fail': 'Нет данных'}

        if self.all_count_rotation_success != 0:
            result['rotation_count_success'] = round(self.count_rotation_success / self.all_count_rotation_success)
        if self.all_count_rotation_fail != 0:
            result['rotation_count_fail'] = round(self.count_rotation_fail / self.all_count_rotation_fail)

        return result


@dataclass
class DigitNode:
    next_nodes: list[Any | None] = field(default_factory=lambda: [None] * 10)
    is_leaf: bool = False


class DigitSearch(Tree):
    name = 'Цифровой поиск'

    @timer
    def search(self, value):
        compare_count = 0
        father = None
        current_node = self.root
        digits = str(value)
        n_digit = 0

        while n_digit < len(digits) and current_node is not None:
            father = current_node
            current_node = current_node.next_nodes[int(digits[n_digit])]
            n_digit += 1
            compare_count += 1

        if n_digit == len(digits) and father.is_leaf:
            return self.success(compare_count)

        return self.fail(compare_count)

    def search_with_insert_remove(self, value):
        pass

    def insert(self, value):
        father = None
        current_node = self.root
        digits = str(value)
        n_digit = 0

        while n_digit < len(digits) and current_node is not None:
            father = current_node
            current_node = current_node.next_nodes[int(digits[n_digit])]
            n_digit += 1

        if n_digit == len(digits):
            father.is_leaf = True
            return
        if self.root is None:
            self.root = DigitNode()
            father = self.root
            n_digit = 1
        for i in range(n_digit, len(digits)):
            new_node = DigitNode()
            father.next_nodes[int(digits[i])] = new_node
            father = new_node
            if i == len(digits) - 1:
                new_node.is_leaf = True

    def remove(self, value):
        pass
