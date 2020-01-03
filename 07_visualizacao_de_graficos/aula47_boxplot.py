import pandas as pd
import matplotlib.pyplot as plt

base = pd.read_csv('trees.csv')

plt.boxplot(base.Volume, vert = False, showfliers = False,
            notch = True, patch_artist = True)
plt.title('Árvore')
plt.xlabel('Volume')

#colorir
#https://matplotlib.org/gallery/statistics/boxplot_demo.html

#plt.boxplot(base)

plt.subplot(2,2,1)
plt.boxplot(base.Volume, vert = False)
plt.subplot(2,2,2)
plt.boxplot(base.Girth, vert = False)
plt.subplot(2,2,3)
plt.boxplot(base.Height, vert = False)

