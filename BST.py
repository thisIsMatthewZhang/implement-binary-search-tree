from Node import Node
class BST:
    def __init__(self):
        self.root = None

    def put(self, new_val: int):
        if self.root is None:
            new_node = Node(new_val)
            self.root = new_node
            return

        def _put(curr: Node, new_val: int):
            if curr.val == new_val:
                return
            # insert new node into left subtree
            elif new_val < curr.val:
                if curr.left is None:
                    new_node = Node(new_val)
                    curr.left = new_node
                else:
                    _put(curr.left, new_val)
            # insert new node into right subtree
            elif new_val > curr.val:
                if curr.right is None:
                    new_node = Node(new_val)
                    curr.right = new_node
                else:
                    _put(curr.right, new_val)

        _put(self.root, new_val)

    def get(self, val: int):

        def _get(curr: Node, val: int):
            if curr is None:
                return None
            # val is found in tree
            elif curr.val == val:
                return curr.val
            # val is in left subtree if it exists
            elif val < curr.val:
                return _get(curr.left, val)
            # val is in right subtree if it exists
            elif val > curr.val:
                return _get(curr.right, val)

        return _get(self.root, val)

    def contains(self, val: int):
        def _contains(curr: Node, val: int):
            if curr is None:
                return False
            # val is found in tree
            elif curr.val == val:
                return True
            # val is in left subtree if it exists
            elif val < curr.val:
                return _contains(curr.left, val)
            # val is in right subtree if it exists
            elif val > curr.val:
                return _contains(curr.right, val)

        return _contains(self.root, val)

    def remove(self, val: int):
        pass

    def height(self):
        pass

    def size(self):
        pass