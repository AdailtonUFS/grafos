import bisect
from typing import Union

from graphs.entities.Edge import Edge
from graphs.entities.Vertex import Vertex


class Matrix:

    def __init__(self, **kwargs):
        self.matrix: list[list[int]] = [[0]]
        self.vertices: dict = {}
        self.edges: list = []

    def add(self, vertex: Vertex) -> bool:

        if self.busca_vertice_na_matriz(vertex):
            return False

        position = self.encontrar_posicao_insercao(vertex.index)

        self.vertices[vertex.index] = vertex
        self.matrix[0].insert(position, vertex.index)
        self.matrix.insert(position, self.gerar_linha(vertex.index))
        self.reajuste_zeros()

        return True

    def conexao(self, edge: Edge):
        indexes = self.buscar_indices_por_aresta(edge)

        if not indexes:
            return False

        index_first_vertex, index_second_vertex = indexes
        adjacency = 2 if edge.is_loop() else 1

        self.matrix[index_first_vertex][index_second_vertex] += adjacency
        if index_first_vertex != index_second_vertex:
            self.matrix[index_second_vertex][index_first_vertex] += adjacency

        self.edges.append(edge)
        return True

    def remover_conexao(self, edge: Edge):
        indexes = self.buscar_indices_por_aresta(edge)

        if not indexes:
            return False

        index_first_vertex, index_second_vertex = indexes

        adjacency = 2 if edge.is_loop() else 1

        self.matrix[index_first_vertex][index_second_vertex] -= adjacency

        if index_first_vertex != index_second_vertex:
            self.matrix[index_second_vertex][index_first_vertex] -= adjacency
        # @TODO ao remover uma conexão remover a aresta da lista de edges
        return True

    def existe_conexao(self, first_index: int, second_index: int) -> bool:
        index_first_vertex_in_matrix = self.busca_indice_na_matriz(first_index)
        index_second_vertex_in_matrix = self.busca_indice_na_matriz(second_index)

        if index_first_vertex_in_matrix and index_second_vertex_in_matrix:
            return self.matrix[index_first_vertex_in_matrix][index_second_vertex_in_matrix] > 0 and \
                self.matrix[index_second_vertex_in_matrix][
                    index_first_vertex_in_matrix] > 0

        return False

    def buscar_indices_por_aresta(self, edge: Edge) -> Union[list, bool]:
        first_vertex = edge.first_vertex
        second_vertex = edge.second_vertex

        index_first_vertex_in_matrix = self.busca_vertice_na_matriz(first_vertex)
        index_second_vertex_in_matrix = self.busca_vertice_na_matriz(second_vertex)

        if index_first_vertex_in_matrix and index_second_vertex_in_matrix:
            return [index_first_vertex_in_matrix, index_second_vertex_in_matrix]

        return False

    def busca_vertice_na_matriz(self, vertex: Vertex) -> Union[int, bool]:
        vertex_indexes_line = self.matrix[0][1:]

        if not vertex_indexes_line:
            return False

        position = bisect.bisect_left(vertex_indexes_line, vertex.index)

        if position < len(vertex_indexes_line) and vertex_indexes_line[position] == vertex.index:
            return position + 1

        return False

    def busca_indice_na_matriz(self, index: int) -> Union[int, bool]:
        vertex_indexes_line = self.matrix[0][1:]

        if not vertex_indexes_line:
            return False

        position = bisect.bisect_left(vertex_indexes_line, index)

        if position < len(vertex_indexes_line) and vertex_indexes_line[position] == index:
            return position + 1

        return False

    def encontrar_posicao_insercao(self, index: int) -> int:
        vertex_indexes_line = self.matrix[0][1:]
        return bisect.bisect(vertex_indexes_line, index) + 1

    def matriz_representacao(self):
        header = "  "
        for vertex_index in self.matrix[0][1:]:
            vertex = self.vertices[vertex_index]
            header += " " + vertex.name
        print(header)

        for adjacencies in self.matrix[1:]:
            if adjacencies[0]:
                vertex = self.vertices[adjacencies[0]]
                adjacencies[0] = vertex.name
            print("  ".join(str(adjacency) for adjacency in adjacencies))

        print("Vértices", len(self.vertices))
        print("Arestas", len(self.edges))

    def gerar_zeros(self) -> list:
        if len(self.matrix[0]) < 2:
            return []

        n = len(self.matrix[0])
        return [0] * (n - 1)

    def gerar_linha(self, indice: int) -> list:
        line = self.gerar_zeros()
        line.insert(0, indice)
        return line

    def reajuste_zeros(self):
        vertex_indexes_line = self.matrix[0]
        index_count = len(vertex_indexes_line)
        for index, line in enumerate(self.matrix[1:], start=1):
            missing_zeros = index_count - len(line)
            line.extend(([0] * missing_zeros))

    def grau_vertice(self, index: int) -> int:
        vertex = self.busca_indice_na_matriz(index)
        if vertex is False:
            return False

        return sum(self.matrix[vertex][1:])
