from code_challenges.trees.binary_tree import BinaryTree
from code_challenges.trees.node import Node

def test_tree_is_empty():
    tree = BinaryTree()
    assert tree.find_max() is None

def test_tree_max():
    node = Node(1)
    node.left = Node(4)
    node.right = Node(3)
    tree = BinaryTree(node)
    assert tree.find_max() == 4

def test_tree_max_multiple_nodes():
    node = Node(8)
    node.left = Node(6)
    node.right = Node(7)
    node.left.left = Node(5)
    node.left.right = Node(3)
    node.right.left = Node(2)
    node.right.right = Node(9)
    tree = BinaryTree(node)
    assert tree.find_max() == 9
