#from igraph import Graph
#from igraph import plot
import igraph

grafo = igraph.load('Grafo.graphml')
print(grafo)
plot(grafo, bbox = (300,300))

grau_total = grafo.degree(type = 'all')
grau_entrada = grafo.degree(type = 'in')
grau_saida = grafo.degree(type = 'out')

plot(grafo, bbox = (300,300), vertex_size = grau_entrada)

grafo.diameter(directed = True)
grafo.diameter(directed = False)

#vértices mais distantes
grafo.get_diameter()

grafo.neighborhood()

grafo2 = grafo
grafo.isomorphic(grafo2)



