from src.v2.Aresta import Aresta
from src.v2.Grafo import Grafo
from src.v2.Matriz import Matriz
from src.v2.Vertice import Vertice


class Exemplo01:
    grafo_matriz: Matriz

    def __init__(self):
        self.grafo_matriz = Grafo('Matriz')
        self.adicionar_vertices()
        self.grafo_matriz.matriz_representacao()


    def adicionar_vertices(self):
        v1 = Vertice('v1', 1)
        self.grafo_matriz.adicionar(v1)

        v3 = Vertice('v3', 3)
        self.grafo_matriz.adicionar(v3)

        v4 = Vertice('v4', 4)
        self.grafo_matriz.adicionar(v4)

        v5 = Vertice('v5', 5)
        self.grafo_matriz.adicionar(v5)

        v2 = Vertice('v2', 2)
        self.grafo_matriz.adicionar(v2)

        e1 = [Aresta(v1, v2), Aresta(v1, v3),Aresta(v1, v4), Aresta(v1, v5)]
        e2 = [Aresta(v2, v3),Aresta(v2, v4), Aresta(v2, v5)]
        e3 = [Aresta(v3, v4), Aresta(v3, v5)]
        e4 = [Aresta(v4, v5)]

        etodos = e1+e2+e3+e4

        for aresta in etodos:
            self.grafo_matriz.conexao(aresta)

 