from abc import abstractmethod, ABC


class Graph(ABC):
    def __new__(cls, structure: str):
        if structure.lower() == "matriz":
            from graphs.entities.Matrix import Matrix
            return Matrix()
        elif structure.lower() == "estrutura de adjacência":
            from graphs.entities.AdjacencyStructure import AdjacencyStrutucture
            return AdjacencyStrutucture()
        else:
            return super().__new__(cls)


    @abstractmethod
    def adicionar(self):
        pass