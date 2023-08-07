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

    def subgraph_vertex_condition(self, vertices_subgraph: List[Vertex]) -> bool:
        for vertex_subgraph in vertices_subgraph:
            is_in_vertex_list = self.vertices.get(vertex_subgraph.index)
            if not is_in_vertex_list:
                return False

        return True

    def subgraph_edges_condition(self, edges: List[Edge]) -> bool:
        for edge in edges:
            has_edge = self.has_connection(edge.first_vertex.index, edge.second_vertex.index)
            if not has_edge:
                return False

        return True

    def is_subgraph(self, vertices_subgraph: List[Vertex], edges: List[Edge]) -> bool:
        vertex_in_graph = self.subgraph_vertex_condition(vertices_subgraph)
        edges_in_graph = self.subgraph_edges_condition(edges)

        return vertex_in_graph and edges_in_graph

    def generated_subgraph_from_vertices_and_edges(self, vertices: List[Vertex],
                                                   edges: List[Edge]):
        if not self.is_subgraph(vertices, edges):
            return False

        graph = AdjacencyStructureRepository()
        graph.add_vertices(vertices)
        graph.add_edges(edges)

        return graph

    def generated_subgraph_from_vertices(self, vertices: List[Vertex]):
        if not self.subgraph_vertex_condition(vertices):
            return False

        graph = AdjacencyStructureRepository()
        graph.add_vertices(vertices)

        adjacencies_created = []

        for vertex_i in vertices:
            adjacencies = self.find_vertex_in_structure_by_index(vertex_i.index)

            if not adjacencies:
                raise Exception(
                    "Unexpected error, find_vertex_in_structure_by_index method verify if vertex is in structure.")

            for adjacency in adjacencies:
                if adjacency in vertices:
                    edge = Edge(vertex_i, adjacency)
                    if edge not in adjacencies_created:
                        graph.add_edge(edge)
                        adjacencies_created.append(Edge(vertex_i, adjacency))

        return graph

    def print(self):
        print(Fore.LIGHTRED_EX + "ESTRUTURA DE ADJACÊNCIA", Style.RESET_ALL, end="\n")
        print()
        print(Fore.LIGHTRED_EX + "VÉRTICES", Style.RESET_ALL)

        for vertex in self.vertices.values():
            print(vertex.name, end=" ")

        print()
        print(Fore.LIGHTRED_EX + "GRAUS", Style.RESET_ALL)

        for index, adjacency in self.adjacency_structure.items():
            vertex = self.vertices.get(index)
            print("g(" + vertex.name + ")=" + str(len(adjacency)), end=", ")

        print("\n")
        print("Vértices:", len(self.vertices))
        print("Arestas:", self.edge_all_vertex())
        print()

        print(Fore.LIGHTRED_EX + "REPRESENTAÇÃO", Style.RESET_ALL, end="\n")

        for index, vertex_list in self.adjacency_structure.items():
            vertex = self.vertices.get(index)
            print("[", vertex.name, "]*->", end="")
            for neighbor in vertex_list:
                print("[", neighbor.name, "]->", end="")
            print()
