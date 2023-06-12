from src.Vertice import Vertice
from src.Aresta import Aresta

class Grafo:
    arestas: list[Aresta]
    vertices = list[Vertice]

    def __init__(self, arestas: list[Aresta], vertices: list[Vertice]):

        self.arestas = arestas
        self.vertices = vertices

    def matriz(self):
        matriz = []
        for i, v1 in enumerate(self.vertices):
            linha = []
            for v2 in self.vertices:
                relacao = self.relacao(v1, v2)
                linha.append(relacao)
            matriz.append(linha)
        return matriz

    def matriz_representacao(self):
        cabecalho = "  "

        for v in self.vertices:
            cabecalho += " " + v.nome

        matriz = self.matriz()

        print(cabecalho)

        for item, vertice in zip(matriz, self.vertices):
            print(vertice.nome, end="  ")
            for i in item:
                print(i, end="  ")
            print("")


    def relacao(self, v1: Vertice, v2: Vertice) -> int:
        count = 0
        for aresta in self.arestas:
            if ((v1 == aresta.vertice01 and v2 == aresta.vertice02)  or (v2 == aresta.vertice01 and v1 == aresta.vertice02)) and v1 == v2:
                count += 2
            elif (v1 == aresta.vertice01 and v2 == aresta.vertice02) or (v2 == aresta.vertice01 and v1 == aresta.vertice02) :
                count += 1

        return count