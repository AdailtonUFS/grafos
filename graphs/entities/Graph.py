from abc import abstractmethod, ABC

from graphs.entities.Edge import Edge
from graphs.entities.Vertex import Vertex


class Graph(ABC):
    def __new__(cls, structure: str):
        if structure.lower() == "matriz":
            from graphs.entities.Matrix import Matrix
            return Matrix()
        elif structure.lower() == "estrutura de adjacência":
            from graphs.entities.AdjacencyStructure import AdjacencyStructure
            return AdjacencyStructure()
        else:
            return super().__new__(cls)


    @abstractmethod
    def add_vertex(self, vertex: Vertex) -> bool:
        pass

    @abstractmethod
    def add_edge(self, edge: Edge):
        pass

    @abstractmethod
    def remove_edge(self, edge: Edge):
        pass

    @abstractmethod
    def has_connection(self, first_index: int, second_index: int) -> bool:
        pass
    @abstractmethod
    def find_indices_by_edge(self, edge: Edge) -> list | bool:
        pass
    @abstractmethod

    def print(self):
        pass