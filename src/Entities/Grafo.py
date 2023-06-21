from src.Entities.Matriz import Matriz
from src.Entities.EstruturaAdjacencia import EstruturaAdjacencia

class Grafo:
    def __new__(cls, estrutura: str):
        if estrutura.lower() == "matriz":
            return Matriz()
        elif estrutura.lower() == "estrutura de adjacência":
            return EstruturaAdjacencia()
        else:
            return super().__new__(cls)