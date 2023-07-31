from colorama import Fore, Style

from graphs.entities.Edge import Edge
from graphs.entities.Vertex import Vertex
from graphs.repositories.MatrixRepository import MatrixRepository


class Matrix:
    def __init__(self):
        self.repository = MatrixRepository()

    def add_vertex(self, vertex: Vertex) -> bool:
        return self.repository.add_vertex(vertex)

    def add_edge(self, edge: Edge):
        return self.repository.add_edge(edge)

    def remove_edge(self, edge: Edge):
        return self.repository.remove_edge(edge)

    def has_connection(self, first_index: int, second_index: int) -> bool:
        return self.repository.has_connection(first_index, second_index)

    def complete_graph(self, k: int):
        return self.repository.complete_graph(k)

    def k_regular_graph(self, n_vertex: int, k_degree: int):
        return self.repository.k_regular(n_vertex, k_degree)

    def print(self):

        print(Fore.LIGHTRED_EX + "VÉRTICES", Style.RESET_ALL)
        for vertex in self.repository.vertices.values():
            print(vertex.name, end=" ")
        print()
        print(Fore.LIGHTRED_EX + "GRAUS", Style.RESET_ALL)

        for index, vertex in self.repository.vertices.items():
            degree = self.repository.degree(index)
            if type(degree) is int:
                print("g(" + vertex.name + ")=" + str(degree), end=", ")
        print()
        print("Somatório do graus dos vértices:", len(self.repository.edges) * 2)

        print()
        print(Fore.LIGHTRED_EX + "ARESTAS", Style.RESET_ALL)
        for edge in self.repository.edges:
            print("aresta:", edge.first_vertex.name + edge.second_vertex.name)
        print()
        print("Vértices:", len(self.repository.vertices))
        print("Arestas:", len(self.repository.edges))

        vertex_indexes_line = self.repository.matrix[0][1:]
        header = "  "
        print()

        print(Fore.LIGHTRED_EX + "MATRIZ DE ADJACÊNCIA", Style.RESET_ALL, end="\n")

        for vertex_index in vertex_indexes_line:
            vertex = self.repository.vertices[vertex_index]
            header += " " + vertex.name

        print(header)

        for adjacencies in self.repository.matrix[1:]:
            if adjacencies[0] is not None:
                vertex = self.repository.vertices[adjacencies[0]]
                adjacencies[0] = vertex.name
            print("  ".join(str(adjacency) for adjacency in adjacencies))
