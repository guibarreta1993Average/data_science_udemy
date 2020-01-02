from sklearn import datasets
from sklearn.metrics import confusion_matrix
import numpy as np
from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.cluster import cluster_visualizer

iris = datasets.load_iris()
cluster = kmedoids(iris.data[:,0:2],[3,12,20])
cluster.get_medoids() #retorna 3 12 20
cluster.process()
previsoes = cluster.get_clusters()
medoides = cluster.get_medoids() # retorna outros medoids após process()

#visualização da clusterização
v = cluster_visualizer()
v.append_clusters(previsoes, iris.data[:, 0:2])
v.append_cluster(medoides, data = iris.data[:, 0:2], marker ='*',markersize = 15)
v.show()

#matriz de confusão
lista_previsoes =[]
lista_real = []
for i in range(len(previsoes)):
    print('---')
    print(i)
    print('---')
    for j in range(len(previsoes[i])):
        print(previsoes[i][j])
        lista_previsoes.append(i)
        lista_real.append(iris.target[previsoes[i][j]])

lista_previsoes = np.asarray(lista_previsoes)
lista_real = np.asarray(lista_real)
confusao = confusion_matrix(lista_real, lista_previsoes) # é possível verificar os acertos do jeito tradicional
