import unittest

class Array:
    def __init__(self, a=[]):
        self.arr = a
        
    def __str__(self):
        return str(self.arr)
        
    def insert(self, value):
        self.arr.append(value)
    
    def remove(self, value):
        self.arr.remove(value)
    
    def update(self, index, value):
        self.arr[index] = value
    
    def find(self, value):
        return self.arr.index(value)
    
    def copy(self, start_index, end_index):
        if start_index == 0 and end_index == (len(self.arr) - 1):
            return self.arr.copy()
        else:
            return self.arr[start_index:end_index]
    
    def sort(self):
        return sorted(self.arr)
    
    def reverse(self):
        return self.arr[::-1]
    
    def swap(self, index_a, index_b):
        self.arr[index_a], self.arr[index_b] = self.arr[index_b], self.arr[index_a]
    
    def filter(self, predicate_fn):
        return list(filter(predicate_fn, self.arr))
    
    def get_list(self):
        return self.arr

class ArrayTest(unittest.TestCase):    
    def test_insert(self):
        input_list, expected_list = [0, 10, 20], [0, 10, 20, 30]
        a = Array(input_list)
        a.insert(30)
        self.assertEqual(a.get_list(), expected_list)
    
    def test_remove(self):
        input_list, expected_list = [1, 2, 3], [1, 3]
        a = Array(input_list)
        a.remove(2)
        self.assertEqual(a.get_list(), expected_list)
    
    def test_update(self):
        input_list, expected_list = [1, 2, 3], [1, 5, 3]
        a = Array(input_list)
        a.update(1, 5)
        self.assertEqual(a.get_list(), expected_list)
    
    def test_find(self):
        input_list, expected_value = [25, 50, 75], 1
        a = Array(input_list)
        self.assertEqual(a.find(50), expected_value)
    
    def test_copy_full(self):
        input_list, expected_list = [25, 50, 75], [25, 50, 75]
        a = Array(input_list)
        self.assertEqual(a.copy(0, len(input_list)-1), expected_list)
    
    def test_copy_partial(self):
        input_list, expected_list = [1, 2, 3, 4, 5, 6, 7, 8, 9], [3, 4, 5, 6]
        a = Array(input_list)
        self.assertEqual(a.copy(2, 6), expected_list)
    
    def test_sort(self):
        input_list, expected_list = [22, 15, 17, 11, 18], [11, 15, 17, 18, 22]
        a = Array(input_list)
        self.assertEqual(a.sort(), expected_list)
    
    def test_reverse(self):
        input_list, expected_list = [3, 4, 5, 6], [6, 5, 4, 3]
        a = Array(input_list)
        self.assertEqual(a.reverse(), expected_list)
    
    def test_swap(self):
        input_list, expected_list = [3, 4, 5, 6], [3, 6, 5, 4]
        a = Array(input_list)
        a.swap(1, 3)
        self.assertEqual(a.get_list(), expected_list)
    
    def test_filter(self):
        input_list, expected_list = [1, 2, 3, 4], [2, 4]
        a = Array(input_list)
        def is_even(n):
            return True if n % 2 == 0 else False
        self.assertEqual(a.filter(is_even), expected_list)

if __name__ == '__main__':
    unittest.main()