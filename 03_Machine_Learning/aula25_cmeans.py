from sklearn.metrics import confusion_matrix
from sklearn import datasets
import numpy as np
import skfuzzy

iris = datasets.load_iris()

r = skfuzzy.cmeans(data = iris.data.T, c = 3, m = 2, error = 0.005,
                   maxiter = 1000, init = None)
previsoes_porcentagem = r[1]

soma_porcentagens = previsoes_porcentagem[0][0] +\
                    previsoes_porcentagem[1][0] +\
                    previsoes_porcentagem[2][0]
                    
previsoes = previsoes_porcentagem.argmax( axis = 0)

confusao = confusion_matrix(iris.target, previsoes)

