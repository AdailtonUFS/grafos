from typing import Dict, List, Union

from colorama import Fore, Style

from graphs.entities.AdjacencyVertex import AdjacencyVertex
from graphs.entities.Edge import Edge
from graphs.entities.Vertex import Vertex


class AdjacencyStructureRepository:
    def __init__(self):
        self.vertices: Dict[int, AdjacencyVertex] = {}
        self.adjacency_structure: Dict[int, List[AdjacencyVertex]] = {}
        self.mark_vertices_structure = {}
        self.tree_edges = []
        self.return_edges = []

    def add_vertex(self, vertex: Vertex) -> bool:

        if self.find_vertex_in_structure_by_index(vertex.index):
            return False

        adjacency_vertex = AdjacencyVertex(vertex.name, vertex.index)

        self.adjacency_structure[adjacency_vertex.index] = []
        self.vertices[adjacency_vertex.index] = adjacency_vertex

    def add_vertices(self, vertices: List[Vertex]):
        for vertex in vertices:
            self.add_vertex(vertex)

    def find_vertex_in_structure_by_index(self, index: int) -> List[Vertex] | None:
        return self.adjacency_structure.get(index)

    def add_edge(self, edge: Edge) -> bool:
        first_vertex_in_structure = self.find_vertex_in_structure_by_index(edge.first_vertex.index)
        second_vertex_in_structure = self.find_vertex_in_structure_by_index(edge.second_vertex.index)

        if first_vertex_in_structure is None or second_vertex_in_structure is None:
            return False

        first_vertex_in_structure.append(edge.second_vertex)

        if first_vertex_in_structure != second_vertex_in_structure:
            second_vertex_in_structure.append(edge.first_vertex)

        return True

    def add_edges(self, edges: List[Edge]):
        for edge in edges:
            self.add_edge(edge)

    def remove_edge(self, edge):
        first_vertex_in_structure = self.find_vertex_in_structure_by_index(edge.first_vertex.index)
        second_vertex_in_structure = self.find_vertex_in_structure_by_index(edge.second_vertex.index)

        if first_vertex_in_structure is None or second_vertex_in_structure is None:
            return False

        is_removed_first_vertex = first_vertex_in_structure.remove(edge.second_vertex)
        is_removed_second_vertex = second_vertex_in_structure.remove(edge.first_vertex)

        if not is_removed_first_vertex or not is_removed_second_vertex:
            return False

        return True

    def has_connection(self, first_index: int, second_index: int) -> bool:
        first_vertex = self.vertices.get(first_index)
        second_vertex = self.vertices.get(second_index)

        adjacency_with_first_vertex = self.find_vertex_in_structure_by_index(first_index)
        adjacency_with_second_vertex = self.find_vertex_in_structure_by_index(second_index)
        second_is_in_first = second_vertex in adjacency_with_first_vertex
        first_is_in_second = first_vertex in adjacency_with_second_vertex

        return second_is_in_first and first_is_in_second

    def edge_all_vertex(self):
        quantity = 0
        for adjacency in self.adjacency_structure.values():
            quantity += len(adjacency)

        return int(quantity / 2)

    def deep_search(self, current_vertex: Vertex, previous_vertex: Union[Vertex | None] = None):

        if self.mark_vertices_structure.get(current_vertex.index) is None:
            print(current_vertex.name, "Visitado!")
            self.mark_vertices_structure[current_vertex.index] = True
            self.tree_edges.append(Edge(previous_vertex, current_vertex))
            for neighbor in self.adjacency_structure.get(current_vertex.index):
                self.deep_search(neighbor, previous_vertex)
        else:
            self.return_edges.append(Edge(previous_vertex, current_vertex))
            print(current_vertex.name, "Já estive nesse!")