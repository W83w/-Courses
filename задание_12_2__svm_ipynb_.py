# -*- coding: utf-8 -*-
"""Задание 12 2 "SVM.ipynb"

Automatically generated by Colaboratory.


# Создание модели методом опорных векторов
## Инструкция по выполнению задания
Ниже находится несколько  упражнений, представляющих собой код с пропущенными фрагментами, которые надо воспроизвести. Часть из этих упражнений очень простые, над некоторыми надо хорошенько подумать.

Чтобы выполнить это задание, нужно сохранить копию файла себе на Google Диск.

После выполнения задания, его нужно отправить на проверку. Для этого достаточно предоставить доступ к файлу и отправить ссылку в соответствующее поле LMS курса.
Удачи в выполнении заданий!
### Импортируем необходимые для выполнения упражнейний библиотеки
В качестве примера для реализации алгоритма классификации методом опорных векторов используем стандартный [датасет Ирисов Фишера](https://ru.wikipedia.org/wiki/%D0%98%D1%80%D0%B8%D1%81%D1%8B_%D0%A4%D0%B8%D1%88%D0%B5%D1%80%D0%B0). Этот датасет есть в модуле datasets библиотеки sklearn.
"""

from sklearn.svm import SVC
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

import numpy as np
from sklearn.pipeline import make_pipeline

iris = datasets.load_iris()
x = iris.data # признаки для модели
y = iris.target # целевая функция

"""## Упражнение 1
Создайте модель как объект класса [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)
"""

from sklearn.svm import SVC
clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
clf.fit(x, y)

clf = SVC() 
clf.fit(x, y)
SVC()
clf.support_vectors_
clf.support_
clf.n_support_

"""## Упражнение 2
Подготовьте данные, разделив их на обучающую и проверочную выборки (функция train_test_split())
"""

sc = StandardScaler()
x_sc = sc.fit_transform(x)
#x_train, x_test, y_train, y_test = train_test_split(x_sc, y, test_size=0.2)
#y_test
x_train, x_test, y_train, y_test = train_test_split(x_sc, y, test_size=0.2, random_state=42)

"""## Упражнение 3
Обучите модель (метод fit()).
"""

model = LinearRegression()
model.fit(x_train, y_train)
pred = model.predict(x_test)
print(pred[0], y_test[0])

x_test[0]

"""## Упражнение 4
Выведите получившиеся опорные вектора на экран. Используйте для этого свойство support_vectors_ обученной модели.
"""

clf.support_vectors_
clf.support_
clf.n_support_

pred = model.predict(x_test)
pred[0], y_test[0]
clf.support_vectors_

"""## Упражнение 5
Проверьте работу модели на тестовых данных. 
"""

from sklearn.metrics import mean_absolute_percentage_error
from sklearn.tree import DecisionTreeRegressor

pred = model.predict(x_test)
mean_absolute_percentage_error(y_test, pred)

modeltree = DecisionTreeRegressor(max_depth=2)
modeltree.fit(x_train, y_train)

predtree = modeltree.predict(x_test)
mean_absolute_percentage_error(y_test, predtree)

"""## Упражнение 6
Используйте метрики [доли верных ответов](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html), [точности](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html) и [полноты](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html), чтобы оценить работу модели на тестовых данных
"""

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.tree import plot_tree 
from sklearn.tree import DecisionTreeRegressor
from sklearn import datasets

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import plot_precision_recall_curve
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
import matplotlib.pyplot as plt
from sklearn import metrics

from sklearn.metrics import accuracy_score
from sklearn.metrics import make_scorer
scoring = {'accuracy': make_scorer(accuracy_score),
           'prec': 'precision'}
scoring

modeltree = DecisionTreeRegressor(max_depth=2)
mean_absolute_percentage_error(y_test, predtree)
#precision = precision_score(y_test, predtree)