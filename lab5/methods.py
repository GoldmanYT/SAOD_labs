import ctypes
import os
from datetime import datetime as dt


class Result(ctypes.Structure):
    _fields_ = [('swaps', ctypes.c_ulonglong),
                ('compares', ctypes.c_ulonglong)]


def array_to_list(n, array):
    return [array[i] for i in range(n)]


def main():
    test = 0

    if test:
        result = Result(0, 0)
        n = 10
        array = methods.create_array(n)
        methods.randomize_array(n, array)

        methods.merge_sort_list(n, array, result)
        print(array_to_list(n, array))
        print(result.swaps, result.compares)
    else:
        start_time = dt.now()
        for n in range(2000, 10001, 2000):
            result = Result(0, 0)
            array = methods.create_array(n)
            for k in range(1000):
                methods.randomize_array(n, array)
                methods.merge_sort_list(n, array, result)
            methods.delete_array(array)

            print(result.compares / n, result.swaps / n)
        end_time = dt.now()
        print(end_time - start_time)


abs_path = os.path.abspath('methods.dll')
methods = ctypes.CDLL(abs_path)

# int* create_array(int n)
methods.create_array.restype = ctypes.POINTER(ctypes.c_int)
methods.create_array.argtypes = [ctypes.c_int]

# void delete_array(int* array)
methods.delete_array.argtypes = [ctypes.POINTER(ctypes.c_int)]

# int* create_copy(int n, int* array)
methods.create_copy.restype = ctypes.POINTER(ctypes.c_int)
methods.create_copy.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]

# void copy_array(int n, int* array, int* dest)
methods.copy_array.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]

# void randomize_array(int n, int* array)
methods.randomize_array.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]

# void insert_sort(int n, int* array, Result* result)
methods.insert_sort.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(Result)]

# void bin_insert_sort(int n, int* array, Result* result)
methods.bin_insert_sort.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(Result)]

# void bubble_sort(int n, int* array, Result* result)
methods.bubble_sort.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(Result)]

# void shaker_sort(int n, int* array, Result* result)
methods.shaker_sort.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(Result)]

# void quick_sort(int n, int* array, Result* result, int f, int l)
methods.quick_sort.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(Result), ctypes.c_int,
                               ctypes.c_int]

# void selection_sort(int n, int* array, Result* result)
methods.selection_sort.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(Result)]

# void counting_sort(int n, int* array, Result* result)
methods.counting_sort.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(Result)]

# void merge_sort(int n, int* array, Result* result)
methods.merge_sort.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(Result)]

# void merge_sort_list(int n, int* array, Result* result)
methods.merge_sort_list.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(Result)]

list_of_methods = [
    methods.insert_sort,
    methods.bin_insert_sort,
    methods.bubble_sort,
    methods.shaker_sort,
    methods.quick_sort,
    methods.selection_sort,
    methods.counting_sort,
    methods.merge_sort,
    methods.merge_sort_list
]

list_of_names = [
    'Вставками',
    'Бинарными вставками',
    'Пузырьковая',
    'Шейкер',
    'Быстрая',
    'Выбором',
    'Подсчётом',
    'Слиянием',
    'Слиянием списков'
]

__all__ = ['methods', 'list_of_methods', 'Result', 'list_of_names']

if __name__ == '__main__':
    main()
