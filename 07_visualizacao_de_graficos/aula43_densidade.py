import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base = pd.read_csv('trees.csv')

sns.distplot(base.iloc[:,1], hist = True, kde = True,
             bins = 4, hist_kws = {'edgecolor': 'black', 'color': 'red'})

