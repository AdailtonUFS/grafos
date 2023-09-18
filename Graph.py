from abc import abstractmethod, ABC

from Edge import Edge
from Vertex import Vertex


class Graph(ABC):
    def __new__(cls, structure: str):
        if structure.lower() == "matriz":
            from Matrix import Matrix
            return Matrix()
        elif structure.lower() == "estrutura de adjacência":
            from AdjacencyStructure import AdjacencyStructure
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
