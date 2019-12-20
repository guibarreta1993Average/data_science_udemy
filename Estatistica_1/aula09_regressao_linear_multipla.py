import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm

base = pd.read_csv('mt_cars.csv')
base = base.drop('Unnamed: 0', axis = 1)

X = base.iloc[:,2].values
y = base.iloc[:,0].values
correlacao = np.corrcoef(X,y)
X = X.reshape(-1,1)

modelo = LinearRegression()
modelo.fit(X,y)

modelo.intercept_
modelo.coef_

#R2
modelo.score(X,y)

previsoes = modelo.predict(X)

#R2 ajustado

