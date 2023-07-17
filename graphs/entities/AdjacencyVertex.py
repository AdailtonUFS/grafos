from graphs.entities.Vertex import Vertex


class AdjacencyVertex(Vertex):
    def __init__(self, name, index):
        super().__init__(name, index)
        self.explored = False
