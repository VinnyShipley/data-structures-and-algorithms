# Graphs

Graphs are a relational database that are a way to store different nodes, or vertices, connected with different connections, or edges.

## Challenge

Today's challenge was to create a file that would handle the construction and some other basic functions that the graph data structure should have

## Approach & Efficiency

For the functions contained within the graph, these are the Big O notations:

* add_node: The Big O for space would be O(1) because the method can only add one value which in turn creates only one new node. The Big O for time would be O(1) due to the fact that it is setting the value in a dictionary, so it doesn't have to cycle through the entire dictionary, it simply finds the index of the new vertex and places it there.

* add_edge: The Big O for space would be O(1) as you are only ever linking the two vertices together. This is essentially the same as finding the two nodes in the list, and then creating an edge between them, which at most amount of time would raise an error, but at most simply add the edge between the start and the end vertex. The Big O for space would also be O(1) due to the fact that at worst the edge is being created between the two vertices, which is going to be constant no matter what the vertices are.

* get_nodes: The Big O for space would be O(N) based on the fact that the returned list will be as long as however many vertices there are in the graph. Big O for time will be O(N) as well, as it will have to search through as many keys as there are vertices within the graph.

* get_neighbors: The big O for space would be 0(N) as the method is only designed to take one value in, the key, and then return however many vertices that particular vertex is connected to. The Big O for time would be O(1) due to the fact that the method is only seeking out one particular index within the adjacency_list, which will not be affected by how long the list is.

* size: Big O for space would be O(N) because the returned list will be exactly proportional to how many vertices are within the given graph. Big O for time would be O(1) because it is only looking for the one value of the entire list.


