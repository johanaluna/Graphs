"""
For this activity I'm going to use DFS because DFS goes to the children before goes to the neighbors
"""
from util import Stack, Queue  # These may come in handy
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # TODO
        self.vertices[vertex_id]=set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # TODO
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError('Error')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # TODO
        return self.vertices[vertex_id]
        



def earliest_ancestor(ancestors, starting_node):
    """
    Write a function that: 
    Given the dataset and the ID of an individual in the dataset,
        returns their earliest known ancestor – the one at the farthest distance from the input individual. 
        If there is more than one ancestor tied for "earliest",
            return the one with the lowest numeric ID.
        If the input individual has no parents, 
            the function should return -1.
    
    Test ancestors is list of pair
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    
    input: (earliest_ancestor(test_ancestors, 1)
    """
    # Instantiate my graph
    graph = Graph() 
    for (parent,child) in ancestors:
        print('ancestor',(parent,child) )
         # each element has a pair , add those elements to the vertex
        graph.add_vertex(parent)
        graph.add_vertex(child)
        # child to parent
    for (parent, child) in ancestors:
        # Add edges
        graph.add_edge(child, parent)
    # Create an empty stack
    stack = Stack()
    # Put the starting point in the stack
    stack.push([starting_node])
    # Make a set to keep track of vertices visited
    visited = set()
    
    earliest_ancestor_path = [starting_node]

    print('long0',earliest_ancestor_path)
    while stack.size() > 0:
        #pop first item
        path = stack.pop()
        vertex = path[-1]
        
        if vertex not in visited:
            print('vertex',vertex)
            visited.add(vertex)
            print('visited',visited)
            print('long1',earliest_ancestor_path)
            print('get neighbors',graph.get_neighbors(vertex))
            for deep_vertex in graph.get_neighbors(vertex):
                print('entre')
                new_path = path.copy()
                new_path.append(deep_vertex)
                print('new_path',new_path)
                stack.push(new_path)

                if len(earliest_ancestor_path) < len(new_path):
                    earliest_ancestor_path = new_path

                if len(earliest_ancestor_path) == len(new_path) and earliest_ancestor_path[-1] != new_path[-1]:
                    earliest_ancestor_path = new_path

    if earliest_ancestor_path[-1] == starting_node:
        return -1
    else: 
        return earliest_ancestor_path[-1]

# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# print(earliest_ancestor(test_ancestors, 3))                
    