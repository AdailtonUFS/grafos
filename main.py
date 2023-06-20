from src.v2.Grafo import Grafo
from src.v2.Vertice import Vertice

print(type(Grafo("Matriz")))
print(type(Grafo("Estrutura de Adjacência")))
print(type(Grafo("Outro")))
print('\n')

grafomatriz = Grafo("Matriz")
grafomatriz.adicionar(Vertice("vertice 0", 2))


grafomatriz.matriz_representacao()

print('\n Inserir 1')

grafomatriz.adicionar(Vertice("vertice 2", 1))
grafomatriz.matriz_representacao()


print('\n Inserir 3')

grafomatriz.adicionar(Vertice("vertice 3", 3))
grafomatriz.matriz_representacao()

print('\n Inserir 3 DENOVO')

grafomatriz.adicionar(Vertice("vertice 3", 3))
grafomatriz.matriz_representacao()