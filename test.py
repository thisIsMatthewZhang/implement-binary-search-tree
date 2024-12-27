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
    def setUp(self):
        self.bst = BST()

    def test_height_of_empty_tree_is_negative_one(self):
        self.assertEqual(self.bst.height(), -1)

    def test_height_of_tree_with_one_node_is_zero(self):
        self.bst.put(29)
        self.assertEqual(self.bst.height(), 0)

    def test_height_of_tree_with_two_node_is_one(self):
        self.bst.put(38)
        self.bst.put(50)
        self.assertEqual(self.bst.height(), 1)

    def test_height_of_tree_with_longer_right_subtree(self):
        self.bst.put(17)
        self.bst.put(19)
        self.bst.put(16)
        self.bst.put(24)
        self.bst.put(91)
        self.bst.put(89)
        print(self.bst.preorder())
        self.assertEqual(self.bst.height(), 4)  # number of nodes 'n' in longest path is 5 -> height is n - 1

    def test_height_of_tree_with_longer_left_subtree(self):
        self.bst.put(34)
        self.bst.put(31)
        self.bst.put(22)
        self.bst.put(25)
        self.bst.put(39)
        self.bst.put(26)
        self.bst.put(17)
        self.bst.put(18)
        self.bst.put(20)
        print(self.bst.preorder())
        self.assertEqual(self.bst.height(), 5)  # number of nodes 'n' in longest path is 6 -> height is n - 1



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


class TestSum(TestCase):
    def test_sum_of_empty_tree_is_zero(self):
        self.bst = BST()
        self.assertEqual(self.bst.sum(), 0)

    def test_sum_of_tree_with_one_node_equals_value_of_that_node(self):
        self.bst = BST()
        self.bst.put(1)
        self.assertEqual(self.bst.sum(), 1)

    def test_sum_of_tree_with_more_than_one_node_is_correct(
            self):  # tree contains the values 5, 2, 8, 6, added in that order
        self.bst = BST()
        self.bst.put(5)
        self.bst.put(2)
        self.bst.put(8)
        self.bst.put(6)
        self.assertEqual(self.bst.sum(), 21)

    def test_sum_of_tree_with_only_left_branch(
            self):  # tree contains the values 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, added in that order
        self.bst = BST()
        for _ in range(20, 1, -2):
            self.bst.put(_)
        self.assertEqual(self.bst.sum(), 110)

    def test_sum_of_tree_with_only_right_branch(
            self):  # tree contains the values 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, added in that order
        self.bst = BST()
        for _ in range(1, 20, 2):
            self.bst.put(_)
        self.assertEqual(self.bst.sum(), 100)


class TestPreorder(TestCase):
    def test_empty_tree_returns_empty_list(self):
        self.bst = BST()
        empty_list = self.bst.preorder()
        self.assertEqual(empty_list, [])
        self.assertFalse(empty_list)

    def test_preorder_on_tree_with_one_node(self):
        self.bst = BST()
        self.bst.put(10)
        li = self.bst.preorder()
        self.assertEqual(li[0], 10)
        self.assertEqual(li, [10])

    def test_preorder_on_tree_with_several_nodes(self):
        self.bst = BST()
        for _ in range(5, 11):
            self.bst.put(_ * 2)
        for _ in range(5, 0, -1):
            self.bst.put(_ * 2)
        self.bst.put(9)
        self.bst.put(17)
        li = self.bst.preorder()
        self.assertEqual(li, [10, 8, 6, 4, 2, 9, 12, 14, 16, 18, 17, 20])


class TestInorder(TestCase):
    def test_empty_tree_returns_empty_list(self):
        self.bst = BST()
        empty_list = self.bst.inorder()
        self.assertEqual(empty_list, [])

    def test_inorder_on_tree_with_one_node(self):
        self.bst = BST()
        self.bst.put(12)
        li = self.bst.inorder()
        self.assertEqual(li, [12])
        self.assertEqual(li[0], 12)

    def test_inorder_on_tree_with_several_nodes(self):
        self.bst = BST()
        for _ in range(5, 11):
            self.bst.put(_ * 2)
        for _ in range(5, 0, -1):
            self.bst.put(_ * 2)
        self.bst.put(9)
        self.bst.put(17)
        li = self.bst.inorder()
        self.assertEqual(li, [2, 4, 6, 8, 9, 10, 12, 14, 16, 17, 18, 20])


class TestPostorder(TestCase):
    def test_empty_tree_returns_empty_list(self):
        self.bst = BST()
        empty_list = self.bst.postorder()
        self.assertEqual(empty_list, [])

    def test_postorder_on_tree_with_one_node(self):
        self.bst = BST()
        self.bst.put(12)
        li = self.bst.postorder()
        self.assertEqual(li, [12])
        self.assertEqual(li[0], 12)

    def test_postorder_on_tree_with_several_nodes(self):
        self.bst = BST()
        for _ in range(5, 11):
            self.bst.put(_ * 2)
        for _ in range(5, 0, -1):
            self.bst.put(_ * 2)
        self.bst.put(9)
        self.bst.put(17)
        li = self.bst.postorder()
        self.assertEqual(li, [2, 4, 6, 9, 8, 17, 20, 18, 16, 14, 12, 10])
