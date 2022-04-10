from typing import List, Tuple
import unittest
import collections

def init_list(n) -> List[int]:
    return [0] * n

def init_grid_shallow(n_rows, n_cols) -> List[List[int]]:
    """
    Warning!
    Initialising a grid using shallow lists in Python can result in difficult
    to trace bugs. It is NOT recommended.
    Analyse the failed test case below: test_set_grid_single_value_shallow()
    Read more here:
    https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
    """
    grid = [[0] * n_cols] * n_rows
    return grid

def init_grid_list_comprehension(n_rows, n_cols) -> List[List[int]]:
    """
    This is the most succinct way to init grid array and it
    does NOT use shallow lists.
    """
    return [[0 for i in range(n_cols)] for j in range(n_rows)]

def init_grid(n_rows, n_cols) -> List[List[int]]:
    # This variant of init grid is probably the simplest to read.
    grid = []
    for _ in range(n_rows):
        row = []
        for _ in range(n_cols):
            row.append(0)
        grid.append(row)
    return grid

def is_within_bounds(grid, coords: Tuple[int, int]):
    x, y = coords
    X, Y = len(grid[0]) - 1, len(grid) - 1
    return (x >= 0 and x <= X) and (y >= 0 and y <= Y)

def has_tuple(a: List[Tuple[int, int]], t: Tuple[int, int]) -> bool:
    for _, v in enumerate(a):
        if v[0] == t[0] and v[1] == t[1]:
            return True
    return False

def is_valid(grid, pos: Tuple[int, int], visited):
    if not is_within_bounds(grid, pos):
        return False
    if has_tuple(visited, pos):
        return False
    return True

def bfs(grid):
    results = []
    # direction vectors
    directions = [ [-1, 0], [0, 1], [1, 0], [0, -1] ]
    
    visited = []
    queue = collections.deque()
    init_pos = (0, 0)
    queue.append(init_pos)
    visited.append(init_pos)
    while queue:
        pos = queue.popleft()
        x, y = pos[0], pos[1]
        results.append(grid[x][y])
        for dr, dc in directions:
            adjacent_pos = (x + dr, y + dc)
            if is_valid(grid, adjacent_pos, visited):
                queue.append(adjacent_pos)
                visited.append(adjacent_pos)
    return results
    
class GridArrayTest(unittest.TestCase):
    def test_list_zeros(self):
        expected = [0, 0, 0, 0]
        arr = init_list(4)
        self.assertEqual(arr, expected)
    
    def test_init_grid(self):
        expected = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        grid = init_grid(4, 4)
        self.assertEqual(grid, expected)
    
    # Caution!
    # See documentation under init_grid_shallow method above.
    def test_set_grid_single_value_shallow(self):
        expected = [
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        grid = init_grid_shallow(4, 4)
        grid[0][0] = 1
        self.assertNotEqual(grid, expected) # note the inequality.
        
    def test_set_grid_single_value(self):
        expected = [
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        grid = init_grid(4, 4)
        grid[0][0] = 1
        self.assertEqual(grid, expected)
        
    def test_is_within_bounds_in_bounds(self):
        grid = init_grid(4, 4)
        self.assertTrue(is_within_bounds(grid, (0,0)))
        
    def test_is_within_bounds_row_out_of_bounds(self):
        grid = init_grid(4, 4)
        self.assertFalse(is_within_bounds(grid, (-1, 0)))
        
    def test_is_within_bounds_col_out_of_bounds(self):
        grid = init_grid(4, 4)
        self.assertFalse(is_within_bounds(grid, (0, -1)))
        
    def test_has_tuple_valid(self):
        input_list: List[Tuple[int, int]] = [(0, 0), (1, 0), (2, 0), (2, 1)]
        t: Tuple[int, int] = (2, 1)
        self.assertTrue(has_tuple(input_list, t))
    
    def test_has_tuple_invalid(self):
        input_list = [(0, 0), (1, 0), (2, 0), (2, 1)]
        t = (3, 3)
        self.assertFalse(has_tuple(input_list, t))
        
    def test_is_valid_not_visited_not_in_bounds(self):
        grid = init_grid(4, 4)
        pos = (5, 5)
        visited = [(0, 0), (1, 0), (2, 0), (2, 1)]
        self.assertFalse(is_valid(grid, pos, visited))
        
    def test_is_valid_visited_in_bounds(self):
        grid = init_grid(4, 4)
        pos = (0, 0)
        visited = [(0, 0), (1, 0), (2, 0), (2, 1)]
        self.assertFalse(is_valid(grid, pos, visited))
    
    def test_is_valid_not_visited_in_bounds(self):
        grid = init_grid(4, 4)
        pos = (1, 1)
        visited = [(0, 0), (1, 0), (2, 0), (2, 1)]
        self.assertTrue(is_valid(grid, pos, visited))
    
    def test_grid_bfs(self):
        grid = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        expected = [1, 2, 5, 3, 6, 9, 4, 7, 10, 13, 8, 11, 14, 12, 15, 16]
        self.assertEqual(bfs(grid), expected)

if __name__ == '__main__':
    unittest.main()