
from code_challenges.trees.node import Node
from code_challenges.trees.binary_tree import BinaryTree
from code_challenges.breadth_first.breadth_first import breadth_first

@pytest.mark.skip("pending")
def test_breadth_first():
    tree = BinaryTree()
    assert breadth_first(tree) == []
@pytest.mark.skip("pending")
def test_root():
    root = Node(2)
    tree = BinaryTree(root)
    assert breadth_first(tree) == [2]
@pytest.mark.skip("pending")
def test_left():
    root_1 = Node(1)
    root_1.left = Node(2)
    tree = BinaryTree(root_1)
    assert breadth_first(tree) == [1,2]
@pytest.mark.skip("pending")
def test_right():
    root_1 = Node(1)
    root_1.right = Node(3)
    tree = BinaryTree(root_1)
    assert breadth_first(tree) == [1,3]
@pytest.mark.skip("pending")
def actual_function_breadth_first():
    root_1 = Node(1)
    root_1.left = Node(4)
    root_1.right = Node(3)
    tree = BinaryTree(root_1)
    assert breadth_first(tree) == [1,4,3]
