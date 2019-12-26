import pandas as pd
import numpy as np 
import matplotlib.pylab as plt
from statsmodels.tsa.seasonal import seasonal_decompose

dateparse = lambda dates: pd.datetime.strptime(dates,'%Y-%m')
base = pd.read_csv('AirPassengers.csv', parse_dates = ['Month'],
                   index_col = 'Month', date_parser = dateparse)
ts = base['#Passengers']
          
ts.mean()

ts['1960'].mean()

media_movel = ts.rolling(window =12).mean()
plt.plot(ts)
plt.plot(media_movel, color = 'red') 

previsoes = []

#um ano
for i in range(1,13):
    superior = len(media_movel)-i
    inferior = superior - 11
    print(superior)
    print(inferior)
    previsoes.append(media_movel[inferior:superior].mean())

previsoes = previsoes[::-1]
plt.plot(previsoes)