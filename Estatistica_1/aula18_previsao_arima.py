import pandas as pd
import numpy as np 
import pmdarima as pm
import matplotlib.pylab as plt
from statsmodels.tsa.arima_model import ARIMA

#from pyramid.arima import auto_arima

dateparse = lambda dates: pd.datetime.strptime(dates,'%Y-%m')
base = pd.read_csv('AirPassengers.csv', parse_dates = ['Month'],
                   index_col = 'Month', date_parser = dateparse)
ts = base['#Passengers']

#p, q, d

modelo =ARIMA(ts, order = (2, 1, 2))          
modelo_treinado = modelo.fit()
modelo_treinado.summary()

previsoes = modelo_treinado.forecast(steps = 12)[0]

eixo = ts.plot()
modelo_treinado.plot_predict('1960', '1970',
                             ax= eixo, plot_insample = False)

modelo_auto = pm.auto_arima(ts, m = 12, seasonal = True, trace = True)
modelo_auto.summary()
proximos_12 = modelo_auto.predict(n_periods = 12)