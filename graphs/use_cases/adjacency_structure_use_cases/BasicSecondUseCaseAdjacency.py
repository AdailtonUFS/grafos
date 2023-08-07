from graphs.entities.AdjacencyStructure import AdjacencyStructure
from graphs.entities.AdjacencyVertex import AdjacencyVertex
from graphs.entities.Edge import Edge
from graphs.entities.Graph import Graph


class BasicSecondUseCaseAdjacency:
    graph: AdjacencyStructure
    example_vertices: list[AdjacencyVertex] = []
    example_edges: list[Edge] = []

    def __init__(self):
        self.graph: AdjacencyStructure = Graph("estrutura de adjacência")
        self.setup()
        self.graph.print()

    def setup(self):
        self.create_vertices()
        self.add_vertices_in_adjacency_structure()
        self.create_edges()
        self.add_edges_in_adjacency_structure()

    def create_vertices(self):
        vertices = [
            AdjacencyVertex('v1', 1),
            AdjacencyVertex('v2', 2),
            AdjacencyVertex('v3', 3),
            AdjacencyVertex('v4', 4),
            AdjacencyVertex('v5', 5)
        ]

        self.example_vertices.extend(vertices)

    def add_vertices_in_adjacency_structure(self):
        for vertex in self.example_vertices:
            self.graph.add_vertex(vertex)

    def create_edges(self):
        v1, v2, v3, v4, v5 = self.example_vertices


        edges = [Edge(v1, v2),
                 Edge(v2, v3),
                 Edge(v3, v3),
                 Edge(v3, v4),
                 Edge(v4, v2),
                 Edge(v4, v5),
                 Edge(v5, v2),
                 Edge(v5, v2)]
        self.example_edges.extend(edges)

    def add_edges_in_adjacency_structure(self):
        for edge in self.example_edges:
            self.graph.add_edge(edge)
