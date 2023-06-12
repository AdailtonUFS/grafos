from src.Vertice import Vertice
from src.Aresta import Aresta
from src.Grafo import Grafo

v1 = Vertice("v1")
v2 = Vertice("v2")
v3 = Vertice("v3")
v4 = Vertice("v4")
v5 = Vertice("v5")
v6 = Vertice("v6")

vertices = [v1, v2, v3, v4, v5, v6]

a1 = Aresta(v1,v2)
a2 = Aresta(v2,v3)
a3 = Aresta(v2,v5)
a4 = Aresta(v4,v5)
a5 = Aresta(v5,v6)
a6 = Aresta(v5,v6)
a7 = Aresta(v6,v6)

arestas = [a1, a2, a3, a4, a5, a6, a7]

grafo = Grafo(arestas, vertices)

grafo.matriz()
