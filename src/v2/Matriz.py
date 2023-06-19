from src.v2.Vertice import Vertice


class Matriz:
    matriz:list = []
    indices:set = set()
    def adicionar(self, vertice:Vertice, force=False) -> bool:
        if vertice.indice in self.indices and force == False:
            print("O item já está na lista.")
            return False

        self.indices.add(vertice.indice)

        print("inserido")
        print(self.indices)
        return True
