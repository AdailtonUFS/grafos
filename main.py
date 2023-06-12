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

grafo.matriz_representacao()


a1 = Aresta(v1,v1)
a2 = Aresta(v1,v2)
a3 = Aresta(v1,v5)
a4 = Aresta(v2,v3)
a5 = Aresta(v2,v3)
a6 = Aresta(v2,v4)
a7 = Aresta(v2,v5)
a8 = Aresta(v3,v4)
a9 = Aresta(v3,v5)
a10 = Aresta(v4,v5)

print('\n')
arestas2 = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
vertices2 = [v1,v2,v3,v4,v5]
grafo2 = Grafo(arestas2, vertices2)
grafo2.matriz_representacao()



