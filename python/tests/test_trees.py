from code_challenges.trees.binary_tree import BinaryTree
from code_challenges.trees.node import Node

# can successfully intantiate a tree with a single root node
def test_new_node():
    node = Node(11)
    actual = node.value
    expected = 11
    assert actual == expected

def test_new_node_bad():
    node = Node(11)
    actual = node.value
    expected = 12
    assert actual != expected
# can succesfully instatiate an empty tree
def test_bt_empty():
    bt = BinaryTree()
    assert bt

def test_bt_empty_root_none():
    bt = BinaryTree()
    assert bt.root == None


def test_bt_left_right():

#           apple
#       /           \
#   pear          orange


    apple = Node('apple')
    pear = Node('pear')
    orange = Node('orange')

    bt = BinaryTree(apple)
    apple.left = pear
    apple.right = orange

    assert apple.left == bt.root.left
    assert apple.right == orange
    order_list = bt.pre_order()
    assert order_list == ['apple', 'pear', 'orange']

# For a Binary Search Tree, can successfully add a left child and right child properly to a node
# Can successfully return a collection from a preorder traversal
def test_pre_order_traversal():
    apple = Node('apple')
    apple.left = Node('pear')
    apple.right = Node('orange')
    bt = BinaryTree(apple)
    assert bt.post_order() == ['pear', 'orange', 'apple']

# Can successfully return a collection from an inorder traversal
def test_in_order_traversal():
    apple = Node('apple')
    apple.left = Node('pear')
    apple.right = Node('orange')
    bt = BinaryTree(apple)
    assert bt.in_order() == ['pear', 'apple', 'orange']

# Can successfully return a collection from a postorder traversal

def test_tree_max_empty():
    tree = BinaryTree()
    assert tree.find_max() is None

