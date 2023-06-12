from src.Vertice import Vertice
from src.Aresta import Aresta

class Grafo:
    arestas: list[Aresta]
    vertices = list[Vertice]

    def __init__(self, arestas: list[Aresta], vertices: list[Vertice]):

        self.arestas = arestas
        self.vertices = vertices

    def matriz(self):
        cabecalho = "   "
        matriz = ""
        for v1 in self.vertices:
            matriz += v1.nome + " "
            cabecalho = cabecalho + " " + v1.nome
            for v2 in self.vertices:
                relacao = self.relacao(v1, v2)
                matriz = matriz + "  " + str(relacao)

            matriz = matriz + "\n"

        texto = cabecalho + "\n" + matriz
        print(texto)

    def relacao(self, v1: Vertice, v2: Vertice) -> int:

        for aresta in self.arestas:
            if ((v1 == aresta.vertice01 and v2 == aresta.vertice02)  or (v2 == aresta.vertice01 and v1 == aresta.vertice02)) and v1 == v2:
                return 2
            elif (v1 == aresta.vertice01 and v2 == aresta.vertice02) or (v2 == aresta.vertice01 and v1 == aresta.vertice02) :
                return 1

        return 0