def business_trip(graph, cities):
    cost = 0
    for i in range(len(cities) - 1):
        for vertex in graph.get_nodes():
            if vertex.value == cities[i]:
                depart_node = vertex
                break
        else:
            return None
        for neighbor in graph.get_neighbor(depart_node):
            if neighbor.vertex.value == cities[i + 1]:
                cost += neighbor.weight
                break
        else:
            return None
    return cost

