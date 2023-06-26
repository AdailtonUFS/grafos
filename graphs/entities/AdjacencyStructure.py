from graphs.entities.Edge import Edge
from graphs.entities.Vertex import Vertex
from graphs.repositories.AdjacencyStructureRepository import AdjacencyStructureRepository


class AdjacencyStructure:

    def __init__(self):
        self.repository = AdjacencyStructureRepository()

    def add_vertex(self, vertex: Vertex) -> bool:
        return self.repository.add_vertex(vertex)

    def add_edge(self, edge: Edge):
        return self.repository.add_edge(edge)

    def remove_edge(self, edge: Edge):
        pass

    def has_connection(self, first_index: int, second_index: int) -> bool:
        pass

    def find_indices_by_edge(self, edge: Edge) -> list | bool:
        pass

    def print(self):
        return self.repository.print()
