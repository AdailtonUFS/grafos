from typing import List

from graphs.entities.Edge import Edge
from graphs.entities.Vertex import Vertex
from graphs.repositories.AdjacencyStructureRepository import AdjacencyStructureRepository


class SubgraphRepository(AdjacencyStructureRepository):
    def __init__(self):
        super().__init__()


