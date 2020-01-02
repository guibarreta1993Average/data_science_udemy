from igraph import Graph
from igraph import plot

grafo = Graph(edges = [(0,2),(0,1),(1,4),(1,5),(2,3),(6,7),(3,7),(4,7),(5,6)],
                       directed = True)
grafo.vs['label'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
grafo.es['weight'] = [2,1,2,1,2,1,3,1]

plot(grafo, bbox = (300,300), edge_label = grafo.es['weight'])

#menor caminho para A - H
caminho_vertice = grafo.get_shortest_paths(0,7, output = 'vpath')
for v in caminho_vertice[0]:
    print(grafo.vs[v]['label'])

caminho_aresta = grafo.get_shortest_paths(0,7, output = 'epath')

#distância percorrida para o menor caminho A - H
distancia = 0
for e in caminho_aresta[0]:
    distancia += grafo.es[e]['weight']
    
print(distancia)