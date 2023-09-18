from Graph import Graph
from Matrix import Matrix


class CreateMatrixCompleteGraphUseCase:
    matrix_graph: Matrix

    def __init__(self):
        self.matrix_graph = Graph("matriz")
        self.matrix_graph.complete_graph(8)
        self.matrix_graph.print()
