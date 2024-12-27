from Node import Node
class BST:
    def __init__(self):
        self.root = None

    def put(self, new_val: int):
        """ Place a new node into the BST that contains int value 'new_val' """
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

    def get(self, val: int) -> int:
        """ Retrieve a node containing specified int value 'val' """
        def _get(curr: Node, val: int) -> int:
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

    def contains(self, val: int) -> bool:
        """ Check if node with specified int value 'val' is inside BST """
        def _contains(curr: Node, val: int) -> bool:
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
        """
        Remove the node containing specified int value 'val'.
        Nodes with two child nodes will be replaced by the inorder successor
        """
        curr = self.root
        parent = None

        # traverse through tree until node is either found or have traversed past leaf node
        while curr is not None and curr.val != val:
            parent = curr
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        if curr is None:
            return False

        if curr.left is not None and curr.right is not None:
            # node to remove has two child nodes... must replace with inorder successor
            successor = curr.right
            successor_parent = curr
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left
            curr.val = successor.val
            curr = successor
            parent = successor_parent

        subtree: Node
        if curr.left is None and curr.right is None:
            subtree = None
        elif curr.left is not None:
            subtree = curr.left
        else:
            subtree = curr.right

        if parent is None:
            self.root = subtree
        elif parent.left == curr:
            parent.left = subtree
        else:
            parent.right = subtree
            
        return True


    def height(self) -> int:
        """
        Calculate height of a BST object.
        An empty BST will have default height of -1 (therefore, BST with singular node has height of 0)
        """
        def _height(curr: Node):
            if curr is None:
                return -1
            else:
                L = _height(curr.left)
                R = _height(curr.right)
                return L + 1 if L > R else R + 1

        return 0 if self.size() == 1 else _height(self.root)

    def size(self) -> int:
        """ Calculate the total number of nodes in a BST object. """
        def _size(curr: Node) -> int:
            if curr is None:
                return 0
            else:
                L = _size(curr.left)
                R = _size(curr.right)
                return L + R + 1

        return _size(self.root)

    def sum(self) -> int:
        """ Calculate the sum of all node values in BST """
        def _sum(curr: Node) -> int:
            if curr is None:
                return 0
            else:
                left_sum = _sum(curr.left)
                right_sum = _sum(curr.right)
                return left_sum + right_sum + curr.val

        return _sum(self.root)

    def preorder(self) -> list:
        """ Return the preorder traversal of BST as a list """
        result = []

        def _preorder(curr: Node, preorder_list: list):
            if curr is None:
                return
            else:
                preorder_list.append(curr.val)
                _preorder(curr.left, preorder_list)
                _preorder(curr.right, preorder_list)

        _preorder(self.root, result)
        return result

    def inorder(self):
        """ Return the inorder traversal of BST as a list """
        result = []
        def _inorder(curr: Node, inorder_list: list):
            if curr is None:
                return
            else:
                _inorder(curr.left, inorder_list)
                inorder_list.append(curr.val)
                _inorder(curr.right, inorder_list)

        _inorder(self.root, result)
        return result

    def postorder(self):
        """ Return the postorder traversal of BST as a list """
        result = []
        def _postorder(curr: Node, postorder_list: list):
            if curr is None:
                return
            else:
                _postorder(curr.left, postorder_list)
                _postorder(curr.right, postorder_list)
                postorder_list.append(curr.val)

        _postorder(self.root, result)
        return result
