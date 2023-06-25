from src.Entities.Edge import Edge
from src.Entities.Graph import Graph
from src.Entities.Matrix import Matrix
from src.Entities.Vertex import Vertex


class Exemplo01:
    grafo_matriz: Matrix

    def __init__(self):
        self.grafo_matriz = Graph('Matriz')
        self.adicionar_vertices()
        self.grafo_matriz.matriz_representacao()


    def adicionar_vertices(self):
        v1 = Vertex('v1', 1)
        self.grafo_matriz.adicionar(v1)

        v3 = Vertex('v3', 3)
        self.grafo_matriz.adicionar(v3)

        v4 = Vertex('v4', 4)
        self.grafo_matriz.adicionar(v4)

        v5 = Vertex('v5', 5)
        self.grafo_matriz.adicionar(v5)

        v2 = Vertex('v2', 2)
        self.grafo_matriz.adicionar(v2)

        e1 = [Edge(v1, v2), Edge(v1, v3), Edge(v1, v4), Edge(v1, v5)]
        e2 = [Edge(v2, v3), Edge(v2, v4), Edge(v2, v5)]
        e3 = [Edge(v3, v4), Edge(v3, v5)]
        e4 = [Edge(v4, v5)]

        etodos = e1+e2+e3+e4

        for aresta in etodos:
            self.grafo_matriz.conexao(aresta)

 