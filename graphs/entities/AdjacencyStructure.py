from graphs.entities.Edge import Edge
from graphs.entities.Vertex import Vertex


class AdjacencyStructure:
    def add_vertex(self, vertex: Vertex) -> bool:
        pass

    def add_edge(self, edge: Edge):
        pass

    def remove_edge(self, edge: Edge):
        pass

    def has_connection(self, first_index: int, second_index: int) -> bool:
        pass

    def find_indices_by_edge(self, edge: Edge) -> list | bool:
        pass

    def print(self):
        pass
