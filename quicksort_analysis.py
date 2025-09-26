

import random
import time
import sys

# Increase the recursion depth limit
sys.setrecursionlimit(5000) # Increased the recursion depth further

# ---------------------------
# Randomized Quicksort
# ---------------------------

def randomized_quicksort(arr):
    """
    Sorts an array using Randomized Quicksort algorithm.
    """
    def _quick_sort(arr, low, high):
        if low < high:
            pivot_index = randomized_partition(arr, low, high)
            _quick_sort(arr, low, pivot_index - 1)
            _quick_sort(arr, pivot_index + 1, high)

    def randomized_partition(arr, low, high):
        pivot_index = random.randint(low, high)
        arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
        return partition(arr, low, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    _quick_sort(arr, 0, len(arr) - 1)
    return arr

# ---------------------------
# Deterministic Quicksort
# ---------------------------

def deterministic_quicksort(arr):
    """
    Sorts an array using deterministic Quicksort (first element as pivot)
    """
    # Shuffle the array to avoid worst-case scenario on sorted/reverse-sorted data
    random.shuffle(arr)

    def _quick_sort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            _quick_sort(arr, low, pivot_index - 1)
            _quick_sort(arr, pivot_index + 1, high)

    def partition(arr, low, high):
        pivot = arr[low]
        i = low + 1
        for j in range(low + 1, high + 1):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[low], arr[i-1] = arr[i-1], arr[low]
        return i - 1

    _quick_sort(arr, 0, len(arr) - 1)
    return arr


# ---------------------------
# Empirical Comparison
# ---------------------------

def run_quicksort_tests():
    sizes = [1000, 5000, 10000, 20000] # Increased max size
    distributions = {
        "Random": lambda n: [random.randint(1, n) for _ in range(n)],
        "Sorted": lambda n: list(range(n)),
        "Reverse": lambda n: list(range(n, 0, -1)),
        "Repeated": lambda n: [random.choice([1,2,3,4,5]) for _ in range(n)]
    }

    for size in sizes:
        print(f"\nArray Size: {size}")
        for dist_name, gen_func in distributions.items():
            arr1 = gen_func(size)
            arr2 = arr1.copy() # Create a copy for deterministic sort

            start = time.time()
            randomized_quicksort(arr1)
            r_time = time.time() - start

            start = time.time()
            deterministic_quicksort(arr2)
            d_time = time.time() - start

            print(f"{dist_name} array -> Randomized QS: {r_time:.6f}s | Deterministic QS: {d_time:.6f}s")


# ---------------------------
# Run tests if this file is executed
# ---------------------------

if __name__ == "__main__":
    print("Empirical Quicksort Comparison:")
    run_quicksort_tests()



