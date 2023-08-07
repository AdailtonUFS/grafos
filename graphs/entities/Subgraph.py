from typing import List, Union

from graphs.entities.AdjacencyStructure import AdjacencyStructure
from graphs.entities.Edge import Edge
from graphs.entities.Vertex import Vertex
from graphs.repositories.SubgraphRepository import SubgraphRepository


class Subgraph:

    def __init__(self, adjacency_structure: AdjacencyStructure):
        self.repository = SubgraphRepository(adjacency_structure.repository)

    def proper(self, vertices: List[Vertex], edges: List[Edge]) -> Union[AdjacencyStructure | bool]:
        return self.repository.proper(vertices, edges)

    def induced(self, vertices: List[Vertex]):
        return self.repository.induced(vertices)
