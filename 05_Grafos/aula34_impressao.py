from igraph import Graph
from igraph import plot

grafo = Graph(edges = [(0,1),(2,3),(0,2),(0,3)], directed = True)
grafo.vs['label'] =['Fernando', 'Pedro', 'Jose', 'Antonio']
grafo.vs['nota'] = [100, 40, 60, 20]
grafo.es['tipoAmizade'] = ['Amigo', 'Inimigo', 'Amigo']
grafo.es['devendo'] = [1,3,2,5]

grafo.vs['color'] = ['red', 'yellow','orange', 'green']

plot(grafo, bbox =(300,300),
     vertex_size = grafo.vs['nota'],
     edge_width = grafo.es['devendo'],
     vertex_color = grafo.vs['color'],
     edge_curved = 0.4,
     vertex_shape = 'square')
