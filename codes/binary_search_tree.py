import collections
import unittest


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, curr, value):
        if value > curr.val:
            if curr.right is None:
                curr.right = Node(value)
            else:
                self._insert(curr.right, value)
        elif value < curr.val:
            if curr.left is None:
                curr.left = Node(value)
            else:
                self._insert(curr.left, value)
        else:
            raise ValueError(f"The value {value} already exists in the BST.")

    def traverse(self, mode):
        if mode == "level":
            res = self._traverse_level_order()
        elif mode == "in":
            res = []
            self._traverse_in_order(res, self.root)
        else:
            raise NotImplementedError(f"The '{mode}' mode is not implemented yet.")
        return res

    def _traverse_level_order(self):
        if not self.root:
            return []

        dequeue = collections.deque([self.root])
        res = []

        while len(dequeue) > 0:
            node = dequeue.popleft()
            res.append(node.val)
            if node.left:
                dequeue.append(node.left)
            if node.right:
                dequeue.append(node.right)

        return res

    def _traverse_in_order(self, res, curr):
        if curr is None:
            return

        res.append(curr.val)
        self._traverse_in_order(res, curr.left)
        self._traverse_in_order(res, curr.right)


class BinarySearchTreeTests(unittest.TestCase):
    def test_create_empty_bst(self):
        bst = BinarySearchTree()
        self.assertIsNone(bst.root)

    def test_insert_first_element(self):
        bst = BinarySearchTree()
        bst.insert(1)
        self.assertEqual(bst.root.val, 1)
        self.assertEqual(bst.root.left, None)
        self.assertEqual(bst.root.right, None)

    def test_insert_second_element_bigger_than_root(self):
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(2)
        self.assertEqual(bst.root.val, 1)
        self.assertEqual(bst.root.left, None)
        self.assertEqual(bst.root.right.val, 2)
        self.assertEqual(bst.root.right.left, None)
        self.assertEqual(bst.root.right.right, None)

    def test_insert_second_element_smaller_than_root(self):
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(0)
        self.assertEqual(bst.root.val, 1)
        self.assertEqual(bst.root.right, None)
        self.assertEqual(bst.root.left.val, 0)
        self.assertEqual(bst.root.left.left, None)
        self.assertEqual(bst.root.left.right, None)

    def test_level_order_traversal_empty_tree(self):
        bst = BinarySearchTree()
        self.assertListEqual(bst.traverse(mode="level"), [])

    def test_level_order_traversal_one_node(self):
        bst = BinarySearchTree()
        bst.insert(10)
        self.assertListEqual(bst.traverse(mode="level"), [10])

    def test_level_order_traversal_multiple_nodes(self):
        bst = BinarySearchTree()
        nums = [10, 20, 5, 7, 25]
        for n in nums:
            bst.insert(n)
        self.assertListEqual(bst.traverse(mode="level"), [10, 5, 20, 7, 25])

    def test_in_order_traversal_empty_tree(self):
        bst = BinarySearchTree()
        self.assertListEqual(bst.traverse(mode="in"), [])

    def test_in_order_traversal_one_node(self):
        bst = BinarySearchTree()
        bst.insert(10)
        self.assertListEqual(bst.traverse(mode="in"), [10])

    def test_in_order_traversal_multiple_nodes(self):
        bst = BinarySearchTree()
        nums = [10, 20, 5, 7, 25]
        for n in nums:
            bst.insert(n)
        self.assertListEqual(bst.traverse(mode="in"), [10, 5, 7, 20, 25])


if __name__ == '__main__':
    unittest.main()
