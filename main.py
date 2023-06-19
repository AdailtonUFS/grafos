from src.v2.Grafo import Grafo
from src.v2.Vertice import Vertice

print(type(Grafo("Matriz")))
print(type(Grafo("Estrutura de Adjacência")))
print(type(Grafo("Outro")))
print('\n')

grafomatriz = Grafo("Matriz")
grafomatriz.adicionar(Vertice("vertice 1", 0))
