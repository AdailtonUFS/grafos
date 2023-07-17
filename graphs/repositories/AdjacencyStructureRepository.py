from typing import Dict, List
from colorama import Fore, Style

from graphs.entities.AdjacencyVertex import AdjacencyVertex
from graphs.entities.Edge import Edge
from graphs.entities.Vertex import Vertex


class AdjacencyStructureRepository:
    def __init__(self):
        self.adjacency_structure: Dict[int, AdjacencyVertex] = {}

    def add_vertex(self, vertex: Vertex) -> bool:

        if self.find_vertex_in_structure_by_index(vertex.index):
            return False

        adjacency_vertex = AdjacencyVertex(vertex.name, vertex.index)

        self.adjacency_structure[adjacency_vertex.index] = adjacency_vertex

    def add_vertices(self, vertices: List[Vertex]) -> bool:
        for vertex in vertices:
            if self.find_vertex_in_structure_by_index(vertex.index):
                return False

            adjacency_vertex = AdjacencyVertex(vertex.name, vertex.index)

            self.adjacency_structure[adjacency_vertex.index] = adjacency_vertex

    def find_vertex_in_structure_by_index(self, index: int) -> AdjacencyVertex | None:
        return self.adjacency_structure.get(index)

    def add_edge(self, edge: Edge) -> bool:
        first_vertex_in_structure = self.find_vertex_in_structure_by_index(edge.first_vertex.index)
        second_vertex_in_structure = self.find_vertex_in_structure_by_index(edge.second_vertex.index)

        if first_vertex_in_structure is None or second_vertex_in_structure is None:
            return False

        first_vertex_in_structure.add_neighbor(second_vertex_in_structure)

        if first_vertex_in_structure != second_vertex_in_structure:
            second_vertex_in_structure.add_neighbor(first_vertex_in_structure)

        return True

    def remove_edge(self, edge):
        first_vertex_in_structure = self.find_vertex_in_structure_by_index(edge.first_vertex.index)
        second_vertex_in_structure = self.find_vertex_in_structure_by_index(edge.second_vertex.index)

        if first_vertex_in_structure is None or second_vertex_in_structure is None:
            return False

        is_removed_first_vertex = first_vertex_in_structure.remove_neighbor(second_vertex_in_structure)
        is_removed_second_vertex = second_vertex_in_structure.remove_neighbor(first_vertex_in_structure)

        if not is_removed_first_vertex or not is_removed_second_vertex:
            return False

        return True

    def has_connection(self, first_index: int, second_index: int) -> bool:
        first_adjacency_vertex = self.find_vertex_in_structure_by_index(first_index)
        second_adjacency_vertex = self.find_vertex_in_structure_by_index(second_index)

        return first_adjacency_vertex.is_neighbor(second_adjacency_vertex)

    def edge_all_vertex(self):
        quantity = 0
        for vertex in self.adjacency_structure.values():
            quantity += vertex.edges_quantity()

        return int(quantity / 2)

    def deep_search(self):
        for vertex in self.adjacency_structure.values():
            if not vertex.explored:
                vertex.explored = True

            neighbor: AdjacencyVertex
            for neighbor_list in vertex.neighbors.values():
                for i, neighbor in enumerate(neighbor_list):
                    if not neighbor.explored:
                        vertex.explored = True
