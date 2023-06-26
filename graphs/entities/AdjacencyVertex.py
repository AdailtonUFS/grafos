from typing import Dict, List

from graphs.entities.Vertex import Vertex


class AdjacencyVertex(Vertex):
    def __init__(self, name, index):
        super().__init__(name, index)
        self.neighbors: Dict[int, List[Vertex]] = {}

    def add_neighbors(self, neighbor: Vertex):
        if self.is_neighbor(neighbor):
            neighbor_in_neighbors = self.neighbors[neighbor.index]
            neighbor_in_neighbors.append(neighbor)
            return True

        self.neighbors[neighbor.index] = [neighbor]
        return True

    def is_neighbor(self, neighbor: Vertex):
        return self.neighbors.get(neighbor.index)
