from random import randint
from datetime import datetime as dt
from dataclasses import dataclass
from typing import Any
from pprint import pprint

SUCCESS = 'success'
FAIL = 'fail'


@dataclass
class Result:
    time: float
    comparisons: int

    def __add__(self, other):
        return Result(
            self.time + other.time,
            self.comparisons + other.comparisons
        )

    def __truediv__(self, other):
        return Result(
            self.time / other,
            self.comparisons / other
        )


@dataclass
class Method:
    name: str
    function: Any

    def __hash__(self):
        return self.function.__hash__()

    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)


def get_array(n):
    return sorted(randint(1, n) * 2 for _ in range(n))


def get_time_comparisons(method, array, key):
    start_time = dt.now()
    comparisons = method(array, key)
    end_time = dt.now()
    return (end_time - start_time).total_seconds(), comparisons


def research(n=1000, k=1000):
    methods = [
        Method('Линейный поиск', linear_search)
    ]
    array = get_array(n)
    data = {method: {
        SUCCESS: [],
        FAIL: []
    } for method in methods}

    for _ in range(k):
        success_key = randint(1, n) * n
        fail_key = randint(0, n) * 2 + 1

        for status, key in zip(
                (SUCCESS, FAIL),
                (success_key, fail_key)
        ):
            for method in methods:
                time, comparisons = get_time_comparisons(
                    method, array, key
                )
                data[method][status].append(Result(time, comparisons))

    for method in methods:
        for status in (FAIL, SUCCESS):
            results = data[method][status]
            mean = sum(results, Result(0, 0)) / len(results)
            data[method][status] = mean

    return data


def linear_search(array, key):
    comparisons = 0

    for k in array:
        comparisons += 1
        if k == key:
            return comparisons

    return comparisons


if __name__ == '__main__':
    pprint(research())
