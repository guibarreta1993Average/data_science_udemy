# -*- coding: utf-8 -*-
"""
                        amostragem estratificada
"""
import pandas as pd
from sklearn.model_selection import train_test_split

iris = pd.read_csv('iris.csv')

x1, _, y1, _ = train_test_split(iris.iloc[:, 0:4], iris.iloc[:, 4],
                              test_size = 0.5, stratify = iris.iloc[:,4])

print(y1.value_counts())

infert = pd.read_csv('infert.csv')
#infert.value_counts()
x2, _, y2,_ = train_test_split(infert.iloc[:, 2:9], infert.iloc[:, 1],
                               test_size = 0.596, stratify = infert.iloc[:,1])
print(y2.value_counts())