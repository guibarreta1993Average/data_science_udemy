from igraph import Graph
from igraph import plot
import igraph
import numpy as np

grafo  = igraph.load('Grafo.graphml')
comunidades = grafo.clusters()
print(comunidades)

switcher = {
        0: 'black', 
        1: 'gray',
        2: 'white',
        3: 'yellow',
        4: 'orange',
        5: 'blue',
        6: 'red',
        7: 'aqua',
        8: 'violet',
        9: 'green',
        10: 'cyan'
    }
    
cores = []
for c in comunidades.membership:
        cores.append(switcher.get(c, lambda: "Invalid color"))

plot(grafo, bbox= (300,300), vertex_color = cores)

grafo2 = Graph(edges = [(0,2),(0,1),(0,5),(1,4),(1,5),(2,3),(6,7),(3,7),(4,7),(5,6)],
                        directed = True)
grafo2.vs['label'] = ['A','B','C','D','E','F','G','H']
grafo2.es['weight'] = [2,1,2,2,1,2,1,3,1]

c = grafo2.community_edge_betweenness()
comunidades2 = c.as_clustering()
print(comunidades2)

cores2 = []
for m in comunidades2.membership:
    cores2.append(switcher.get(m, lambda:"invalid color"))

plot(grafo2, bbox = (300, 300), vertex_color = cores2)

#cliques
cli = grafo.as_undirected().cliques(min = 4)
cli2 = grafo2.as_undirected().cliques(min = 3)
print(cli)
len(cli)
print(cli2)
len(cli2)
