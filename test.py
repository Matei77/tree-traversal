import unittest
from tree import Tree

class TestFindMethod(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        self.tree.add(1)
        self.tree.add(2)
        self.tree.add(3)
    
    def test_find1(self):
        self.assertNotEqual(self.tree.find(2), None)
        
    def test_find2(self):
        self.assertEqual(self.tree.find(4), None)