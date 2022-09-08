from data_structures.graph import Graph


def direct_flights(graph, cities):
    cost = 0

    for i in (0, len(cities) - 1):

        neighbor_vertexes = []
        nodes = set(graph.get_nodes())

        for edge in graph.get_neighbors(nodes(cities[i])):
            neighbor_vertexes.append(edge[cities[i]])

        if cities[i + 1] in neighbor_vertexes:
            routes = graph.get_neighbors(cities[i])
            cost += routes[cities[i + 1].weight]

