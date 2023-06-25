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

    def find_indices_by_edge(self, edge: Edge) -> list | bool:
        return self.repository.find_indices_by_edge(edge)

    def print_matrix(self):

        vertex_indexes_line = self.repository.matrix[0][1:]
        header = "  "

        for vertex_index in vertex_indexes_line:
            vertex = self.repository.vertices[vertex_index]
            header += " " + vertex.name

        print(header)

        for adjacencies in self.repository.matrix[1:]:
            if adjacencies[0]:
                vertex = self.repository.vertices[adjacencies[0]]
                adjacencies[0] = vertex.name
            print("  ".join(str(adjacency) for adjacency in adjacencies))

        print("Vértices:", len(self.repository.vertices))
        print("Arestas:", len(self.repository.edges))