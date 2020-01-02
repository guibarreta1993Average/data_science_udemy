import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
import string

corpus = PlaintextCorpusReader('Arquivos', '.*')

palavras = corpus.words()

stops = stopwords.words('english')

palavras_sem_stop = [p for p in palavras if p not in stops]
len(palavras_sem_stop)

sujeira = string.punctuation
sujeira += '&#' + ';\',' 

palavras_sem_pontuacao = [p for p in palavras_sem_stop if (p not in sujeira and not p.isdecimal())]

frequencia = nltk.FreqDist(palavras_sem_pontuacao)