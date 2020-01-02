import matplotlib.pyplot as plt
import nltk 
#nltk.download()
from nltk.corpus import PlaintextCorpusReader

corpus = PlaintextCorpusReader('Arquivos', '.*')

arquivos = corpus.fileids()
arquivos[0]
arquivos[0:100]

#mostrar todos os arquivos
for a in arquivos:
    print(a)

texto = corpus.raw('1.txt')

todo_texto = corpus.raw()
palavras = corpus.words()
palavras[170]
len(palavras)

