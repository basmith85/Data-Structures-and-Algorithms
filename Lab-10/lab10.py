from random import randint, seed
import time

class Sorting:
    def __init__(self, size):
        self.arr = []  # Initialize an empty list
        self.size = size

    def add(self, element):
        if len(self.arr) < self.size:
            self.arr.append(element)
        else:
            print("Array is already full, cannot add more elements.")
    
    def selection_sort(self):
        """Implements selection sort"""
        n = len(self.arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]

    def max_heapify(self, n, i):
        """Implements Heapify for array"""
        largest = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        if left_child < n and self.arr[left_child] > self.arr[largest]:
            largest = left_child
        if right_child < n and self.arr[right_child] > self.arr[largest]:
            largest = right_child
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.max_heapify(n, largest)

    def heap_sort(self):
        """Implements Heap sort"""
        n = len(self.arr)
        for i in range(n // 2 - 1, -1, -1):
            self.max_heapify(n, i)
        for i in range(n - 1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.max_heapify(i, 0)

    def merge_sort(self):
        """Immplements Merge sort"""
        def merge_sort_helper(array):
            if len(array) > 1:
                r = len(array) // 2
                L = array[:r]
                M = array[r:]
                merge_sort_helper(L)
                merge_sort_helper(M)
                i = j = k = 0
                while i < len(L) and j < len(M):
                    if L[i] < M[j]:
                        array[k] = L[i]
                        i += 1
                    else:
                        array[k] = M[j]
                        j += 1
                    k += 1
                
                while i < len(L):
                    array[k] = L[i]
                    i += 1
                    k += 1
                
                while j < len(M):
                    array[k] = M[j]
                    j += 1
                    k += 1
        merge_sort_helper(self.arr)

    def test_sorting_time(self, sorting_method_name):
        sizes = [10000, 20000, 30000, 40000, 50000]
        times = []
        for size in sizes:
            self.arr = [randint(1, 100) for _ in range(size)]
            sorting_method = getattr(self, f"{sorting_method_name}_sort")
            start_time = time.time()
            sorting_method()
            end_time = time.time()
            time_taken = end_time - start_time
            print(f"Time taken for {sorting_method_name} with array size {size}: {time_taken:.6f} seconds")
            times.append(time_taken)
        return times

#Test Sorted array
def is_sorted(arr):
  if arr == sorted(arr):
    print("Passed!")
  else:
    print("Failed!")

# Test each sirting technique
def test_sort_algorithms(sorting_method, set_seed=None):
  if seed != None:
    seed(set_seed)
  sorting = Sorting(10)
  # Add 10 random elements
  for _ in range(10):
    sorting.add(randint(1, 100))
  # Apply the sorting algorithm
  if sorting_method == 'selection':
    sorting.selection_sort()
    print("Selection Sort:", is_sorted(sorting.arr))
  elif sorting_method == 'heap':
    sorting.heap_sort()
    print("Heap Sort:", is_sorted(sorting.arr))
  elif sorting_method == 'merge':
    sorting.merge_sort()
    print("Merge Sort:", is_sorted(sorting.arr))
        
#Test run time
def run_time_tests():
    seeding = 45
    array_sizes = [10000, 20000, 30000, 40000, 50000]
    methods = ['selection', 'heap', 'merge']
    print("Array Size\t\tSelection Sort\t\tHeap Sort\t\tMerge Sort")
    for size in array_sizes:
        times = []
        for m in methods:
            sorting = Sorting(size)
            seed(seeding)
            for _ in range(size):
                sorting.add(randint(1, 50000))
            interval = sorting.test_sorting_time(m)
            times.append(interval)
        print(f"{size}\t\t{times[0][0]:.6f}\t\t{times[1][0]:.6f}\t\t{times[2][0]:.6f}")

#test case execution
seed_num = 43   
test_sort_algorithms('selection', seed_num)
test_sort_algorithms('heap', seed_num)
test_sort_algorithms('merge', seed_num)
run_time_tests()

"""
Part B:
Passed!
Selection Sort: None
Passed!
Heap Sort: None
Passed!
Merge Sort: None
Array Size              Selection Sort          Heap Sort               Merge Sort
Time taken for selection with array size 10000: 2.423777 seconds
Time taken for selection with array size 20000: 8.625952 seconds
Time taken for selection with array size 30000: 19.176860 seconds
Time taken for selection with array size 40000: 33.931798 seconds
Time taken for selection with array size 50000: 53.037831 seconds
Time taken for heap with array size 10000: 0.035973 seconds
Time taken for heap with array size 20000: 0.072239 seconds
Time taken for heap with array size 30000: 0.099733 seconds
Time taken for heap with array size 40000: 0.149518 seconds
Time taken for heap with array size 50000: 0.181489 seconds
Time taken for merge with array size 10000: 0.022799 seconds
Time taken for merge with array size 20000: 0.034073 seconds
Time taken for merge with array size 30000: 0.058572 seconds
Time taken for merge with array size 40000: 0.084949 seconds
Time taken for merge with array size 50000: 0.111616 seconds
10000           2.423777                0.035973                0.022799
Time taken for selection with array size 10000: 2.131589 seconds
Time taken for selection with array size 20000: 8.596958 seconds
Time taken for selection with array size 30000: 19.272907 seconds
Time taken for selection with array size 40000: 35.750083 seconds
Time taken for selection with array size 50000: 54.191370 seconds
Time taken for heap with array size 10000: 0.035973 seconds
Time taken for heap with array size 20000: 0.079188 seconds
Time taken for heap with array size 30000: 0.102056 seconds
Time taken for heap with array size 40000: 0.142177 seconds
Time taken for heap with array size 50000: 0.200702 seconds
Time taken for merge with array size 10000: 0.033401 seconds
Time taken for merge with array size 20000: 0.041701 seconds
Time taken for merge with array size 30000: 0.065892 seconds
Time taken for merge with array size 40000: 0.094908 seconds
Time taken for merge with array size 50000: 0.108904 seconds
20000           2.131589                0.035973                0.033401
Time taken for selection with array size 10000: 2.138090 seconds
Time taken for selection with array size 20000: 8.540448 seconds
Time taken for selection with array size 30000: 19.357210 seconds
Time taken for selection with array size 40000: 34.001286 seconds
Time taken for selection with array size 50000: 54.255009 seconds
Time taken for heap with array size 10000: 0.035455 seconds
Time taken for heap with array size 20000: 0.066940 seconds
Time taken for heap with array size 30000: 0.101902 seconds
Time taken for heap with array size 40000: 0.134893 seconds
Time taken for heap with array size 50000: 0.180476 seconds
Time taken for merge with array size 10000: 0.022274 seconds
Time taken for merge with array size 20000: 0.049554 seconds
Time taken for merge with array size 30000: 0.066838 seconds
Time taken for merge with array size 40000: 0.078811 seconds
Time taken for merge with array size 50000: 0.114833 seconds
30000           2.138090                0.035455                0.022274
Time taken for selection with array size 10000: 2.117332 seconds
Time taken for selection with array size 20000: 8.554374 seconds
Time taken for selection with array size 30000: 19.139061 seconds
Time taken for selection with array size 40000: 33.790865 seconds
Time taken for selection with array size 50000: 52.657812 seconds
Time taken for heap with array size 10000: 0.038900 seconds
Time taken for heap with array size 20000: 0.066378 seconds
Time taken for heap with array size 30000: 0.104236 seconds
Time taken for heap with array size 40000: 0.155688 seconds
Time taken for heap with array size 50000: 0.179741 seconds
Time taken for merge with array size 10000: 0.021273 seconds
Time taken for merge with array size 20000: 0.045176 seconds
Time taken for merge with array size 30000: 0.067881 seconds
Time taken for merge with array size 40000: 0.087283 seconds
Time taken for merge with array size 50000: 0.104556 seconds
40000           2.117332                0.038900                0.021273
Time taken for selection with array size 10000: 2.132756 seconds
Time taken for selection with array size 20000: 8.596784 seconds
Time taken for selection with array size 30000: 19.884348 seconds
Time taken for selection with array size 40000: 34.529967 seconds
Time taken for selection with array size 50000: 54.541523 seconds
Time taken for heap with array size 10000: 0.028595 seconds
Time taken for heap with array size 20000: 0.077899 seconds
Time taken for heap with array size 30000: 0.112904 seconds
Time taken for heap with array size 40000: 0.158112 seconds
Time taken for heap with array size 50000: 0.183108 seconds
Time taken for merge with array size 10000: 0.020345 seconds
Time taken for merge with array size 20000: 0.035091 seconds
Time taken for merge with array size 30000: 0.065100 seconds
Time taken for merge with array size 40000: 0.080938 seconds
Time taken for merge with array size 50000: 0.098093 seconds
50000           2.132756                0.028595                0.020345
"""

"""
Part B.2:
Selection Sort O(n^2): The time taken by selection sort increases quadratically with the size of the array. In the output,
the time taken significantly increases as the array size grows

Heap Sort O(n log n): In the output the time taken grows much more slowly compared to selection sort, indicating the logarithmic
growth consistent with its complexity

Merge Sort O(n log n): Merge sort has the same time complexity as Heap sort. In the output, the time taken is comparable, showing that
times are consistent with the time complexity of O(n log n)
"""
