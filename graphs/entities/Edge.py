from graphs.entities.Vertex import Vertex


class Edge:

    def __init__(self, first_vertex:Vertex, second_vertex:Vertex):
        self.first_vertex = first_vertex
        self.second_vertex = second_vertex

    def is_loop(self):
        return self.first_vertex == self.second_vertex
