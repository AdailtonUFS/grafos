from graphs.entities.AdjacencyStructure import AdjacencyStructure
from graphs.entities.AdjacencyVertex import AdjacencyVertex
from graphs.entities.Edge import Edge
from graphs.entities.Graph import Graph


class CreateAdjacencyGraphUseCase3:
    graph: AdjacencyStructure
    example_vertices: list[AdjacencyVertex] = []
    example_edges: list[Edge] = []

    def __init__(self):
        self.graph: AdjacencyStructure = Graph("estrutura de adjacência")
        self.setup()
        self.graph.print()
        va, *_ = self.example_vertices
        self.graph.deep_search(va)
        self.graph.test_deep()

    def setup(self):
        self.create_vertices()
        self.add_vertices_in_adjacency_structure()
        self.create_edges()
        self.add_edges_in_adjacency_structure()

    def create_vertices(self):
        vertices = [
            AdjacencyVertex('a', 1),
            AdjacencyVertex('b', 2),
            AdjacencyVertex('c', 3),
            AdjacencyVertex('d', 4),
            AdjacencyVertex('e', 5),
            AdjacencyVertex('f', 6),
            AdjacencyVertex('g', 7),
            AdjacencyVertex('h', 8)
        ]

        self.example_vertices.extend(vertices)

    def add_vertices_in_adjacency_structure(self):
        for vertex in self.example_vertices:
            self.graph.add_vertex(vertex)

    def create_edges(self):
        va, vb, vc, vd, ve, vf, vg, vh = self.example_vertices

        edges = [Edge(va, vb),
                 Edge(va, vc),
                 Edge(va, ve),
                 Edge(va, vf),
                 Edge(vb, vd),
                 Edge(vb, ve),
                 Edge(vc, vf),
                 Edge(vc, vg),
                 Edge(vc, vh),
                 Edge(vf, vg),
                 Edge(vf, vh),
                 Edge(vg, vh),
                 ]
        self.example_edges.extend(edges)

    def add_edges_in_adjacency_structure(self):
        for edge in self.example_edges:
            self.graph.add_edge(edge)
