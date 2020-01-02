import pandas as pd
from apyori import apriori

dados = pd.read_csv('transacoes.txt', header = None)
transacoes = []
for i in range(len(dados)):
    transacoes.append([str(dados.values[i,j]) for j in range(len(dados.values[i]))])

regras = apriori(transacoes, min_support = 0.5, min_confidence = 0.5)

resultados = list(regras)

resultados2 = [list(x) for x in resultados]

resultados3 = []
for j in range(len(resultados2)):
    resultados3.append([list(x) for x in resultados2[j][2]])

