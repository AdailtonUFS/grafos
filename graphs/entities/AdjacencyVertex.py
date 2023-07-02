from typing import Dict, List

from graphs.entities.Vertex import Vertex


class AdjacencyVertex(Vertex):
    def __init__(self, name, index):
        super().__init__(name, index)
        self.neighbors: Dict[int, List[Vertex]] = {}

    def add_neighbor(self, neighbor: Vertex):
        if self.is_neighbor(neighbor):
            neighbor_in_neighbors = self.neighbors[neighbor.index]
            neighbor_in_neighbors.append(neighbor)
            return True

        self.neighbors[neighbor.index] = [neighbor]
        return True

    def is_neighbor(self, neighbor: Vertex):
        return self.neighbors.get(neighbor.index)

    def remove_neighbor(self, neighbor: Vertex):
        if not self.is_neighbor(neighbor):
            return False

        if len(self.neighbors[neighbor.index]) == 1:
            self.neighbors.pop(neighbor.index)
            return True

        self.neighbors[neighbor.index].pop(0)
        return True

    def edges_quantity(self):
        quantity = 0

        for key, value in self.neighbors.items():

            if key == self.index:
                quantity += len(value) * 2
            else:
                quantity += len(value)

        return quantity
