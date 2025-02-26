from abc import ABC, abstractmethod
from datetime import datetime
from math import log2, floor

to_ns = 1_000_000_000


def timer(search):
    def search_with_time(self, array, value):
        start_time = datetime.now()
        success = search(self, array, value)
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
    name = None

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

    def get_result(self):
        return {'count_compare_success': round(self.count_compare_success / self.count_success),
                'count_compare_fail': round(self.count_compare_fail / self.count_fail),
                'time_success': round(self.time_success / self.count_success),
                'time_fail': round(self.time_fail / self.count_fail)}

    def get_compare_count(self):
        return {'count_compare_success': round(self.count_compare_success / self.count_success),
                'count_compare_fail': round(self.count_compare_fail / self.count_fail)}

    def get_time(self):
        return {'time_success': round(self.time_success / self.count_success),
                'time_fail': round(self.time_fail / self.count_fail)}

    def __str__(self):
        return str(self.get_result())


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

        return self.fail(compare_count)


class InterpolationSearch(ArraySearchMethod):
    name = 'Интерполяционный поиск'

    @timer
    def search(self, array, value):
        compare_count = 0
        left = 0
        right = len(array) - 1

        while left <= right:
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

            if array[left] > value:
                compare_count += 1
                break
            elif array[right] < value:
                compare_count += 2
                break
            compare_count += 2

        return self.fail(compare_count)
