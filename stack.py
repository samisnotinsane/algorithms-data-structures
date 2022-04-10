import unittest

def reverse(text:str) -> str:
    reversed_text = ""
    stack = Stack()
    for c in text:
        stack.push(c)
    while not stack.is_empty():
        c = stack.pop()
        reversed_text += c
    return reversed_text

class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, element):
        self.data.append(element)
    
    def pop(self):
        return self.data.pop()
    
    def is_empty(self):
        return len(self.data) == 0

class StackTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def test_push(self):
        stack = Stack()
        stack.push(0)
        self.assertEqual(stack.data[0], 0)
        return
    
    def test_pop(self):
        stack = Stack()
        stack.push(0)
        stack.push(1)
        self.assertEqual(stack.pop(), 1)
        return
    
    def test_pop_order(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        stack.push(6)
        self.assertEqual(stack.pop(), 6)
        self.assertEqual(stack.pop(), 5)
        return
    
    def test_is_empty_when_not_empty(self):
        stack = Stack()
        stack.push('c')
        self.assertFalse(stack.is_empty())
        return
    
    def test_is_empty_when_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        return
    
    def test_reverse(self):
        test_str = "abcde"
        self.assertEqual(reverse(test_str), "edcba")
        return
    
    def tearDown(self) -> None:
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()