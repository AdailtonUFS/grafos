from src.v1.Vertice import Vertice

class Aresta:
    vertice01: Vertice
    vertice02: Vertice

    def __init__(self, vertice01, vertice02):
        self.vertice01 = vertice01
        self.vertice02 = vertice02