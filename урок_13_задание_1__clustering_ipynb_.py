# -*- coding: utf-8 -*-
"""урок 13 задание 1 "Clustering.ipynb"

Automatically generated by Colaboratory.

# Применение методов кластеризации

## Инструкция по выполнению задания
Ниже находится несколько  упражнений, представляющих собой код с пропущенными фрагментами, которые надо воспроизвести. Часть из этих упражнений очень простые, над некоторыми надо хорошенько подумать.
Чтобы выполнить это задание, нужно сохранить копию файла себе на Google Диск.

После выполнения задания, его нужно отправить на проверку. Для этого достаточно предоставить доступ к файлу и отправить ссылку в соответствующее поле LMS курса.
Удачи в выполнении заданий!
Для упражнений этого задания используем такой же датасет про недвижимость Бостона, что и для упражнения по PCA.
# Импортируем необходимые библиотеки
"""
import scipy.cluster.hierarchy as sch # для построения дендрограммы
from sklearn.cluster import AgglomerativeClustering # собственно для кластеризации
import matplotlib.pyplot as plt # для визуализации
from sklearn.datasets import load_boston

"""## Загрузим датасет"""

boston = load_boston()

"""## Упражнение 1
С помощью [дендрограммы](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html) определите оптимальное количество кластеров. Для этого можно выделить признаки, которые считаете наиболее существенными и построить дендрограмму по ним. А можете провести анализ по всем признакам.

Напоминаем, что определение кластеров по дендрограмме производится следующим образом: мысленно проведем горизонтальные прямоугольники между горизонтальными линиями дендрограммы так, чтобы ни одна горизонтальная линия не оказалась внутри него. 
![прямоугольник](https://miro.medium.com/max/700/1*ldDTryuZD0pZX8F8BqCcCA.jpeg)

Тот прямоугольник, который будет иметь наибольшую высоту, показывает наибольшее евклидовое расстояние между кластерами. На приведенном выше рисунке правый прямоугольник показывает большее евклидово расстояние. Значит оптимальным будет разделение на 3 кластера.

А сколько кластеров получается у Вас?
"""

from google.colab import drive
drive.mount('/content/drive')

import scipy.cluster.hierarchy as sch
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
import pandas as pd

col = ['sepal length', 'sepal width', 'petal length', 'petal width', 
      'plant species']
df = pd.read_csv('/content/drive/MyDrive/IRIS.csv',names=col,)
df.head()

df_proc = df[['sepal length', 'sepal width', 'petal length', 'petal width']]
scaler = MinMaxScaler()
scaler.fit(df_proc)
x = scaler.transform(df_proc)

pca = PCA(n_components=2)
pca.fit(x)
x_new = pca.transform(x)

df['comp1'] = x_new[:, 0]
df['comp2'] = x_new[:, 1]
df.head()

df_setosa = df[df['plant species'] == 'Iris-setosa']
df_versicolour = df[df['plant species'] == 'Iris-versicolor']
df_virginica = df[df['plant species'] == 'Iris-virginica']

from sklearn.cluster import DBSCAN
dbscan = DBSCAN(eps=3, min_samples=2) # по умолчанию eps=0.5, min_samples=5
clusters = dbscan.fit_predict(X)

from scipy.cluster import hierarchy
import matplotlib.pyplot as plt

ytdist = np.array([662., 877., 255., 412., 996., 295., 468., 268.,
                   400., 754., 564., 138., 219., 869., 669.])
Z = df_proc[['sepal length', 'sepal width', 'petal length', 'petal width']]
plt.figure()

import plotly.figure_factory as ff
import numpy as np
np.random.seed(1)
#X = np.random.rand(15, 12) 
fig = ff.create_dendrogram(Z)
fig.update_layout(width=800, height=500)
fig.show()

"""## Упражнение 2

Выполните агломеративную кластеризацию с помощью класса  [AgglomerativeClustering()](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html).
"""

clustering = AgglomerativeClustering().fit(Z)
clustering
AgglomerativeClustering()
clustering.labels_

"""## Упражнение 3
Визуализируйте результаты кластерного анализа. Для этого выберите 2 признака и постройте в их координатах точки согласно их разбивке на кластеры.
"""

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 3, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 42)

plt.scatter(df_setosa['sepal width'], df_setosa['sepal length'], 
label='Iris-setosa')
plt.scatter(df_versicolour['sepal width'], df_versicolour['sepal length'], 
label='Iris-versicolor')
plt.scatter(df_virginica['sepal width'], df_virginica['sepal length'], 
label='Iris-virginica')
plt.legend()
plt.show()