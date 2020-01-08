import pandas as pd 
import seaborn as srn

base = pd.read_csv('trees.csv')

#apenas volume
srn.boxplot(base.Volume).set_title('Árvores')

#base completa
srn.boxplot(data = base)