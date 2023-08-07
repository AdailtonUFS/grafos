import random
from typing import List
from colorama import Fore, Style

from graphs.entities.Edge import Edge
from graphs.entities.Vertex import Vertex
from graphs.repositories.AdjacencyStructureRepository import AdjacencyStructureRepository


class AdjacencyStructure:

    def __init__(self):
        self.repository = AdjacencyStructureRepository()

    def add_vertex(self, vertex: Vertex) -> bool:
        return self.repository.add_vertex(vertex)

    def add_vertices(self, vertices: List[Vertex]) -> bool:
        return self.repository.add_vertices(vertices)

    def add_edge(self, edge: Edge):
        return self.repository.add_edge(edge)

    def add_edges(self, edges: List[Edge]):
        return self.repository.add_edges(edges)

    def remove_edge(self, edge: Edge):
        return self.repository.remove_edge(edge)

    def has_connection(self, first_index: int, second_index: int) -> bool:
        return self.repository.has_connection(first_index, second_index)

    def test_deep(self):
        for i, boole in self.repository.mark_vertices_structure.items():
            print(i, "->", boole)

    def deep_search(self, vertex: Vertex) -> bool:
        # vertex = random.choice(list(self.repository.vertices.values()))
        self.repository.deep_search(vertex)
        return True

    def is_subgraph(self, vertices: List[Vertex], edges: List[Edge]):
        return self.repository.is_subgraph(vertices, edges)

    def generated_subgraph_from_vertices_and_edges(self, vertices: List[Vertex], edges: List[Edge]):
        return self.repository.generated_subgraph_from_vertices_and_edges(vertices, edges)

    def generated_subgraph_from_vertices(self, vertices: List[Vertex]):
        return self.repository.generated_subgraph_from_vertices(vertices)

    def print(self):
        print(Fore.LIGHTRED_EX + "ESTRUTURA DE ADJACÊNCIA", Style.RESET_ALL, end="\n")
        print()
        print(Fore.LIGHTRED_EX + "VÉRTICES", Style.RESET_ALL)

        for vertex in self.repository.vertices.values():
            print(vertex.name, end=" ")

        print()
        print(Fore.LIGHTRED_EX + "GRAUS", Style.RESET_ALL)

        for index, adjacency in self.repository.adjacency_structure.items():
            vertex = self.repository.vertices.get(index)
            print("g(" + vertex.name + ")=" + str(len(adjacency)), end=", ")

        print("\n")
        print("Vértices:", len(self.repository.vertices))
        print("Arestas:", self.repository.edge_all_vertex())
        print()

        print(Fore.LIGHTRED_EX + "REPRESENTAÇÃO", Style.RESET_ALL, end="\n")

        for index, vertex_list in self.repository.adjacency_structure.items():
            vertex = self.repository.vertices.get(index)
            print("[", vertex.name, "]*->", end="")
            for neighbor in vertex_list:
                print("[", neighbor.name, "]->", end="")
            print()

    def clean_print(self):
        print(Fore.LIGHTRED_EX + "ESTRUTURA DE ADJACÊNCIA", Style.RESET_ALL, end="\n")
        print()
        print(Fore.LIGHTRED_EX + "VÉRTICES", Style.RESET_ALL)

        for vertex in self.repository.adjacency_structure.values():
            print(vertex.name, end=" ")

        print("\n")
        print("Vértices:", len(self.repository.adjacency_structure))
        print("Arestas:", self.repository.edge_all_vertex())
        print()
        print(Fore.LIGHTRED_EX + "REPRESENTAÇÃO", Style.RESET_ALL, end="\n")
        for _, vertex in self.repository.adjacency_structure.items():
            if vertex.explored is True:
                print(Fore.LIGHTGREEN_EX)
            else:
                print(Style.RESET_ALL)

            print("[", vertex.name, "]*->", end="")
            for neighbor_list in vertex.neighbors.values():
                for i, neighbor in enumerate(neighbor_list):
                    print("[", neighbor.name, "]->", end="")
            print()
