from graphs.entities.AdjacencyStructure import AdjacencyStructure
from graphs.entities.AdjacencyVertex import AdjacencyVertex
from graphs.entities.Edge import Edge
from graphs.entities.Graph import Graph


class SubgraphUseCaseAdjacency:
    graph: AdjacencyStructure
    example_vertices: list[AdjacencyVertex] = []
    example_edges: list[Edge] = []

    def __init__(self):
        self.graph: AdjacencyStructure = Graph("estrutura de adjacência")
        self.setup()
        self.graph.print()

        u, y, v, x, *_ = self.example_vertices
        uy, uv, yv, yv, yx, *_ = self.example_edges

        print("SUBGRAFO INDUZIDO")
        subgraph_generated = self.graph.generated_subgraph_from_vertices([u, y, v, x])
        subgraph_generated.print()

        print("SUBGRAFO PROPRIO")
        subgraph_default = self.graph.generated_subgraph_from_vertices_and_edges([u, y, v, x], [uy, uv, yv, yv])
        subgraph_default.print()


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
            AdjacencyVertex('v', 6),
        ]

        self.example_vertices.extend(vertices)

    def create_edges(self):
        u, y, v, x, w, v = self.example_vertices

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
