"""Unittesting framework for binary_tree.py
Parameters
----------
None
Returns
-------
None
"""

import unittest
import binary_tree as bt
import random as rdm


# Testing none input
class TestNoneInput(unittest.TestCase):

    def test_none_node(self):
        self.assertRaises(ValueError, lambda: bt.Node(None, None))
        tree = bt.Node(7, None)
        self.assertEqual(None, tree.value)

    def test_none_insert_root(self):
        tree = bt.insert(None, 7, 4)
        self.assertEqual(tree.key, 7)
        self.assertEqual(tree.value, 4)

    def test_none_insert_key(self):
        root = bt.Node(7, 4)
        self.assertRaises(ValueError, lambda: bt.insert(root, None, 7))

    def test_none_insert_value(self):
        root = bt.Node(7, 4)
        root = bt.insert(root, 8, None)
        self.assertEqual(root.right.key, 8)


# Testing incorrect type input
class TestIncorrectInput(unittest.TestCase):
    def test_incorrect_node(self):
        self.assertRaises(ValueError, lambda: bt.Node('hi', None))
        self.assertRaises(TypeError, lambda: bt.Node([], None))

    def test_incorrect_insert(self):
        self.assertRaises(ValueError, lambda: bt.insert('hi', 5))
        self.assertRaises(ValueError, lambda: bt.insert(7, 5))
        self.assertRaises(ValueError, lambda: bt.insert(float(420.69), 5))
        self.assertRaises(ValueError, lambda: bt.insert([], 5))
        root = None
        self.assertRaises(ValueError, lambda: bt.insert(root, 'hi'))
        self.assertRaises(TypeError, lambda: bt.insert(root, []))

    def test_incorrect_search(self):
        self.assertRaises(ValueError, lambda: bt.search(7, 5))
        self.assertRaises(ValueError, lambda: bt.search(float(420.69), 5))
        self.assertRaises(ValueError, lambda: bt.search([], 5))


# Test correct input
class TestCorrectInput(unittest.TestCase):

    def test_correct_insert(self):
        for i in range(1000):
            root = None
            node_1_key = rdm.randint(1, 1000)
            node_1_value = rdm.randint(1, 1000)
            node_2_key = rdm.randint(1, 1000)
            node_2_value = rdm.randint(1, 1000)
            node_3_key = rdm.randint(1, 1000)
            node_3_value = rdm.randint(1, 1000)
            root = bt.insert(root, node_1_key, node_1_value)
            bt.insert(root, node_2_key, node_2_value)
            bt.insert(root, node_3_key, node_3_value)
            keylist = [node_1_key, node_2_key, node_3_key]
            if len(keylist) > len(set(keylist)):
                continue
            if node_2_key > node_1_key:
                self.assertEqual(root.right.key, node_2_key)
                self.assertEqual(root.right.value, node_2_value)
                if node_3_key > node_1_key:
                    if node_3_key > node_2_key:
                        self.assertEqual(root.right.right.key, node_3_key)
                        self.assertEqual(root.right.right.value, node_3_value)
                    else:
                        self.assertEqual(root.right.left.key, node_3_key)
                        self.assertEqual(root.right.left.value, node_3_value)
                else:
                    self.assertEqual(root.left.key, node_3_key)
                    self.assertEqual(root.left.value, node_3_value)
            else:
                self.assertEqual(root.left.key, node_2_key)
                self.assertEqual(root.left.value, node_2_value)
                if node_3_key > node_1_key:
                    self.assertEqual(root.right.key, node_3_key)
                    self.assertEqual(root.right.value, node_3_value)
                else:
                    if node_3_key > node_2_key:
                        self.assertEqual(root.left.right.key, node_3_key)
                        self.assertEqual(root.left.right.value, node_3_value)
                    else:
                        self.assertEqual(root.left.left.key, node_3_key)
                        self.assertEqual(root.left.left.value, node_3_value)

    def test_correct_search(self):
        for i in range(100):
            root = None
            node_1_key = rdm.randint(1, 1000)
            node_1_value = rdm.randint(1, 1000)
            node_2_key = rdm.randint(1, 1000)
            node_2_value = rdm.randint(1, 1000)
            node_3_key = rdm.randint(1, 1000)
            node_3_value = rdm.randint(1, 1000)
            root = bt.insert(root, node_1_key, node_1_value)
            bt.insert(root, node_2_key, node_2_value)
            bt.insert(root, node_3_key, node_3_value)
            self.assertEqual(bt.search(root, node_1_key), node_1_value)
            self.assertEqual(bt.search(root, node_2_key), node_2_value)
            self.assertEqual(bt.search(root, node_3_key), node_3_value)


if __name__ == '__main__':
    unittest.main()
