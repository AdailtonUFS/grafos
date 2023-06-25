import bisect
from typing import Union

from graphs.entities.Edge import Edge
from graphs.entities.Vertex import Vertex


class MatrixRepository:
    def __init__(self):
        self.matrix: list[list[int]] = [[0]]
        self.vertices: dict = {}
        self.edges: list = []

    def add_vertex(self, vertex: Vertex) -> bool:
        if self._find_vertex_in_matrix(vertex):
            return False

        position = self._find_insertion_position(vertex.index)

        self.vertices[vertex.index] = vertex
        self.matrix[0].insert(position, vertex.index)
        self.matrix.insert(position, self._generate_row(vertex.index))
        self._adjust_zeros()

        return True

    def add_edge(self, edge: Edge):
        indexes = self.find_indices_by_edge(edge)

        if not indexes:
            return False

        index_first_vertex, index_second_vertex = indexes
        adjacency = 2 if edge.is_loop() else 1

        self.matrix[index_first_vertex][index_second_vertex] += adjacency
        if index_first_vertex != index_second_vertex:
            self.matrix[index_second_vertex][index_first_vertex] += adjacency

        self.edges.append(edge)
        return True

    def remove_edge(self, edge: Edge):
        indexes = self.find_indices_by_edge(edge)

        if not indexes:
            return False

        index_first_vertex, index_second_vertex = indexes

        adjacency = 2 if edge.is_loop() else 1

        self.matrix[index_first_vertex][index_second_vertex] -= adjacency

        if index_first_vertex != index_second_vertex:
            self.matrix[index_second_vertex][index_first_vertex] -= adjacency

        # @TODO ao remover uma conexão remover a aresta da lista de edges
        return True

    def has_connection(self, first_index: int, second_index: int) -> bool:
        index_first_vertex_in_matrix = self._find_index_in_matrix(first_index)
        index_second_vertex_in_matrix = self._find_index_in_matrix(second_index)

        if index_first_vertex_in_matrix and index_second_vertex_in_matrix:
            return (
                    self.matrix[index_first_vertex_in_matrix][index_second_vertex_in_matrix] > 0
                    and self.matrix[index_second_vertex_in_matrix][index_first_vertex_in_matrix] > 0
            )

        return False

    def find_indices_by_edge(self, edge: Edge) -> Union[list, bool]:
        first_vertex = edge.first_vertex
        second_vertex = edge.second_vertex

        index_first_vertex_in_matrix = self._find_vertex_in_matrix(first_vertex)
        index_second_vertex_in_matrix = self._find_vertex_in_matrix(second_vertex)

        if index_first_vertex_in_matrix and index_second_vertex_in_matrix:
            return [index_first_vertex_in_matrix, index_second_vertex_in_matrix]

        return False

    def _find_vertex_in_matrix(self, vertex: Vertex) -> Union[int, bool]:
        vertex_indexes_line = self.matrix[0][1:]

        if not vertex_indexes_line:
            return False

        position = bisect.bisect_left(vertex_indexes_line, vertex.index)

        if position < len(vertex_indexes_line) and vertex_indexes_line[position] == vertex.index:
            return position + 1

        return False

    def _find_index_in_matrix(self, index: int) -> Union[int, bool]:
        vertex_indexes_line = self.matrix[0][1:]

        if not vertex_indexes_line:
            return False

        position = bisect.bisect_left(vertex_indexes_line, index)

        if position < len(vertex_indexes_line) and vertex_indexes_line[position] == index:
            return position + 1

        return False

    def _find_insertion_position(self, index: int) -> int:
        vertex_indexes_line = self.matrix[0][1:]
        return bisect.bisect(vertex_indexes_line, index) + 1

    def _generate_zeros(self) -> list:
        if len(self.matrix[0]) < 2:
            return []

        n = len(self.matrix[0])
        return [0] * (n - 1)

    def _generate_row(self, index: int) -> list:
        row = self._generate_zeros()
        row.insert(0, index)
        return row

    def _adjust_zeros(self):
        vertex_indexes_line = self.matrix[0]
        index_count = len(vertex_indexes_line)
        for index, row in enumerate(self.matrix[1:], start=1):
            missing_zeros = index_count - len(row)
            row.extend(([0] * missing_zeros))
