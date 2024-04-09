
import random
import unittest
import time

SEED = 65536

def selection_sort(arr: list[int]):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def bubble_sort(arr: list[int]):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def merge_sort(arr: list[int]):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


class TestSortingAlgorithms(unittest.TestCase):
    def test_selection_sort(self):
        arr = [random.randint(0, 100) for i in range(SEED)]
        start_time = time.time()
        selection_sort(arr)
        end_time = time.time()
        print(f"Selection sort: {end_time - start_time} seconds")
        self.assertEqual(arr, sorted(arr))

    def test_bubble_sort(self):
        arr = [random.randint(0, 100) for i in range(SEED)]
        start_time = time.time()
        bubble_sort(arr)
        end_time = time.time()
        print(f"Bubble sort: {end_time - start_time} seconds")
        self.assertEqual(arr, sorted(arr))

    def test_merge_sort(self):
        arr = [random.randint(0, 100) for i in range(SEED)]
        start_time = time.time()
        merge_sort(arr)
        end_time = time.time()
        print(f"Merge sort: {end_time - start_time} seconds")
        self.assertEqual(arr, sorted(arr))
        
                
if __name__ == '__main__':
    unittest.main()
    
# Run the tests

