from graphs.graphs import Vertex, Graph, Edge
def test_add_node():
    g = Graph()
    v = g.add_node('node')
    assert True

def test_add_edge():
    g = Graph()
    pb = g.add_node('pb')
    jam = g.add_node('jam')
    g.add_edge(pb, jam, 5)
    assert True


def test_collection():
    g = Graph()
    node_1 = g.add_node('one')
    node_2 = g.add_node('two')
    node_3 = g.add_node('three')
    expected = 3
    actual = len(g.get_node())
    assert actual == expected


def test_size():
    g = Graph()
    node1 = g.add_node('one')
    node2 = g.add_node('two')
    expected = 2
    actual = g.size()
    assert actual == expected


def test_mty():
    g = Graph()
    actual = g.get_node()
    expected = []
    assert actual == expected
