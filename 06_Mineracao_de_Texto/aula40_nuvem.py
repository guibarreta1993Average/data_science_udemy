import matplotlib.pyplot as plt
import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from matplotlib.colors import ListedColormap
from wordcloud import WordCloud

corpus = PlaintextCorpusReader('Arquivos', '.*')
todo_texto = corpus.raw()

stops = stopwords.words('english')

mapa_cores = ListedColormap(['orange', 'green', 'red', 'magenta'])

nuvem = WordCloud(background_color = 'white',
                  colormap = mapa_cores,
                  stopwords = stops,
                  max_words = 100)
nuvem.generate(todo_texto)
plt.imshow(nuvem)


