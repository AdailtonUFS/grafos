from graphs.entities.Edge import Edge
from graphs.entities.Graph import Graph
from graphs.entities.Matrix import Matrix
from graphs.entities.Vertex import Vertex


class CreateMatrixGraphUseCase:
    matrix_graph: Matrix
    example_vertices: list[Vertex] = []
    example_edges: list[Edge] = []

    def __init__(self):
        self.matrix_graph = Graph("matriz")
        self.setup()
        self.matrix_graph.print()

    def setup(self):
        self.create_vertices()
        self.add_vertices_in_matrix()
        self.create_edges()
        self.add_edges_in_matrix()

    def create_vertices(self):
        vertices = [Vertex('v1', 1),
                    Vertex('v2', 2),
                    Vertex('v3', 3),
                    Vertex('v4', 4),
                    Vertex('v5', 5),
                    ]

        self.example_vertices.extend(vertices)

    def add_vertices_in_matrix(self):
        for vertex in self.example_vertices:
            self.matrix_graph.add_vertex(vertex)

    def create_edges(self):
        v1, v2, v3, v4, v5 = self.example_vertices

        edges = [Edge(v1, v2),
                 Edge(v1, v3),
                 Edge(v1, v4),
                 Edge(v1, v5),
                 Edge(v2, v3),
                 Edge(v2, v4),
                 Edge(v2, v5),
                 Edge(v3, v4),
                 Edge(v3, v5),
                 Edge(v4, v5)
                 ]
        self.example_edges.extend(edges)

    def add_edges_in_matrix(self):
        for edge in self.example_edges:
            self.matrix_graph.add_edge(edge)
