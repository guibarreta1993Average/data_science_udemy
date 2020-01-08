import pandas as pd

base = pd.read_csv('insect.csv')

agrupamento = base.groupby(['spray'])['count'].sum()

agrupamento.plot.bar(color = 'red')

agrupamento.plot.pie(legend = True)