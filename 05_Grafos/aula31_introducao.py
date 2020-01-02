from igraph import Graph
from igraph import plot

#grafo simples orientado que forma um circuito
grafo1 = Graph(edges = [(0,1),(1,2),(2,3),(3,0)], directed = True)
print(grafo1)
grafo1.vs['label'] = range(grafo1.vcount()) #não funcionou
plot(grafo1, bbox = (300,300))

#grafo orientado com laço
grafo2 = Graph(edges = [(0,1),(1,2),(2,3),(3,0),(1,1)], directed = True)
print(grafo2)
plot(grafo2, bbox = (300,300))

#circuito não-euleriano
grafo3 = Graph(edges = [(0,1),(1,2),(2,3),(3,0),(1,0),(2,0),(3,0)], directed = False)
print(grafo3)
plot(grafo3, bbox = (300,300))

#grafo desconexo
grafo4 = Graph(edges = [(0,1),(1,2),(2,3),(3,0),(1,1)], directed = True)
grafo4.add_vertex(5)
print(grafo4)
plot(grafo4, bbox = (300,300))
