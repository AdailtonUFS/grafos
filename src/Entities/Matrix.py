import bisect

from typing import Union
from src.Entities.Edge import Edge
from src.Entities.Vertex import Vertex

class Matrix:

    def __init__(self, **kwargs):
        self.matriz: list[list[int]] = [[0]]
        self.vertices: dict = {}
        self.arestas: list = []

    def adicionar(self, vertice: Vertex) -> bool:

        if self.busca_vertice_na_matriz(vertice):
            return False

        posicao = self.encontrar_posicao_insercao(vertice.indice)

        self.vertices[vertice.indice] = vertice
        self.matriz[0].insert(posicao, vertice.indice)
        self.matriz.insert(posicao, self.gerar_linha(vertice.indice))
        self.reajuste_zeros()

        return True

    def conexao(self, aresta: Edge):
        indices = self.buscar_indices_por_aresta(aresta)

        if not indices:
            return False

        indice_vertice_01, indice_vertice_02 = indices
        ligacao = 2 if aresta.laco() else 1

        self.matriz[indice_vertice_01][indice_vertice_02] += ligacao
        if indice_vertice_01 != indice_vertice_02:
            self.matriz[indice_vertice_02][indice_vertice_01] += ligacao

        self.arestas.append(aresta)
        return True

    def remover_conexao(self, aresta: Edge):
        indices = self.buscar_indices_por_aresta(aresta)

        if not indices:
            return False

        indice_vertice_01, indice_vertice_02 = indices

        ligacao = 2 if aresta.laco() else 1
        self.matriz[indice_vertice_01][indice_vertice_02] -= ligacao
        if indice_vertice_01 != indice_vertice_02:
            self.matriz[indice_vertice_02][indice_vertice_01] -= ligacao
        # @TODO ao remover uma conexão remover a aresta da lista de arestas
        return True

    def existe_conexao(self, indice01: int, indice02: int) -> bool:
        indice_na_matriz_01 = self.busca_indice_na_matriz(indice01)
        indice_na_matriz_02 = self.busca_indice_na_matriz(indice02)

        if indice_na_matriz_01 and indice_na_matriz_02:
            return self.matriz[indice_na_matriz_01][indice_na_matriz_02] > 0 and self.matriz[indice_na_matriz_02][
                indice_na_matriz_01] > 0

        return False

    def buscar_indices_por_aresta(self, aresta: Edge) -> Union[list, bool]:
        vertice01 = aresta.vertice01
        vertice02 = aresta.vertice02

        indice_vertice_01 = self.busca_vertice_na_matriz(vertice01)
        indice_vertice_02 = self.busca_vertice_na_matriz(vertice02)

        if indice_vertice_01 and indice_vertice_02:
            return [indice_vertice_01, indice_vertice_02]

        return False

    def busca_vertice_na_matriz(self, vertice: Vertex) -> Union[int, bool]:
        primeira_linha_matriz = self.matriz[0][1:]

        if not primeira_linha_matriz:
            return False

        posicao = bisect.bisect_left(primeira_linha_matriz, vertice.indice)

        if posicao < len(primeira_linha_matriz) and primeira_linha_matriz[posicao] == vertice.indice:
            return posicao + 1

        return False

    def busca_indice_na_matriz(self, indice: int) -> Union[int, bool]:
        primeira_linha_matriz = self.matriz[0][1:]

        if not primeira_linha_matriz:
            return False

        posicao = bisect.bisect_left(primeira_linha_matriz, indice)

        if posicao < len(primeira_linha_matriz) and primeira_linha_matriz[posicao] == indice:
            return posicao + 1

        return False

    def encontrar_posicao_insercao(self, indice: int) -> int:
        matriz_sem_a_posicao_zero = self.matriz[0][1:]
        return bisect.bisect(matriz_sem_a_posicao_zero, indice) + 1

    def matriz_representacao(self):
        cabecalho = "  "
        for item in self.matriz[0][1:]:
            vertice = self.vertices[item]
            cabecalho += " " + vertice.nome

        print(cabecalho)
        for linha in self.matriz[1:]:
            if linha[0]:
                vertice = self.vertices[linha[0]]
                linha[0] = vertice.nome
            print("  ".join(str(elemento) for elemento in linha))

        print("Vértices",len(self.vertices))
        print("Arestas",len(self.arestas))

    def gerar_zeros(self) -> list:
        if len(self.matriz[0]) < 2:
            return []

        n = len(self.matriz[0])
        return [0] * (n - 1)

    def gerar_linha(self, indice: int) -> list:
        linha = self.gerar_zeros()
        linha.insert(0, indice)
        return linha

    def reajuste_zeros(self):
        quantidade_de_indices = len(self.matriz[0])
        for indice, linha in enumerate(self.matriz[1:], start=1):
            zeros_faltantes = quantidade_de_indices - len(linha)
            linha.extend(([0] * zeros_faltantes))

    def grau_vertice(self, indice: int) -> int:
        vertice = self.busca_indice_na_matriz(indice)
        if vertice is False:
            return False

        return sum(self.matriz[vertice][1:])
