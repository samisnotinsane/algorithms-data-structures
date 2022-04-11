import unittest

class SortableArray:
    def __init__(self, array):
        self.array = array
    
    def partition(self, left_pointer, right_pointer):
        pivot_pointer = right_pointer
        right_pointer -= 1
        while True:
            while self.array[left_pointer] < self.array[pivot_pointer]:
                left_pointer += 1

            while self.array[right_pointer] >= self.array[pivot_pointer]:
                right_pointer -= 1
                
            if left_pointer >= right_pointer:
                break
            else:
                self.array[left_pointer], self.array[right_pointer] = self.array[right_pointer], self.array[left_pointer]
                left_pointer += 1
        self.array[left_pointer], self.array[pivot_pointer] = self.array[pivot_pointer], self.array[left_pointer]
        return left_pointer # this should be the pivot by the time partition is complete
    
    def quick_sort(self, left_index, right_index):
        if right_index - left_index <= 0:
            return
        
        # locate the pivot
        pivot_index = self.partition(left_index, right_index)
        
        # recursively quick sort subarray to the left of pivot
        self.quick_sort(left_index, pivot_index-1)
        
        # recursively quick sort subarray to the right of pivot
        self.quick_sort(pivot_index+1, right_index)

class SortingTest(unittest.TestCase):    
    def test_partition(self):
        array = [0, 5, 2, 1, 6, 3]
        sortable_array = SortableArray(array)
        pivot = sortable_array.partition(0, len(array)-1)
        self.assertEqual(pivot, 3)
    
    def test_quick_sort(self):
        array = [1, 6, 3, 4, 5, 2, 7]
        sortable_array = SortableArray(array)
        sortable_array.quick_sort(0, len(array)-1)
        self.assertEqual(sortable_array.array, sorted(array))

if __name__ == '__main__':
    unittest.main()