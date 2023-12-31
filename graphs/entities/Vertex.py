class Vertex:
    def __init__(self, name: str, index: int):
        self.name = name
        self.index = index

    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.name == other.name and self.index == other.index
        return False
