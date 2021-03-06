from sklearn import datasets
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import confusion_matrix
import numpy as np

base = datasets.load_iris()
previsores = base.data
classe = base.target

#binarização da classe
classe_dummy = np_utils.to_categorical(classe)

X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores,
                                                                  classe_dummy,
                                                                  test_size = 0.3,
                                                                  random_state = 0)

num_entradas = len(previsores[0])
modelo = Sequential()
modelo.add(Dense(units = num_entradas + 1, input_dim = num_entradas))
modelo.add(Dense(units = num_entradas))
modelo.add(Dense(units = num_entradas - 1, activation = 'softmax'))

modelo.summary()

#imprimir
from keras.utils.vis_utils import plot_model

modelo.compile(optimizer = 'adam', loss = 'categorical_crossentropy',
               metrics = ['accuracy'])
modelo.fit(X_treinamento, y_treinamento, epochs = 1000,
           validation_data = (X_teste, y_teste))

previsoes = modelo.predict(X_teste)

#valores maiores que 0.5 são true senão falso
previsoes = (previsoes > 0.5)

y_teste_matrix = [np.argmax(t) for t in y_teste]
y_previsoes_matrix = [np.argmax(t) for t in previsoes]

confusao = confusion_matrix(y_teste_matrix, y_previsoes_matrix)
