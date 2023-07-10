from colorama import Fore, Style

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
        return self.repository.remove_edge(edge)

    def has_connection(self, first_index: int, second_index: int) -> bool:
        return self.repository.has_connection(first_index, second_index)

    def print(self):
        print(Fore.LIGHTRED_EX + "ESTRUTURA DE ADJACÊNCIA", Style.RESET_ALL, end="\n")
        print()
        print(Fore.LIGHTRED_EX + "VÉRTICES", Style.RESET_ALL)

        for vertex in self.repository.adjacency_structure.values():
            print(vertex.name, end=" ")

        print()
        print(Fore.LIGHTRED_EX + "GRAUS", Style.RESET_ALL)

        for vertex in self.repository.adjacency_structure.values():
            print("g(" + vertex.name + ")=" + str(vertex.edges_quantity()), end=", ")

        print("\n")
        print("Vértices:", len(self.repository.adjacency_structure))
        print("Arestas:", self.repository.edge_all_vertex())
        print()
        print(Fore.LIGHTRED_EX + "REPRESENTAÇÃO", Style.RESET_ALL, end="\n")
        for _, vertex in self.repository.adjacency_structure.items():
            print("[", vertex.name, "]*->", end="")
            for neighbor_list in vertex.neighbors.values():
                for i, neighbor in enumerate(neighbor_list):
                    print("[", neighbor.name, "]->", end="")
            print()
