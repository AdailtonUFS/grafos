class Vertex:
    nome: str
    indice: int

    def __init__(self, nome, indice):
        self.nome = nome
        self.indice = indice

    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.nome == other.nome and self.indice == other.indice
        return False