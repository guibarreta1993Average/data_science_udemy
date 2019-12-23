from scipy.stats import poisson

#Média de acidentes de carro é 2 por dia

#Qual a probabilidade de ocorrerem 3 acidentes no dia?
poisson.pmf(3, 2)

#Qual a probabilidade de ocorrerem 3 ou menos acidentes por dia?
poisson.cdf(3, 2)

#Qual a probabilidade de ocorrerem 3 ou mais acidentes por dia?
poisson.sf(3, 2) 
