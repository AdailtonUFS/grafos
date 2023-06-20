from bisect import bisect

from src.v2.Vertice import Vertice


class Matriz:
    matriz: list = [[""]]
    indices: dict = {}

    def adicionar(self, vertice: Vertice) -> bool:
        if self.esta_na_matriz(vertice):
            return False

        posicao = self.encontrar_posicao(vertice.indice)

        self.indices[vertice.indice] = posicao

        self.matriz[0].insert(posicao, vertice.indice)

        # @TODO ao inserir um novo indice atualizar os zeros em cada item

        linha = self.gerar_linha(vertice.indice)
        self.matriz.insert(posicao, linha)

        return True

    def esta_na_matriz(self, vertice: Vertice) -> bool:
        return self.indices.get(vertice.indice) is not None

    def encontrar_posicao(self, indice: int) -> int:
        matriz_sem_a_posicao_zero = self.matriz[0][1:]
        indice_matriz = bisect(matriz_sem_a_posicao_zero, indice)
        return indice_matriz + 1

    def matriz_representacao(self):

        for linha in self.matriz:
            print(linha)

    def gerar_zeros(self) -> list:
        if len(self.matriz[0]) < 2:
            return []

        n = len(self.matriz[0])
        return [0] * (n - 1)

    def gerar_linha(self, indice:int) -> list:
        linha = self.gerar_zeros()
        linha.insert(0, indice)
        return linha