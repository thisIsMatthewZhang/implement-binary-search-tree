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
    def test_getting_empty_tree_returns_none(self):
        self.bst = BST()
        self.assertIsNone(self.bst.get(1))

    def test_getting_val_that_does_not_exist_in_tree_returns_none(self):
        self.bst = BST()
        self.bst.put(50)
        for _ in range(15, 100, 5):
            self.bst.put(_)
        self.assertIsNone(self.bst.get(100))
        self.assertIsNone(self.bst.get(10))
        self.assertIsNone(self.bst.get(-15))

    def test_getting_root_val(self):
        self.bst = BST()
        self.bst.put(10)
        self.assertEqual(self.bst.get(10), 10)
        self.assertEqual(self.bst.get(10), self.bst.root.val)

    def test_getting_val_from_left_subtree(self):
        self.bst = BST()
        self.bst.put(10)
        self.bst.put(5)
        self.bst.put(20)
        self.assertEqual(self.bst.get(5), 5)
        self.assertEqual(self.bst.get(5), self.bst.root.left.val)

    def test_getting_val_from_right_subtree(self):
        self.bst = BST()
        self.bst.put(10)
        self.bst.put(5)
        self.bst.put(20)
        self.assertEqual(self.bst.get(20), 20)
        self.assertEqual(self.bst.get(20), self.bst.root.right.val)

class TestContains(TestCase):
    def test_contains_returns_false_if_tree_is_empty(self):
        self.bst = BST()
        self.assertFalse(self.bst.contains(0))
        self.assertFalse(self.bst.contains(-5))

    def test_contains_returns_false_if_tree_does_not_contain_specified_val(self):
        self.bst = BST()
        self.bst.put(50)
        self.bst.put(51)
        self.assertFalse(self.bst.contains(52))
        self.assertFalse(self.bst.contains(49))

    def test_contains_returns_true_if_tree_does_contain_val(self):
        self.bst = BST()
        self.bst.put(50)
        for _ in range(15, 100, 5):
            self.bst.put(_)
        self.assertTrue(self.bst.contains(15))
        self.assertTrue(self.bst.contains(95))

class TestRemove(TestCase):
    pass

class TestHeight(TestCase):
    pass

class TestSize(TestCase):
    def test_size_of_empty_tree_returns_zero(self):
        self.bst = BST()
        self.assertEqual(self.bst.size(), 0)

    def test_tree_with_one_node_returns_one(self):
        self.bst = BST()
        self.bst.put(0)
        self.assertEqual(self.bst.size(), 1)

    def test_tree_with_ten_nodes_returns_ten(self):
        self.bst = BST()
        for _ in range(10):
            self.bst.put(_ * 3)
        self.assertEqual(self.bst.size(), 10)

    def test_tree_with_ten_nodes_returns_ten_after_putting_duplicate_vals(self):
        self.bst = BST()
        for _ in range(10):
            self.bst.put(_ * 3)
        self.bst.put(6)
        self.bst.put(21)
        self.assertEqual(self.bst.size(), 10)

class TestPreorder(TestCase):
    pass

class TestInorder(TestCase):
    pass

class TestPostorder(TestCase):
    pass





