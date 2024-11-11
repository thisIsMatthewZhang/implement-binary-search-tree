from unittest import TestCase
from BST import BST

class TestPut(TestCase):
    def test_that_bst_is_none_upon_initialization(self):
        self.bst = BST()
        self.assertIsNone(self.bst.root)
        self.assertEqual(self.bst.root, None)

    def test_putting_node_into_empty_tree(self):
        self.bst = BST()
        self.bst.put(10)
        self.assertIsNotNone(self.bst)
        self.assertEqual(self.bst.root.val, 10)

    def test_putting_node_into_left_subtree(self):
        self.bst = BST()
        self.bst.put(15)
        self.assertIsNone(self.bst.root.left)
        self.bst.put(10)
        self.assertIsNotNone(self.bst.root.left)
        self.assertEqual(self.bst.root.val, 15)
        self.assertEqual(self.bst.root.left.val, 10)

    def test_putting_node_into_right_subtree(self):
        self.bst = BST()
        self.bst.put(10)
        self.assertIsNone(self.bst.root.right)
        self.bst.put(15)
        self.assertIsNotNone(self.bst.root.right)
        self.assertEqual(self.bst.root.val, 10)
        self.assertEqual(self.bst.root.right.val, 15)

    def test_putting_node_with_value_that_already_exists_in_tree(self):
        self.bst = BST()
        self.bst.put(20)
        self.bst.put(20)
        self.assertEqual(self.bst.root.val, 20)
        self.assertIsNone(self.bst.root.left)
        self.assertIsNone(self.bst.root.right)


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

