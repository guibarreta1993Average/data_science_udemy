# -*- coding: utf-8 -*-
"""
                        amostragem simples
"""

import pandas as pd
import numpy as np

base = pd.read_csv('iris.csv')

#semente para gerar sempre a mesma proporção de valores a cada execução do código
np.random.seed(123377)

amostra = np.random.choice(a=[0,1], size = 150, replace = True, p=[0.5,0.5])
tamanho_da_amostra = len(amostra)
quantidade_de_zeros = len( amostra[amostra==0])
quantidade_de_uns = len(amostra[amostra==1])

print(tamanho_da_amostra, " ", quantidade_de_zeros, " ", quantidade_de_uns)
