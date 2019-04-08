# -*- coding: utf-8 -*-
"""Classificacao de Aco KNN Colab

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X8pTYLVyINc2iRgRvaZU1RSmTvdEi__8
"""

#MEU VIZINHOS

import pandas as pd
import collections
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler # Normalização de dados
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from yellowbrick.classifier import ConfusionMatrix #Biblioteca específica para visualização da matriz de confusão

base = pd.read_csv('aco.csv')
               
previsores = base.iloc[:, 0:4].values
classe = base.iloc[:, 3].values


imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(previsores[:, 0:4])
previsores[:, 0:4] = imputer.transform(previsores[:, 0:4])


scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.25, random_state=0)

classificador = KNeighborsClassifier(n_neighbors=7, metric='minkowski', p = 2)# n_neighbors (k) vizinhos, metrica minkwski, p=2 é medida euclidiana padrão
classificador.fit(previsores_treinamento, classe_treinamento)
previsoes = classificador.predict(previsores_teste)

precisao = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)


collections.Counter(classe_teste)


print(previsoes)
print("\n")
print(matriz)
print("\n")
print(precisao)
print("\n")
print(previsoes)