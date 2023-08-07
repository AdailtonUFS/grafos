from typing import List, Union

from graphs.entities.AdjacencyStructure import AdjacencyStructure
from graphs.entities.Edge import Edge
from graphs.entities.Vertex import Vertex
from graphs.repositories.AdjacencyStructureRepository import AdjacencyStructureRepository


class SubgraphRepository:
    def __init__(self, adjacency_structure: AdjacencyStructureRepository):
        self.adjacency_structure = adjacency_structure

    def _check_equals_vertices(self, vertices: List[Vertex]) -> bool:
        vertices_keys = set(vertex.index for vertex in vertices)
        vertices_graph = set(self.adjacency_structure.adjacency_structure.keys())

        return vertices_keys == vertices_graph

    def _check_vertices(self, vertices: List[Vertex]) -> bool:
        vertices_keys = set(vertex.index for vertex in vertices)
        vertices_graph = set(self.adjacency_structure.adjacency_structure.keys())

        return vertices_keys.issubset(vertices_graph)

    def _check_edges(self, edges: List[Edge]) -> bool:
        return all(
            self.adjacency_structure.has_connection(edge.first_vertex.index, edge.second_vertex.index) for edge in
            edges)


    def _validate(self, vertices: List[Vertex], edges: List[Edge]) -> bool:
        adjacency_structure_contain_vertices = self._check_vertices(vertices)
        adjacency_structure_contain_edges = self._check_edges(edges)

        return adjacency_structure_contain_vertices and adjacency_structure_contain_edges

    def proper(self, vertices: List[Vertex], edges: List[Edge]) -> Union[AdjacencyStructure | bool]:

        if not self._validate(vertices, edges):
            return False

        graph = AdjacencyStructure()
        graph.add_vertices(vertices)
        graph.add_edges(edges)

        return graph

    def induced(self, vertices: List[Vertex]):
        if not self._check_vertices(vertices):
            return False

        graph = AdjacencyStructure()
        graph.add_vertices(vertices)

        adjacencies_created = []

        for vertex_i in vertices:
            adjacencies = self.adjacency_structure.find_vertex_in_structure_by_index(vertex_i.index)
            if adjacencies is None:
                raise Exception(
                    "Unexpected error, find_vertex_in_structure_by_index method verify if vertex is in structure.")

            for adjacency in adjacencies:
                if adjacency in vertices:
                    edge = Edge(vertex_i, adjacency)
                    edge_reversed = Edge(adjacency, vertex_i)

                    if edge_reversed not in adjacencies_created:
                        graph.add_edge(edge)
                        adjacencies_created.append(Edge(vertex_i, adjacency))

        return graph
