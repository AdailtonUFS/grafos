from abc import abstractmethod, ABC


class Graph(ABC):
    def __new__(cls, estrutura: str):
        if estrutura.lower() == "matriz":
            from src.Entities.Matrix import Matriz
            return Matriz()
        elif estrutura.lower() == "estrutura de adjacência":
            from src.Entities.AdjacencyStructure import AdjacencyStrutucture
            return AdjacencyStrutucture()
        else:
            return super().__new__(cls)


    @abstractmethod
    def adicionar(self):
        pass