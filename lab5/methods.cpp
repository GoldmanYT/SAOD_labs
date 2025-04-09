#include <ctime>
#include <random>

using namespace std;

struct Result {
    size_t compares;
    size_t swaps;
};

extern "C" int* create_array(int n)
{
    int* array = new int[n];
    return array;
}

extern "C" void delete_array(int* array)
{
    delete[] array;
}

extern "C" int* create_copy(int n, int* array)
{
    int* copy = new int[n];
    for (int i = 0; i < n; ++i) {
        copy[i] = array[i];
    }
    return copy;
}

extern "C" void copy_array(int n, int* array, int* dest)
{
    for (int i = 0; i < n; ++i) {
        dest[i] = array[i];
    }
}

extern "C" void randomize_array(int n, int* array)
{
    srand(time(0));
    for (int i = 0; i < n; ++i) {
        array[i] = rand();
    }
}

extern "C" void insert_sort(int n, int* array, Result* result)
{
    for (int j = 1; j < n; ++j) {
        int i = j - 1, t = array[j];
        while (i >= 0 && t < array[i]) {
            ++result->compares;
            ++result->swaps;
            array[i + 1] = array[i];
            --i;
        }
        ++result->swaps;
        array[i + 1] = t;
    }
}

extern "C" void bin_insert_sort(int n, int* array, Result* result)
{
    for (int j = 1; j < n; j++) {
        int left = -1, right = j, t = array[j], i;
        while (right - left > 1) {
            int mid = (left + right) / 2;
            ++result->compares;
            if (t >= array[mid]) {
                left = mid;
            } else {
                right = mid;
            }
        }
        for (i = j - 1; i >= right; --i) {
            array[i + 1] = array[i];
            ++result->swaps;
        }
        array[i + 1] = t;
        ++result->swaps;
    }
}

extern "C" void bubble_sort(int n, int* array, Result* result)
{
    int b = n;
    while (b) {
        int t = 0;
        for (int j = 0; j < b - 1; ++j) {
            if (array[j] > array[j + 1]) {
                swap(array[j], array[j + 1]);
                result->swaps += 3;
                t = j + 1;
            }
            ++result->compares;
        }
        b = t;
    }
}

extern "C" void shaker_sort(int n, int* array, Result* result)
{
    int left = 0, right = n - 1;
    while (left < right) {
        int t = left;
        for (int j = left; j < right; ++j) {
            if (array[j] > array[j + 1]) {
                swap(array[j], array[j + 1]);
                result->swaps += 3;
                t = j;
            }
            ++result->compares;
        }
        right = t;
        t = right;
        for (int j = right; j > left; --j) {
            if (array[j - 1] > array[j]) {
                swap(array[j - 1], array[j]);
                result->swaps += 3;
                t = j;
            }
            ++result->compares;
        }
        left = t;
    }
}

extern "C" void quick_sort(int n, int* array, Result* result, int f, int l)
{
    if (f > l)
        return;

    int i = f + 1;
    ++result->compares;
    while (array[i] < array[f]) {
        ++i;
        ++result->compares;
    }
    int j = l;
    ++result->compares;
    while (array[j] > array[f]) {
        j--;
        ++result->compares;
    }

    while (i < j) {
        swap(array[i], array[j]);
        result->swaps += 3;

        ++i;
        ++result->compares;
        while (array[i] < array[f]) {
            ++i;
            ++result->compares;
        }
        --j;
        ++result->compares;
        while (array[j] > array[f]) {
            --j;
            ++result->compares;
        }
    }
    swap(array[f], array[j]);
    result->swaps += 3;
    quick_sort(n, array, result, f, j - 1);
    quick_sort(n, array, result, j + 1, l);
}

extern "C" void selection_sort(int n, int* array, Result* result)
{
    for (int i = n - 1; i > 0; --i) {
        int j = 0;
        for (int k = 1; k <= i; ++k) {
            ++result->compares;
            if (array[k] > array[j]) {
                j = k;
            }
        }
        swap(array[j], array[i]);
        result->swaps += 3;
    }
}

extern "C" void counting_sort(int n, int* array, Result* result)
{
    int* c = new int[n] {};

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            ++result->compares;
            ++result->swaps;
            if (array[i] < array[j]) {
                ++c[j];
            } else {
                ++c[i];
            }
        }
    }
    int* copy = new int[n];

    for (int i = 0; i < n; ++i) {
        copy[c[i]] = array[i];
    }
    for (int i = 0; i < n; ++i) {
        array[i] = copy[i];
    }

    delete[] copy;
    delete[] c;
}

extern "C" void merge_sort(int n, int* array, Result* result)
{
    int* copy = new int[n];

    bool t = 0;
    int k = 1;
    while (k < n) {
        if (t) {
            bool d = 0;
            int dest_left = 0, dest_right = n - 1;
            int left = 0, right = n - 1;
            int left_len = min(k, right - left + 1);
            int right_len = min(k, max(0, right - left + 1 - left_len));
            while (left < right) {
                if (d) {
                    int i = left, j = right;
                    while (i < left + left_len && j > right - right_len) {
                        if (copy[i] < copy[j]) {
                            array[dest_right] = copy[i];
                            ++result->swaps;
                            --dest_right;
                            ++i;
                        } else {
                            array[dest_right] = copy[j];
                            ++result->swaps;
                            --dest_right;
                            --j;
                        }
                        ++result->compares;
                    }
                    while (i < left + left_len) {
                        array[dest_right] = copy[i];
                        ++result->swaps;
                        --dest_right;
                        ++i;
                    }
                    while (j > right - right_len) {
                        array[dest_right] = copy[j];
                        ++result->swaps;
                        --dest_right;
                        --j;
                    }
                } else {
                    int i = left, j = right;
                    while (i < left + left_len && j > right - right_len) {
                        if (copy[i] < copy[j]) {
                            array[dest_left] = copy[i];
                            ++result->swaps;
                            ++dest_left;
                            ++i;
                        } else {
                            array[dest_left] = copy[j];
                            ++result->swaps;
                            ++dest_left;
                            --j;
                        }
                        ++result->compares;
                    }
                    while (i < left + left_len) {
                        array[dest_left] = copy[i];
                        ++result->swaps;
                        ++dest_left;
                        ++i;
                    }
                    while (j > right - right_len) {
                        array[dest_left] = copy[j];
                        ++result->swaps;
                        ++dest_left;
                        --j;
                    }
                }
                left += left_len;
                right -= right_len;
                left_len = min(k, right - left + 1);
                right_len = min(k, max(0, right - left + 1 - left_len));
                d = !d;
            }
        } else {
            bool d = 0;
            int dest_left = 0, dest_right = n - 1;
            int left = 0, right = n - 1;
            int left_len = min(k, right - left + 1);
            int right_len = min(k, max(0, right - left + 1 - left_len));
            while (left < right) {
                if (d) {
                    int i = left, j = right;
                    while (i < left + left_len && j > right - right_len) {
                        if (array[i] < array[j]) {
                            copy[dest_right] = array[i];
                            ++result->swaps;
                            --dest_right;
                            ++i;
                        } else {
                            copy[dest_right] = array[j];
                            ++result->swaps;
                            --dest_right;
                            --j;
                        }
                        ++result->compares;
                    }
                    while (i < left + left_len) {
                        copy[dest_right] = array[i];
                        ++result->swaps;
                        --dest_right;
                        ++i;
                    }
                    while (j > right - right_len) {
                        copy[dest_right] = array[j];
                        ++result->swaps;
                        --dest_right;
                        --j;
                    }
                } else {
                    int i = left, j = right;
                    while (i < left + left_len && j > right - right_len) {
                        if (array[i] < array[j]) {
                            copy[dest_left] = array[i];
                            ++result->swaps;
                            ++dest_left;
                            ++i;
                        } else {
                            copy[dest_left] = array[j];
                            ++result->swaps;
                            ++dest_left;
                            --j;
                        }
                        ++result->compares;
                    }
                    while (i < left + left_len) {
                        copy[dest_left] = array[i];
                        ++result->swaps;
                        ++dest_left;
                        ++i;
                    }
                    while (j > right - right_len) {
                        copy[dest_left] = array[j];
                        ++result->swaps;
                        ++dest_left;
                        --j;
                    }
                }
                left += left_len;
                right -= right_len;
                left_len = min(k, right - left + 1);
                right_len = min(k, max(0, right - left + 1 - left_len));
                d = !d;
            }
        }
        k <<= 1;
        t = !t;
    }
    if (t) {
        for (int i = 0; i < n; ++i) {
            array[i] = copy[i];
            ++result->swaps;
        }
    }

    delete[] copy;
}

extern "C" void merge_sort_list(int n, int* array, Result* result)
{
    int* copy = new int[n];

    bool t = 0;
    int k = 1;
    while (k < n) {
        if (t) {
            bool d = 0;
            int dest_left = 0, dest_right = n - 1;
            int left = 0, right = n - 1;
            int left_len = min(k, right - left + 1);
            int right_len = min(k, max(0, right - left + 1 - left_len));
            while (left < right) {
                if (d) {
                    int i = left, j = right;
                    while (i < left + left_len && j > right - right_len) {
                        if (copy[i] < copy[j]) {
                            array[dest_right] = copy[i];
                            ++result->swaps;
                            --dest_right;
                            ++i;
                        } else {
                            array[dest_right] = copy[j];
                            ++result->swaps;
                            --dest_right;
                            --j;
                        }
                        ++result->compares;
                    }
                    while (i < left + left_len) {
                        array[dest_right] = copy[i];
                        ++result->swaps;
                        --dest_right;
                        ++i;
                    }
                    while (j > right - right_len) {
                        array[dest_right] = copy[j];
                        ++result->swaps;
                        --dest_right;
                        --j;
                    }
                } else {
                    int i = left, j = right;
                    while (i < left + left_len && j > right - right_len) {
                        if (copy[i] < copy[j]) {
                            array[dest_left] = copy[i];
                            ++result->swaps;
                            ++dest_left;
                            ++i;
                        } else {
                            array[dest_left] = copy[j];
                            ++result->swaps;
                            ++dest_left;
                            --j;
                        }
                        ++result->compares;
                    }
                    while (i < left + left_len) {
                        array[dest_left] = copy[i];
                        ++result->swaps;
                        ++dest_left;
                        ++i;
                    }
                    while (j > right - right_len) {
                        array[dest_left] = copy[j];
                        ++result->swaps;
                        ++dest_left;
                        --j;
                    }
                }
                left += left_len;
                right -= right_len;
                left_len = min(k, right - left + 1);
                right_len = min(k, max(0, right - left + 1 - left_len));
                d = !d;
            }
        } else {
            bool d = 0;
            int dest_left = 0, dest_right = n - 1;
            int left = 0, right = n - 1;
            int left_len = min(k, right - left + 1);
            int right_len = min(k, max(0, right - left + 1 - left_len));
            while (left < right) {
                if (d) {
                    int i = left, j = right;
                    while (i < left + left_len && j > right - right_len) {
                        if (array[i] < array[j]) {
                            copy[dest_right] = array[i];
                            ++result->swaps;
                            --dest_right;
                            ++i;
                        } else {
                            copy[dest_right] = array[j];
                            ++result->swaps;
                            --dest_right;
                            --j;
                        }
                        ++result->compares;
                    }
                    while (i < left + left_len) {
                        copy[dest_right] = array[i];
                        ++result->swaps;
                        --dest_right;
                        ++i;
                    }
                    while (j > right - right_len) {
                        copy[dest_right] = array[j];
                        ++result->swaps;
                        --dest_right;
                        --j;
                    }
                } else {
                    int i = left, j = right;
                    while (i < left + left_len && j > right - right_len) {
                        if (array[i] < array[j]) {
                            copy[dest_left] = array[i];
                            ++result->swaps;
                            ++dest_left;
                            ++i;
                        } else {
                            copy[dest_left] = array[j];
                            ++result->swaps;
                            ++dest_left;
                            --j;
                        }
                        ++result->compares;
                    }
                    while (i < left + left_len) {
                        copy[dest_left] = array[i];
                        ++result->swaps;
                        ++dest_left;
                        ++i;
                    }
                    while (j > right - right_len) {
                        copy[dest_left] = array[j];
                        ++result->swaps;
                        ++dest_left;
                        --j;
                    }
                }
                left += left_len;
                right -= right_len;
                left_len = min(k, right - left + 1);
                right_len = min(k, max(0, right - left + 1 - left_len));
                d = !d;
            }
        }
        k <<= 1;
        t = !t;
    }
    if (t) {
        for (int i = 0; i < n; ++i) {
            array[i] = copy[i];
        }
    }

    delete[] copy;
}