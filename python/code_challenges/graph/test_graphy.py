import pytest
from graph import Graph

def test_add_node():
    test = Graph()
    new_node = test.add_node("A")
    assert new_node.value == "A"

def test_add_edge_two_vertex():
    test = Graph()
    node1 = test.add_node("A")
    node2 = test.add_node("B")
    test.add_edge(node1, node2)
    assert test.adjacency_list[node1]
    assert test.get_neighbor(node1)[0].vertex.value == "B"
    assert test.adjacency_list[node2]
    assert test.get_neighbor(node2)[0].vertex.value == "A"

def test_get_nodes():
    test = Graph()
    node1 = test.add_node("A")
    node2 = test.add_node("B")
    node3 = test.add_node("C")
    all_nodes = test.get_nodes()
    assert len(all_nodes) == 3
    assert all_nodes[0].value == "A"
    assert all_nodes[1].value == "B"
    assert all_nodes[2].value == "C"

def test_get_neighbors():
    test = Graph()
    node1 = test.add_node("A")
    node2 = test.add_node("B")
    node3 = test.add_node("C")
    test.add_edge(node1, node2)
    test.add_edge(node1, node3)
    assert test.get_neighbor(node1)[0].vertex.value == "B"
    assert test.get_neighbor(node1)[1].vertex.value == "C"
    assert test.get_neighbor(node2)[0].vertex.value == "A"
    assert test.get_neighbor(node3)[0].vertex.value == "A"

def test_edge_weight():
    test = Graph()
    node1 = test.add_node("A")
    node2 = test.add_node("B")
    test.add_edge(node1, node2, 42)
    assert test.get_neighbor(node1)[0].vertex.value == "B"
    assert test.get_neighbor(node2)[0].vertex.value == "A"
    assert test.get_neighbor(node1)[0].weight == 42
    assert test.get_neighbor(node1)[0].weight == test.get_neighbor(node2)[0].weight

def test_size():
    test = Graph()
    node1 = test.add_node("A")
    node2 = test.add_node("B")
    node3 = test.add_node("C")
    assert test.size() == 3
    node4 = test.add_node("D")
    node5 = test.add_node("E")
    assert test.size() == 5

def test_add_edge_one_vertex_one_edge():
    test = Graph()
    new_node = test.add_node("A")
    assert new_node.value == "A"
    test.add_edge(new_node)
    assert test.adjacency_list[new_node]
    assert test.get_neighbor(new_node)[0].vertex == None

def test_add_edge_self_point():
    test = Graph()
    new_node = test.add_node("A")
    assert new_node.value == "A"
    test.add_edge(new_node, new_node)
    assert test.adjacency_list[new_node]
    assert test.get_neighbor(new_node)[0].vertex.value == "A"

def test_empty_graph():
    test = Graph()
    assert test.get_nodes() == []
    assert test.size() == 0
    assert test.get_neighbor() == None