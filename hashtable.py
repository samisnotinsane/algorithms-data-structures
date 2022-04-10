import unittest

class HashTable:
    def __init__(self, h={}):
        self.ht = h
        
    def __str__(self):
        return str(self.ht)
        
    def insert(self, key, value):
        if self.is_key_exists(key):
            self.ht[key] = value
        else:
            raise ValueError('Key already exists!')
    
    def find(self, key):
        return self.ht.get(key)
    
    def update(self, key, value):
        if self.is_key_exists(key):
            self.ht[key] = value
            return True
        else:
            return False
    
    def is_key_exists(self, key):
        return True if key in self.ht.keys() else False
    
    def is_value_exists(self, value):
        return True if value in self.ht.values() else False
    
    def delete(self, key):
        if self.is_key_exists(key):
            del self.ht[key]
            return True
        else:
            return False
    
class HashTableTest(unittest.TestCase):
    def test_insert_key_value_pair(self):
        h = HashTable()
        h.insert(0, 22)
        self.assertEqual(h.ht[0], 22)
    
    def test_find_value_for_key(self):
        h = HashTable()
        h.ht[0] = 22
        h.ht[1] = 25
        h.ht[2] = 27
        self.assertEqual(h.find(2), 27)
    
    def test_update_value_for_key(self):
        h = HashTable()
        h.ht[0] = 22
        h.ht[1] = 25
        h.ht[2] = 27
        h.update(1, 26)
        self.assertEqual(h.ht[1], 26)
    
    def test_check_if_key_exists(self):
        h = HashTable()
        h.ht[0] = 22
        h.ht[1] = 25
        h.ht[2] = 27
        self.assertTrue(h.is_key_exists(2))
        
    def test_check_if_value_exists(self):
        h = HashTable()
        h.ht[0] = 22
        h.ht[1] = 25
        h.ht[2] = 27
        self.assertTrue(h.is_value_exists(27))
    
    def test_loop_over_key_value_pairs(self):
        h = HashTable()
        h.ht[0] = 22
        h.ht[1] = 25
        h.ht[2] = 27
        self.assertEqual(str(h), '{0: 22, 1: 25, 2: 27}')
    
    def test_delete_key_value_pair(self):
        h = HashTable()
        h.ht[0] = 22
        h.ht[1] = 25
        h.ht[2] = 27
        h.delete(2)
        self.assertFalse(h.is_key_exists(2))

if __name__ == "__main__":
    unittest.main()