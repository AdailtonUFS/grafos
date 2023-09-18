from Vertex import Vertex


class Edge:

    def __init__(self, first_vertex: Vertex, second_vertex: Vertex):
        self.first_vertex = first_vertex
        self.second_vertex = second_vertex

    def is_loop(self):
        return self.first_vertex == self.second_vertex

    def __eq__(self, other):
        if isinstance(other, Edge):
            return self.first_vertex == other.first_vertex and self.second_vertex == other.second_vertex
        return False
