import unittest

class Queue:
    def __init__(self) -> None:
        self.data = []
    
    def enqueue(self, element) -> None:
        self.data.append(element)
    
    def dequeue(self) -> object:
        return self.data.pop(0)

class QueueTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def test_init(self):
        q = Queue()
        self.assertIsNotNone(q.data)
        
    def test_enqueue(self):
        q = Queue()
        q.enqueue(5)
        q.enqueue(9)
        q.enqueue(100)
        self.assertListEqual(q.data, [5, 9, 100])
        
    def test_dequeue(self):
        q = Queue()
        q.enqueue(5)
        q.enqueue(9)
        q.enqueue(100)
        q.dequeue()
        self.assertListEqual(q.data, [9, 100])

if __name__ == "__main__":
    unittest.main()