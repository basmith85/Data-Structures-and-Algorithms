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

    def quicksort(self, low, high):
        if low < high:
            pi = self.partition(low, high)  # Partitioning index
            self.quicksort(low, pi - 1)  # Recursively sort elements before partition
            self.quicksort(pi + 1, high)  # Recursively sort elements after partition

    def partition(self, low, high):
        pivot_index = self.median_of_three(low, high)
        pivot_value = self.arr[pivot_index]
        self.arr[pivot_index], self.arr[high] = self.arr[high], self.arr[pivot_index]
        i = low - 1

        for j in range(low, high):
            if self.arr[j] < pivot_value:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        return i + 1

    def median_of_three(self, low, high):
        mid = (low + high) // 2
        candidates = [(low, self.arr[low]), (mid, self.arr[mid]), (high, self.arr[high])]
        candidates.sort(key=lambda x: x[1])
        return candidates[1][0]

    def radix_sort(self):
        if not self.arr:
            return

        max_num = max(self.arr)
        exp = 1

        while max_num // exp > 0:
            self.counting_sort(exp)
            exp *= 10

    def counting_sort(self, exp):
        n = len(self.arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = self.arr[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = self.arr[i] // exp
            output[count[index % 10] - 1] = self.arr[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(n):
            self.arr[i] = output[i]

# Test quick sorting technique
def is_sorted(arr):
    return arr == sorted(arr)

def test_quicksort():
    """Test the Quicksort algorithm"""
    seed_num = 43
    seed(seed_num)  # Set the seed for reproducibility
    sorting = Sorting(10)
    for _ in range(10):
        sorting.add(randint(1, 100))

    start_time = time.time()
    sorting.quicksort(0, len(sorting.arr) - 1)  # Apply the Quicksort algorithm
    end_time = time.time()

    print("Quick Sort:", "Passed!" if is_sorted(sorting.arr) else "Failed!")
    print("Execution Time:", end_time - start_time)

# Test case execution
test_quicksort()

# Test radix sorting technique
def test_radix_sort():
    # Test case 1
    arr1 = [234, 34, 34, 2, 1, 0, 2, 3422]
    sorting = Sorting(len(arr1))  # Create Sorting object with the same length as arr1
    sorting.arr = arr1  # Set the array in the sorting object
    sorting.radix_sort()  # Call radix_sort on the sorting object
    assert sorting.arr == [0, 1, 2, 2, 34, 34, 234, 3422], f"Test case 1 failed: {sorting.arr}"

    # Test case 2
    arr2 = [329, 457, 657, 839, 436, 720, 355]
    sorting = Sorting(len(arr2))
    sorting.arr = arr2
    sorting.radix_sort()
    assert sorting.arr == [329, 355, 436, 457, 657, 720, 839], f"Test case 2 failed: {sorting.arr}"

    # Test case 3
    arr3 = [1, 200, 3, 400, 5]
    sorting = Sorting(len(arr3))
    sorting.arr = arr3
    sorting.radix_sort()
    assert sorting.arr == [1, 3, 5, 200, 400], f"Test case 3 failed: {sorting.arr}"

    # Test case 4 (empty array)
    arr4 = []
    sorting = Sorting(len(arr4))
    sorting.arr = arr4
    sorting.radix_sort()
    assert sorting.arr == [], f"Test case 4 failed: {sorting.arr}"

    # Test case 5 (array with one element)
    arr5 = [42]
    sorting = Sorting(len(arr5))
    sorting.arr = arr5
    sorting.radix_sort()
    assert sorting.arr == [42], f"Test case 5 failed: {sorting.arr}"

    print("All test cases passed!")

# Run the test cases
test_radix_sort()
