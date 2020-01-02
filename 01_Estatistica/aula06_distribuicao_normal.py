# -*- coding: utf-8 -*-
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot  as plt
#conjunto de objetos em uma cesta, a média é 8 e o desvio padrão é 2.
#Qual a probabilidade de tirar um objeto cujo o peso é menor que 6 quilos?
norm.cdf(6, 8, 2) #valor, média e desvio padrão

#Qual a probabilidade de tirar um objeto cujo o peso é maior que 6 quilos?
norm.sf(6, 8, 2)
1 - norm.cdf(6, 8, 2)

#Qual a probabilidade de tirar um objeto cujo o peso é menor que 6 ou maior
#que 10 quilos?
norm.cdf(6, 8, 2) + norm.sf(10, 8, 2)

#Qual a probabilidade de tirar um objeto que o peso é menor que 10 e maior
#que 8 quilos?
norm.cdf(10, 8, 2) - norm.cdf(8, 8, 2)



#gerando um dados, gráfico e executando o teste de shapiro
dados = norm.rvs(size= 100)
stats.probplot(dados, plot = plt)

stats.shapiro(dados)