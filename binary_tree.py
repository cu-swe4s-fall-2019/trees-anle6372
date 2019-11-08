"""
Library of classes that creates binary tree data structures without rebalancing strategies
class Node (self, key, value=None, left=None, right=None):
    Parameters
    ----------
    key: (required) type integer or float that represents the navigable index corresponding to that node
    value: (optional) data to be stored in Node
    left: (optional) child instance of Node with key less than or equal to parent key
    right: (optional) child instance of Node with key greater than parent key

    Functions
    ----------
    insert(root, key, value=None)
        parameters:
            root: (req) the parent root to be inserted as a child off of
            key: (req) the key to be attributed to the new node
            value: (optional) data to be stored in new child Node
        returns:
            root: return the parent root
    search(self, key):
        parameters:
            key: the key corresponding to the node
        returns: value corresponding to the given key
    Returns
    -------
    Tree: A unbalanced binary tree consisting of branched node objects
"""


class Node:
    def __init__(self, key, value=None, left=None, right=None):
        if key is None:
            raise ValueError('Node must have key attribute')
        try:
            key = float(key)
        except ValueError:
            raise ValueError(('key must be type supported by >, < and ='))
        except TypeError:
            raise TypeError(('key must be type supported by >, < and ='))

        self.key = key
        self.value = value
        self.left = left
        self.right = right

def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
    if lheight > rheight:
        return int(lheight + 1)
    else:
        return int(rheight + 1)


def insert(root, key, value=None):
    if key is None:
        raise ValueError('Inserted node must have key attribute')
    if root == None:
        root = Node(key, value=value)
        return root
    else:
        if type(root) is not Node:
            raise ValueError('Root must be a Node object')
        if key < root.key:
            if root.left == None:
                root.left = Node(key, value=value)
            else:
                insert(root.left, key, value=value)
        else:
            if root.right == None:
                root.right = Node(key, value=value)
            else:
                insert(root.right, key, value=value)
        return root

def search(node, key):
    if key is None:
        raise ValueError('Search must have key input')
    if type(node) is not Node:
        raise ValueError('Root must be a Node object')
    if node.key == key:
        return node.value
    if key > node.key:
        return search(node.right, key)
    else:
        return search(node.left, key)