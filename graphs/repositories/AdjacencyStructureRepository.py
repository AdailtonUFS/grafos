from typing import Dict

from graphs.entities.AdjacencyVertex import AdjacencyVertex
from graphs.entities.Edge import Edge
from graphs.entities.Vertex import Vertex


class AdjacencyStructureRepository:
    def __init__(self):
        self.adjacency_structure: Dict[int,AdjacencyVertex] = {}

    def add_vertex(self, vertex:Vertex) -> bool:

        if self.find_vertice_in_structure_by_index(vertex.index):
            return False

        adjancecy_vertex = AdjacencyVertex(vertex.name, vertex.index)

        self.adjacency_structure[adjancecy_vertex.index] = adjancecy_vertex

    def find_vertice_in_structure_by_index(self, index:int) -> AdjacencyVertex | None:
        return self.adjacency_structure.get(index)

    def add_edge(self, edge: Edge) -> bool:
        first_vertice_in_structure = self.find_vertice_in_structure_by_index(edge.first_vertex.index)
        second_vertice_in_structure = self.find_vertice_in_structure_by_index(edge.second_vertex.index)

        if first_vertice_in_structure is None or second_vertice_in_structure is None:
            return False

        first_vertice_in_structure.add_neighbors(second_vertice_in_structure)
        second_vertice_in_structure.add_neighbors(first_vertice_in_structure)

    def print(self):
        for _, vertex in self.adjacency_structure.items():
            print("[", vertex.name, "]*->", end="")
            for neighbor_list in vertex.neighbors.values():
                for i, neighbor in enumerate(neighbor_list):
                    print("[", neighbor.name, "]->", end="")
            print()
