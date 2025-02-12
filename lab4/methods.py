from abc import ABC, abstractmethod
from datetime import datetime


def timer(search):
    def search_with_time(self, array, value):
        start_time = datetime.now()
        success = search(self, array, value)
        end_time = datetime.now()
        if success:
            self.time_success += (end_time - start_time).total_seconds()
        else:
            self.time_fail += (end_time - start_time).total_seconds()

    return search_with_time


class ArraySearchMethod(ABC):
    name = None

    def __init__(self):
        self.count_compare_fail = 0
        self.count_compare_success = 0
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

    def __str__(self):
        return str({'count_compare_fail': self.count_compare_fail,
                    'count_compare_success': self.count_compare_success,
                    'time_fail': self.time_fail,
                    'time_success': self.time_success})


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
            compare_count += 1
            if array[mid] > value:
                right = mid
            elif array[mid] < value:
                left = mid + 1
            else:
                return self.success(compare_count)

        return self.fail(compare_count)
