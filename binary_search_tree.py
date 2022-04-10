import unittest

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self, value):
        self.root = Node(value)
    
    def add_left(self, value, node):
        node.left = Node(value)
    
    def add_right(self, value, node):
        node.right = Node(value)
    
    def search(self, searchValue, node):
        if node is None or node.value == searchValue:
            return node
        elif searchValue < node.value:
            return self.search(searchValue, node.left)
        else: # searchValue > node.value
            return self.search(searchValue, node.right)
        
    def insert(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert(value, node.right)
    
    def __lift(self, node, nodeToDelete):
        if node.left:
            node.left = self.__lift(node.left, nodeToDelete)
            return node
        else:
            nodeToDelete.value = node.value
            return node.right
    
    def remove(self, value, node):
        if node is None:
            return None
        elif value < node.value:
            node.left = self.remove(value, node.left)
            return node
        elif value > node.value:
            node.right = self.remove(value, node.right)
            return node
        elif value == node.value:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.right = self.__lift(node.right, node)
                return node

class BinarySearchTreeTest(unittest.TestCase):
    def setUp(self):
        self.tree = BinarySearchTree(50)
    
    def test_root_value(self):
        tree = self.tree
        self.assertEqual(tree.root.value, 50)
    
    def test_add_left(self):
        tree = self.tree
        tree.add_left(25, tree.root)
        self.assertEqual(tree.root.left.value, 25)
    
    def test_add_right(self):
        tree = self.tree
        tree.add_right(75, tree.root)
        self.assertEqual(tree.root.right.value, 75)
    
    def test_search_exists(self):
        #      50
        #   25    75
        tree = self.tree
        tree.add_left(25, tree.root)
        tree.add_right(75, tree.root)
        node = tree.search(75, tree.root)
        self.assertEqual(node.value, 75)
    
    def test_search_not_exists(self):
        tree = self.tree
        tree.add_left(25, tree.root)
        tree.add_right(75, tree.root)
        node = tree.search(88, tree.root)
        self.assertIsNone(node)
    
    def test_insert_lowest_value(self):
        #      50
        #   25    75
        # 4
        # ^
        tree = self.tree
        tree.add_left(25, tree.root)
        tree.add_right(75, tree.root)
        tree.insert(4, tree.root)
        self.assertEqual(tree.root.left.left.value, 4)
    
    def test_remove_leaf_no_child(self):
        tree = self.tree
        tree.add_left(25, tree.root)
        tree.add_right(75, tree.root)
        tree.remove(75, tree.root)
        self.assertIsNone(tree.root.right)
    
    def tearDown(self):
        self.tree = None

if __name__ == "__main__":
    unittest.main()