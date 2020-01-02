from scipy.stats import t

# Média de salários dos cientistas de dados = R$ 75,00 por hora
# Amostra com 9 funcionários e desvio padrão = 10

#Qual a probabilidade de selecionar um cientista de dados e o salário
#ser menor que R$ 80 por hora
t.cdf(1.5, 8)

#Qual a probabilidade do salário ser maior do que R$ 80 por hora
t.sf(1.5, 8)