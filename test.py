from unittest import TestCase
from BST import BST

class TestPut(TestCase):
    def test_that_bst_is_none_upon_initialization(self):
        self.bst = BST()
        self.assertIsNone(self.bst)
        self.assertEqual(self.bst, None)
        self.assertEqual(self.bst.root, None)

    def test_putting_node_into_empty_bst(self):
        self.bst = BST()
        self.bst.put(10)
        self.assertIsNotNone(self.bst)

class TestGet(TestCase):
    pass

class TestContains(TestCase):
    pass

class TestRemove(TestCase):
    pass

class TestHeight(TestCase):
    pass

class TestSize(TestCase):
    pass

