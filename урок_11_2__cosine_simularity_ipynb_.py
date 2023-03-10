# -*- coding: utf-8 -*-
"""Урок 11 2 "cosine simularity.ipynb"

Automatically generated by Colaboratory.


# Упражнения на определение косинусного сходства

## Инструкция по выполнению задания
Ниже находится несколько  упражнений, представляющих собой код с пропущенными фрагментами, которые надо воспроизвести. Часть из этих упражнений очень простые, над некоторыми надо хорошенько подумать.

Чтобы выполнить это задание, нужно сохранить копию файла себе на Google Диск.
После выполнения задания, его нужно отправить на проверку. Для этого достаточно предоставить доступ к файлу и отправить ссылку в соответствующее поле LMS курса.
Удачи в выполнении заданий!

### Для определения косинусного сходства воспользуемся библиотекой [textdistance](https://pypi.org/project/textdistance/)
Чтобы выполнить определение косинусного расстояния необходимо вызвать функцию cosine из этой библиотеки. В качестве аргументов она принимает токенизированные последовательности слов двух текстов.
"""

!pip install textdistance
import nltk
nltk.download('punkt')
!pip install pymorphy2
import pymorphy2
import re
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

import textdistance

"""### Тексты для сравнения"""

text1 = 'Алгоритмы сравнения текстов используется для борьбы с плагиатом'
text2 = 'Сравнение двух текстов показало, что они отличаются по стилистике, объему и отношению авторов к проблеме'

"""### Упражнение 1
Выполним определение косинусного сходства для двух текстов. Для этого выполним уже знакомую  последовательность действий из предыдущих заданий: токенизируйте тексты, преобразуйте к нижнему регистру, удалите стоп-слова, лемматиризуйте.
Полученные токенизированные последовательности пропустите через соответствующую функцию из библиотеки textdistance.
"""

from nltk.corpus import stopwords
morph = pymorphy2.MorphAnalyzer()
tokenizedtext1 = []
tokenizedtext2 = []
for i in text1:
  tok_sen = ''
  txt = re.findall(r'[а-я]+', i.lower())
  for j in txt:
    if j not in stopwords.words('russian'):
      w = morph.parse(j)[0].normal_form
      if tok_sen == '':
        tok_sen += w
      else:
        tok_sen += (' ' + w)
  tokenizedtext1.append(tok_sen)

for i in text2:
  tok_sen = ''
  txt = re.findall(r'[а-я]+', i.lower())
  for j in txt:
    if j not in stopwords.words('russian'):
      w = morph.parse(j)[0].normal_form
      if tok_sen == '':
        tok_sen += w
      else:
        tok_sen += (' ' + w)
  tokenizedtext2.append(tok_sen)


similarity = textdistance.hamming.normalized_similarity(tokenizedtext1, tokenizedtext2)
similarity

"""### Упражнение 2
Косинусное сходство может быть определено и между отдельными словами. Показатель может оценивать минимальное расстояние редактирования (сколько замен букв надо сделать в одном слове, чтобы получить другое) или семантическое расстояние между словами. Расстояние редактирования не особо важно для понимания смыла текста машиной. Поэтому найдем семантическое расстояние. Для этого используем библиотеку gensim. Сравним слова "алгоритм" и "программа" (что-то относительно близкое по смыслу), а также "алгоритм" и "посуда" (понятия абсолютно из разных сфер).

Для определения схожести используйте метод similarity(), на вход которого подайте проверяемые слова. Только учтите, что аргументы должны иметь вид u'слово_ЧАСТЬ РЕЧИ'. Знаете как части речи называются на английском?
"""

import gensim.downloader as api

model = api.load("word2vec-ruscorpora-300")

similarity1 = textdistance.hamming.normalized_similarity('алгоритм', 'программа')
similarity1

similarity2 = textdistance.hamming.normalized_similarity('алгоритм', 'посуда')
similarity2

