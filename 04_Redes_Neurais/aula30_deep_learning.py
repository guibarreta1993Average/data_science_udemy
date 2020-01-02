from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import np_utils
from keras.datasets import mnist
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt

(X_treinamento, y_treinamento), (X_teste, y_teste) = mnist.load_data()

#exibindo uma imagem
plt.imshow(X_treinamento[22], cmap = 'gray')
plt.title(y_treinamento[22])

#redimensionamento de 28x28 para uma linha de 784
X_treinamento = X_treinamento.reshape(len(X_treinamento), np.prod(X_treinamento.shape[1:]))
X_teste = X_teste.reshape(len(X_teste), np.prod(X_teste.shape[1:]))

X_treinamento = X_treinamento.astype('float32')
X_teste = X_teste.astype('float32')

#normalização
X_treinamento /= 255
X_teste /= 255

#binarização
y_treinamento = np_utils.to_categorical(y_treinamento, 10)
y_teste = np_utils.to_categorical(y_teste, 10)

#rede neural
modelo = Sequential()
modelo.add(Dense(units = 64, activation = 'relu', input_dim = len(X_treinamento[0])))
modelo.add(Dropout(0.2))
modelo.add(Dense(units = 64, activation = 'relu'))
modelo.add(Dropout(0.2))
modelo.add(Dense(units = 64, activation = 'relu'))
modelo.add(Dropout(0.2))
modelo.add(Dense(units = 10, activation = 'softmax'))
modelo.add(Dropout(0.2))

modelo.summary()

modelo.compile(optimizer = 'adam', loss = 'categorical_crossentropy',
               metrics = ['accuracy'])
historico = modelo.fit(X_treinamento, y_treinamento, epochs = 20,
                       validation_data = (X_teste, y_teste))

#evolução do treinamento
historico.history.keys()
plt.plot(historico.history['val_loss'])
plt.plot(historico.history['val_accuracy'])

previsoes = modelo.predict(X_teste) 
y_teste_matrix = [np.argmax(t) for t in y_teste]
y_previsoes_matrix = [np.argmax(t) for t in previsoes]
confusao = confusion_matrix(y_teste_matrix, y_previsoes_matrix)

#exemplo
y_teste[45] #5
novo = X_teste[45]
novo = np.expand_dims(novo, axis = 0) #expandir dimesões de 28x28 para 784
pred = modelo.predict(novo)
pred = [np.argmax(t) for t in pred] #5