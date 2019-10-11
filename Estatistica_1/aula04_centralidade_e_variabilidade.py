# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 10:32:07 2019

@author: guilherme.barreta
"""

import numpy as np 
from scipy import stats

jogadores = [40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000]

np.mean(jogadores)
np.median(jogadores)
np.std(jogadores, ddof= 1)

quartis = np.quantile(jogadores, [0,0.25, 0.5, 0.75, 1])

print(stats.describe(jogadores))
