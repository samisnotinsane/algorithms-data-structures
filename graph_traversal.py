"""
Graph search algorithms.

A testbed for traversing a small fully connected graph
(e.g. a social network) using the DFS and BFS graph searching algorithms.
"""
from typing import List
import collections
import unittest

def depth_first_search(graph, node, visited={}, result=[]) -> List[str]:
    visited[node] = 1
    result.append(node)
    for adjacent_node in graph[node]:
        if adjacent_node in visited:
            continue
        else:
            depth_first_search(graph, adjacent_node, visited)
    return result

def breadth_first_search(graph, node) -> List[str]:
    result = []
    visited = {}
    queue = collections.deque()
    visited[node] = 1
    result.append(node)
    queue.append(node)
    while queue:
        curr_node = queue.popleft()
        for adjacent_node in graph[curr_node]:
            if adjacent_node in visited:
                continue
            else:
                visited[adjacent_node] = 1
                result.append(adjacent_node)
                queue.append(adjacent_node)
    return result

class GraphTraversalTest(unittest.TestCase):
    def setUp(self):
        # graph represented by adjacency list
        self.network = {
            'Alice' : ['Bob', 'Candy', 'Derek', 'Elaine'],
            'Bob'   : ['Alice', 'Fred'],
            'Candy' : ['Alice', 'Helen'],
            'Derek' : ['Alice', 'Elaine', 'Gina'],
            'Elaine': ['Alice', 'Derek'],
            'Fred'  : ['Bob', 'Helen'],
            'Gina'  : ['Derek', 'Irena'],
            'Helen' : ['Fred', 'Candy'],
            'Irena' : ['Gina']
        }
    
    def test_depth_first_traversal(self):
        expected = \
            [
                'Alice', 'Bob', 'Fred',
                'Helen', 'Candy', 'Derek',
                'Elaine', 'Gina', 'Irena'
            ]
        self.assertEqual(depth_first_search(self.network, 'Alice'), expected)
        
    def test_breadth_first_traversal(self):
        expected = \
            [
                'Alice', 'Bob', 'Candy',
                'Derek', 'Elaine', 'Fred',
                'Helen', 'Gina', 'Irena'
            ]
        self.assertEqual(breadth_first_search(self.network, 'Alice'), expected)
    
    def tearDown(self):
        # reset graph
        self.network = None

if __name__ == '__main__':
    unittest.main()