# -*- coding: utf-8 -*-
"""Classificacao de aco Regressao.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uKosNa8ZIt_9AQ2-T52_yxqAzXBK7C_D
"""

#Regressão


import pandas as pd
base = pd.read_csv('aco.csv')

previsores = base.iloc[:, 0:4].values
classe = base.iloc[:, 3].values

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(previsores[:, 0:4])
previsores[:, 0:4] = imputer.transform(previsores[:, 0:4])

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

from sklearn.model_selection import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.25, random_state=0)

from sklearn.linear_model import LogisticRegression
classificador = LogisticRegression(random_state = 0)
classificador.fit(previsores_treinamento, classe_treinamento)
previsoes = classificador.predict(previsores_teste)

from sklearn.metrics import confusion_matrix, accuracy_score
precisao = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)

import collections
collections.Counter(classe_teste)
print(matriz)
print(precisao)