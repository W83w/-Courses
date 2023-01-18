# -*- coding: utf-8 -*-
"""задание 8 3 "OpenCV2.ipynb"
# Упражнения на маски и зоны интереса
## Инструкция по выполнению задания
Ниже находится несколько  упражнений, представляющих собой код с пропущенными фрагментами, которые надо воспроизвести. Часть из этих упражнений очень простые, над некоторыми надо хорошенько подумать.
Чтобы выполнить это задание, нужно сохранить копию файла себе на Google Диск.
После выполнения задания, его нужно отправить на проверку. Для этого достаточно предоставить доступ к файлу и отправить ссылку в соответствующее поле LMS курса.
Удачи в выполнении заданий!
## Немного теории
Обработка изображений, особенно методами машинного обучения может требовать немало ресурсов, особенно, если мы работаем с видеопотоками в режиме реального времени. Кроме того, иногда важные элементы на изображении располагаются в определенной его части, в то время как остальная часть изображения не играет особой роли для нашей задачи. Тогда принято выделять эту интеересующую часть изображения и обрабатывать именно ее. Эту часть принято называть областью интереса (ROI, Region of Interest). 

И наоборот, иногда какую-то часть изображения нужно изолировать, чтобы алгоритмы не обрабатывали ее. Например, у представим себе систему мониторинга лесных пожаров, которая с помощью видеокамер, установленных на вышках сотовой связи, фиксирует наличиее задымления над лесом. И где-то вдалеке начинается поселок, где расположена котельная, отапливающаая поселок. Выбросы из трубы котельной не должны приводить к срабатыванию системы, поэтому на область изображения из видеопотока накладывают маску - пиксели этой части изображения заменяются ккаким-либо нейтральным цветом прежде чем кадр попадает на обработку в основной алгоритм системы мониторинга.
В этом задании мы научимся выделять и видоизменять области интереса, а также закрывать (закрашивать) масками определенные части изображения.
Для этого нам понадобится библиотека OpenCV и понимание того, что из себя представляет массив пикселей изображения.
## Импортируем библиотеки
"""

from google.colab import drive
drive.mount('/content/drive')

import cv2 # импортируем OpenCV
from matplotlib import pyplot as plt # импортируем matplotlib
import numpy as np # импортируем numpy
from google.colab import drive
from matplotlib.image import imread
from google.colab.patches import cv2_imshow

"""### Упражнение 1
Займемся областью интереса. Загрузите цветное изображение [мема](https://drive.google.com/file/d/1DyexyEJ1YNY8S5ayib1_ZxBopevYZt97/view?usp=sharing) и выведите его на экран средствами openCV и matplotlib. Помните, что по умолчанию библиотека openCV цветное изображение воспринимает как BGR (картинка будет выглядеть синей, скорее всего), а не RGB. Для нормального отображения нужно дополнительно преобразовать цветовую схему.
"""

img_harre = cv2.imread('/content/drive/MyDrive/harre.jpg')
img_harre_color = cv2.cvtColor(img_harre, cv2.COLOR_BGR2RGB)
plt.imshow(img_harre_color)

"""### Упражнение 2
Сделаем лицо Гарри Поттера областью интереса. Подберите вручную координаты области и выведите эту область в виде отдельного изображения.

Помните, что при указании координат в изображении с помощью квадратных скобок сперва идут строки, а потом столбцы, т.е. сперва значения У, а уже потом Х.
"""

from google.colab.patches import cv2_imshow
img_harre_color = cv2.imread('/content/drive/MyDrive/harre.jpg')
img_color_picture = cv2.cvtColor(img_harre_color, cv2.COLOR_BGR2RGB)

img_harre = img_harre_color[270:430, 330:450]
cv2_imshow(img_harre)

"""### Упражнение 3
Теперь давайте изменим значения пикселей в области интереса. Сделайте так, чтобы область интереса на изображении мема стала черно-белой, а все остальные пиксели остались прежними.

Помните, что черно-белое (в оттенках серого) изображение содержит по одному числу для характеристики цвета пикселя, в то время как цветное изображение имеет три числа. Чтобы поместить черно-белое изображение в область интереса цветной картинки, нужно, чтобы размерность массивов совпадала.
"""

img_harre_gray = cv2.cvtColor(img_harre, cv2.COLOR_RGB2GRAY)
img_bgb_gray= cv2.cvtColor(img_harre_gray, cv2.COLOR_BGR2RGB)
cv2_imshow(img_bgb_gray)

for i in range(0, img_bgb_gray.shape[0]):
  for j in range(img_bgb_gray.shape[1]):
    img_harre_color[i-800][j-500] = img_bgb_gray[i][j]
plt.imshow(img_harre_color)

"""### Упражнение 4
Если справились с предыдущим упражнением, то давайте получим противоположную картинку: черно-белое изображение с цветной областью интереса.
"""

img_scene_gray = cv2.cvtColor(img_harre_color, cv2.COLOR_RGB2GRAY)
img_scene_bgb = cv2.cvtColor(img_scene_gray, cv2.COLOR_BGR2RGB)
plt.imshow(img_scene_bgb)

img_harreyforcolorfase = cv2.imread('/content/drive/MyDrive/harre.jpg')
img_harreyforcolorfase = cv2.cvtColor(img_harreyforcolorfase, cv2.COLOR_BGR2RGB)
img_harrefasecolor = img_harreyforcolorfase[270:430, 330:450]

#img_harry_brg = cv2.cvtColor(img_harreyforcolorfase, cv2.COLOR_RGBA2BGR)

for i in range(0, img_harrefasecolor.shape[0]): 
  for j in range(img_harrefasecolor.shape[1]):
    img_scene_bgb[i-800][j-500] = img_harrefasecolor[i][j]
plt.imshow(img_scene_bgb)

"""### Упражнение 5
Перейдем к маскам. Часто можно встретить маски на трансляциях уличных веб-камер. Там они обычно закрывают рекламные билборды. Давайте и мы с вами закроем билборды на [изображении](https://www.volgatech.net/upload/iblock/caa/ilg0anu3c0oxofqlvr3to72a0ws3ag2m.png). Закрасьте два билборда черным цветом. Выведите результат.
"""

billboard = cv2.imread('/content/drive/MyDrive/Bilbord.jpg')
billboard = cv2.cvtColor(billboard, cv2.COLOR_BGR2RGB)
plt.imshow(billboard)

cv2.rectangle(billboard, (150, 200), (520, 400), (0, 0, 0), -1)
cv2.rectangle(billboard, (650, 350), (900, 500), (0, 0, 0), -1)
plt.imshow(billboard)