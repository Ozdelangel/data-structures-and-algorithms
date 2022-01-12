from linked_list.linked_list import LinkedList, Node
import pytest
@pytest.mark.skip('pending')
def test_node_instance():
    node = Node(1, None)
    assert node.next == None
    assert node.value == 1
@pytest.mark.skip('pending')
def test_node_instance_fail():
    node = Node(1, None)
    assert node.next != node
    assert node.value != 2
@pytest.mark.skip('pending')
def test_linked_list():
    node = Node(1, None)
    ll = LinkedList(node)
    assert ll.head == node
@pytest.mark.skip('pending')
def linked_list_empty():
    ll = LinkedList()
    assert ll.head == None
@pytest.mark.skip('pending')
def test_linked_list_insert_to_empty():
    #  ll.head = apple
    ll = LinkedList()
    ll.insert('apple')
    assert ll.head.value == 'apple'
@pytest.mark.skip('pending')
def test_insert_to_linked_list():
    # ll
    # node 1
    # node2
    # ll.head = apple
    # apple.next = pear
    # pear.next = none
    # apple -> pear -> none
    ll = LinkedList()
    node1 = Node('apple')
    ll.head == node1
    node2 = Node('pear')
    node1.next = node2
    ll.insert('bananna')
    assert ll.head.value == 'bananna'

@pytest.mark.skip('pending')
def test_includes_linked_list_true():
    ll = LinkedList()
    node_true = Node(True)
    node_true = True
    assert node_true == True
@pytest.mark.skip('pending')

def test_import():
    assert LinkedList
