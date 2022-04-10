import unittest

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            if cur.next is None:
                break
            cur = cur.next
        return count
    
    def __str__(self):
        if self.head is None:        # when list is empty
            return '[]'
        final_str = ''
        cur = self.head
        final_str += '['
        while cur is not None:
            if cur == self.head:     # node is the head
                final_str += 'Ø<-'
            if cur.next is not None: # node is not the tail
                final_str = final_str + cur.data + '->'
            else:                    # node is the tail
                final_str = final_str + cur.data + '->Ø'
            cur = cur.next
        final_str += ']'
        return final_str
    
    def append(self, value):
        if self.head is None:       # when linked list is empty
            node = Node(value)
            self.head = node
        else:                       # when linked list is not empty
            node = Node(value)
            cur = self.head
            while cur.next:         # run pointer to tail
                cur = cur.next
            cur.next = node         # wire in new node
            node.prev = cur
    
    def prepend(self, value):
        node = Node(value)
        if self.head is None:       # when linked list is empty
            self.head = node
        else:                       # prepend to head
            self.head.prev = node
            node.next = self.head
            self.head = node
    
    def print_list(self):
        print(str(self))
        
    def add_after_node(self, key, value):
        cur = self.head
        while cur:                  # traverse to key
            if cur.data == key:
                break
            cur = cur.next
        if cur.next is None:        # add node after tail node
            node = Node(value)
            cur.next = node
            node.prev = cur
        else:                       # add node after non-tail node
            node = Node(value)
            node.next = cur.next
            node.prev = cur
            cur.next = node
    
    def add_before_node(self, key, value):
        if self.head.data == key:   # add node before head node
            node = Node(value)
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:                       # add node before non-head node
            prev = self.head
            cur = self.head.next
            while cur:              # traverse to key
                if cur.data == key:
                    break
                prev = cur
                cur = cur.next
            node = Node(value)
            prev.next = node
            node.prev = prev
            node.next = cur
            cur.prev = node
    
    def remove(self, key):
        if len(self) == 1 and key == self.head.data:      # case: only node present in list
            self.head = None
            return
        if key == self.head.data:                         # case: head node
            self.head.next.prev = None
            self.head = self.head.next
            return
        prev = self.head
        cur = self.head.next
        while cur:                                        # traverse to key
            if key == cur.data:
                break
            prev = cur
            cur = cur.next
        if cur.prev is not None and cur.next is not None: # case: non-head and non-tail node
            prev.next = cur.next
            cur.next.prev = prev
            cur.prev = None
            cur.next = None
            cur = None
            return
        if cur.next is None:                               # case: tail node
            prev.next = cur.next
            cur.prev = None
            cur.next = None
            cur = None
    
    def reverse(self):
        if len(self) == 1 or len(self) == 0:
            return
        temp = None
        cur = self.head
        while cur:
            # swap next and prev pointers of cur
            temp = cur.prev
            cur.prev = cur.next
            cur.next = temp
            cur = cur.prev
        self.head = temp.prev
    
    def remove_duplicates(self):
        dictionary = dict()
        cur = self.head
        while cur:
            print('current node:', cur.data)
            if cur.data in dictionary:
                print('current is already in dictionary, delete node')
                # remove node
                self.remove(cur.data)
            else:
                print('adding current to dictionary...')
                # add to dictionary
                dictionary[cur.data] = 1
            cur = cur.next

class DoublyLinkedListTest(unittest.TestCase):
    def setUp(self):
        self.dllist = DoublyLinkedList()
    
    def test_append(self):
        dll = self.dllist
        dll.append('A')
        self.assertEqual(dll.head.data, 'A')
    
    def test_len(self):
        dll = self.dllist
        self.assertEqual(len(dll), 0)
    
    def test_str(self):
        dll = self.dllist
        dll.append('A')
        dll.append('B')
        self.assertEqual(str(dll), '[Ø<-A->B->Ø]')
    
    def test_prepend(self):
        dll = self.dllist
        dll.append('B')
        dll.prepend('A')
        self.assertEqual(dll.head.data, 'A')
    
    def test_add_after_tail_node(self):
        dll = self.dllist
        dll.append('A')
        dll.append('B')
        dll.append('C')
        dll.add_after_node('C', 'c')
        self.assertEqual(dll.head.next.next.next.data, 'c')
    
    def test_add_after_non_tail_node(self):
        dll = self.dllist
        dll.append('A')
        dll.append('B')
        dll.add_after_node('A', 'a')
        self.assertEqual(dll.head.next.data, 'a')
    
    def test_add_before_head_node(self):
        dll = self.dllist
        dll.append('A')
        dll.add_before_node('A', '1')
        self.assertEqual(dll.head.data, '1')
    
    def test_add_before_non_head_node(self):
        dll = self.dllist
        dll.append('M')
        dll.append('5')
        dll.add_before_node('5', '2')
        self.assertEqual(dll.head.next.data, '2')
    
    def test_remove_case_only_node(self):
        dll = self.dllist
        dll.append('A')
        dll.remove('A')
        self.assertEqual(len(dll), 0)
    
    def test_remove_case_head_node(self):
        dll = self.dllist
        dll.append('A')
        dll.append('B')
        dll.remove('A')
        self.assertEqual(dll.head.data, 'B')
    
    def test_remove_case_non_head_non_tail_node(self):
        dll = self.dllist
        dll.append('A')
        dll.append('B')
        dll.append('C')
        dll.remove('B')
        self.assertEqual(len(dll), 2)
        self.assertEqual(dll.head.data, 'A')
        self.assertEqual(dll.head.next.data, 'C')
    
    def test_remove_case_tail_node(self):
        dll = self.dllist
        dll.append('A')
        dll.append('B')
        dll.append('C')
        dll.remove('C')
        self.assertEqual(len(dll), 2)
    
    def test_reverse(self):
        dll = self.dllist
        dll.append('A')
        dll.append('B')
        dll.append('C')
        dll.append('D')
        dll.reverse()
        self.assertEqual(dll.head.data, 'D')
        self.assertEqual(dll.head.next.data, 'C')
        self.assertEqual(dll.head.next.next.data, 'B')
        self.assertEqual(dll.head.next.next.next.data, 'A')
    
    def test_remove_duplicates(self):
        dll = self.dllist
        dll.append('1')
        dll.append('4')
        dll.append('7')
        dll.append('4')
        dll.remove_duplicates()
        dll.print_list()
    
    def tearDown(self):
        self.dllist = None

if __name__ == "__main__":
    unittest.main()