import pytest
from graph import Graph
from graph_business_trip import business_trip

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

def test_breadth_first():
    test = Graph()
    node1 = test.add_node("A")
    node2 = test.add_node("B")
    node3 = test.add_node("C")
    node4 = test.add_node("D")
    node5 = test.add_node("E")
    test.add_edge(node1, node2)
    test.add_edge(node1, node3)
    test.add_edge(node2, node3)
    test.add_edge(node2, node4)
    test.add_edge(node3, node4)
    test.add_edge(node4, node5)
    assert test.breadth_first(node1) == ["A", "B", "C", "D", "E"]

def test_breadth_first_disconnected_vertex():
    test = Graph()
    node1 = test.add_node("A")
    node2 = test.add_node("B")
    node3 = test.add_node("C")
    node4 = test.add_node("D")
    test.add_edge(node2, node3)
    test.add_edge(node2, node4)
    test.add_edge(node3, node4)
    assert test.breadth_first(node1) == ["A"]

def test_breadth_one_node():
    test = Graph()
    node1 = test.add_node("A")
    assert test.breadth_first(node1) == ["A"]

def test_business_trip_two_vertex():
    test = Graph()
    node1 = test.add_node("A")
    node2 = test.add_node("B")
    node3 = test.add_node("C")
    node4 = test.add_node("D")
    node5 = test.add_node("E")
    test.add_edge(node1, node2, 1)
    test.add_edge(node1, node3, 2)
    test.add_edge(node2, node3, 3)
    test.add_edge(node2, node4, 4)
    test.add_edge(node3, node4, 5)
    test.add_edge(node4, node5, 6)
    path = ["A", "C"]
    assert business_trip(test, path) == 2

def test_business_trip_three():
    test = Graph()
    node1 = test.add_node("A")
    node2 = test.add_node("B")
    node3 = test.add_node("C")
    node4 = test.add_node("D")
    node5 = test.add_node("E")
    test.add_edge(node1, node2, 1)
    test.add_edge(node1, node3, 2)
    test.add_edge(node2, node3, 3)
    test.add_edge(node2, node4, 4)
    test.add_edge(node3, node4, 5)
    test.add_edge(node4, node5, 6)
    path = ["A", "B", "C"]
    assert business_trip(test, path) == 4

def test_business_trip_fail_two_vertex():
    test = Graph()
    node1 = test.add_node("A")
    node2 = test.add_node("B")
    node3 = test.add_node("C")
    node4 = test.add_node("D")
    node5 = test.add_node("E")
    test.add_edge(node1, node2, 1)
    test.add_edge(node1, node3, 2)
    test.add_edge(node2, node3, 3)
    test.add_edge(node2, node4, 4)
    test.add_edge(node3, node4, 5)
    test.add_edge(node4, node5, 6)
    path = ["A", "D"]
    assert business_trip(test, path) == None

def test_business_trip_fail_three_vertex():
    test = Graph()
    node1 = test.add_node("A")
    node2 = test.add_node("B")
    node3 = test.add_node("C")
    node4 = test.add_node("D")
    node5 = test.add_node("E")
    test.add_edge(node1, node2, 1)
    test.add_edge(node1, node3, 2)
    test.add_edge(node2, node3, 3)
    test.add_edge(node2, node4, 4)
    test.add_edge(node3, node4, 5)
    test.add_edge(node4, node5, 6)
    path = ["A", "B", "E"]
    assert business_trip(test, path) == None

def test_nonexistent_vertex():
    test = Graph()
    node1 = test.add_node("A")
    node2 = test.add_node("B")
    node3 = test.add_node("C")
    node4 = test.add_node("D")
    node5 = test.add_node("E")
    test.add_edge(node1, node2, 1)
    test.add_edge(node1, node3, 2)
    test.add_edge(node2, node3, 3)
    test.add_edge(node2, node4, 4)
    test.add_edge(node3, node4, 5)
    test.add_edge(node4, node5, 6)
    path = ["F", "A"]
    assert business_trip(test, path) == None