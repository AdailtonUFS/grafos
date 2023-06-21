from src.Entities.Aresta import Aresta
from src.Entities.Grafo import Grafo
from src.Entities.Matriz import Matriz
from src.Entities.Vertice import Vertice


class Exemplo02:
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

        e1 = Aresta(v1, v2)
        self.grafo_matriz.conexao(e1)

        e2 = Aresta(v2, v3)
        self.grafo_matriz.conexao(e2)

        e3 = Aresta(v3, v3)
        self.grafo_matriz.conexao(e3)

        e4 = Aresta(v3, v4)
        self.grafo_matriz.conexao(e4)

        e5 = Aresta(v4, v2)
        self.grafo_matriz.conexao(e5)

        e6 = Aresta(v4, v5)
        self.grafo_matriz.conexao(e6)

        e7 = Aresta(v5, v2)
        self.grafo_matriz.conexao(e7)

        e8 = Aresta(v5, v2)
        self.grafo_matriz.conexao(e8)

