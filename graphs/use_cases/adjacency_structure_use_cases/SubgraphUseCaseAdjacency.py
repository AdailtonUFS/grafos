from graphs.entities.AdjacencyStructure import AdjacencyStructure
from graphs.entities.AdjacencyVertex import AdjacencyVertex
from graphs.entities.Edge import Edge
from graphs.entities.Graph import Graph
from graphs.entities.Subgraph import Subgraph


class SubgraphUseCaseAdjacency:
    graph: AdjacencyStructure
    example_vertices: list[AdjacencyVertex] = []
    example_edges: list[Edge] = []

    def __init__(self):
        self.graph: AdjacencyStructure = Graph("estrutura de adjacência")
        self.setup()
        self.graph.print()
        self.subgraph = Subgraph(self.graph)

        print("\n___________________________________\n")
        u, y, v, x, w = self.example_vertices
        uy, uv, yv1, yv2, yx, yw, xw, vw = self.example_edges

        subgraph_proper = self.subgraph.proper([u, y, v], [uy, uv, yv1, yv2])
        subgraph_proper.print()
        print("\n___________________________________\n")
        subgraph_induced = self.subgraph.induced([y, v, x, u])
        subgraph_induced.print()


    def setup(self):
        self.create_vertices()
        self.graph.add_vertices(self.example_vertices)
        self.create_edges()
        self.graph.add_edges(self.example_edges)

    def create_vertices(self):
        vertices = [
            AdjacencyVertex('u', 1),
            AdjacencyVertex('y', 2),
            AdjacencyVertex('v', 3),
            AdjacencyVertex('x', 4),
            AdjacencyVertex('w', 5),
        ]

        self.example_vertices.extend(vertices)

    def create_edges(self):
        u, y, v, x, w = self.example_vertices

        edges = [Edge(u, y),
                 Edge(u, v),
                 Edge(y, v),
                 Edge(y, v),
                 Edge(y, x),
                 Edge(y, w),
                 Edge(x, w),
                 Edge(v, w),
                 ]
        self.example_edges.extend(edges)
