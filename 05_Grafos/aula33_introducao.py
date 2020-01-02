from igraph import Graph
from igraph import plot

grafo4 = Graph(directed = False)
grafo4.add_vertices(5)
grafo4.add_edges([(0,1),(1,2),(2,3),(3,4),(4,0),(0,2),(2,1)])
grafo4.add_vertex(5) #6 nodes
grafo4.add_vertex(6) #7 nodes
grafo4.vs['label'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
grafo4.vs['name'] =  ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print(grafo4)
plot(grafo4, bbox = (300,300))

#matriz de adjacências
print(grafo4.get_adjacency())

#adjacências do vértice 0
print(grafo4.get_adjacency()[0,])

#número de arestas entre os vértices 1 e 2
print(grafo4.get_adjacency()[1,2])

for v in grafo4.vs:
    print(v)

grafo5 = Graph(edges = [(0,1),(2,3),(0,2),(0,3)], directed = True)
grafo5.vs['label'] = ['Fernando', 'Pedro', 'Jose', 'Antonio'] 
grafo5.vs['peso'] = [40, 30, 30, 25]

#atribuir para todos os vértices o mesmo valor de atributo
grafo5.vs['type'] = 'Humano'

#descrição dos vértices
for v in grafo5.vs:
    print(v)

grafo5.es['TipoAmizade'] = ['Amigo', 'Inimigo', 'Inimigo', 'Amigo']
grafo5.es['weight'] = [1,2,1,3]

#atribuir para todas as arestas o mesmo valor de atributo
grafo5.es['relação'] = 'Conhecido'

#descrição das arestas
for e in grafo5.es:
    print(e)
    
grafo5['name'] = 'Amizades'

print(grafo5['name'])
plot(grafo5, bbox = (300,300))

