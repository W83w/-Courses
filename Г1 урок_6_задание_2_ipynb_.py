# -*- coding: utf-8 -*-
"""Урок 6 задание 2.ipynb"
# Упражнения на построение графиков

## Инструкция по выполнению задания
Ниже находится несколько  упражнений, представляющих собой код с пропущенными фрагментами, которые надо воспроизвести. Часть из этих упражнений очень простые, над некоторыми надо хорошенько подумать.
Чтобы выполнить это задание, нужно сохранить копию файла себе на Google Диск.
После выполнения задания, его нужно отправить на проверку. Для этого достаточно предоставить доступ к файлу и отправить ссылку в соответствующее поле LMS курса.
Удачи в выполнении заданий!

## Импортируем нужные библиотеки
"""

import matplotlib.pyplot as plt

"""### Упражнение 1

Построим линейный и точечный графики для данных, представленных ниже.

Для точечного графика помимо значений величины, график которой нужно построить (y), еще необходимо указать зависимую от нее величину (x). Поскольку нам она не дана в виде исходных данных, ее можно задать как целые число от 0 (или 1) до длины списка представленных данных.
"""

data = [10, 54, 47, 65, 18, 22, 15, 1]

plt.plot(data[0:])

"""### Упражнение 2

Для этого и последующих упражнений данного задания используем данные из [датасета](https://data.humdata.org/dataset/4aef17d7-92bf-4260-81fe-91e798eb1c11/resource/2f45efb7-c5ad-4332-b3d1-8087542a3801/download/wfp_food_prices_rus.csv). В нем содержится статистика по ценам на пшеницу в регионах России в разные годы. Файл следует загрузить в файловую систему виртуальной машины и прочитать, сохранив в датафрейм Pandas. 



"""

import pandas as pd
import numpy as np
the_price_of_wheat = pd.read_csv("/content/wfp_food_prices_rus.csv")
the_price_of_wheat

"""В датафрейме содержится информация по нескольким регионам. Давайте выделим отдельно данные по Ростовской области и Санкт-Петербургу."""

tp_rostov_sankt = the_price_of_wheat[the_price_of_wheat['admin1'].isin(['Rostovskaya Oblast', 'Sankt-peterburg'])]
tp_rostov_sankt

"""Давайте построим точечные графики цен на зерно в рублях для Ростовской области и Санкт-Петербурга. В качестве аргументов функции scatter() используем столбцы с датами и ценами."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

price_chart = tp_rostov_sankt.plot.scatter(x='price', y='date')

"""### Упражнение 3

Если данные из столбцов не преобразовывать, то окажутся строки и по оси Х и по оси У. Чтобы это исправить, преобразуйте столбец цен во [float](https://datatofish.com/convert-string-to-float-dataframe/), а столбец с датами [в формат дат](https://datatofish.com/strings-to-datetime-pandas/).
"""

the_price_of_wheat1 = the_price_of_wheat
#the_price_of_wheat1["price"] = the_price_of_wheat1["price"].astype(float)
price = tp_rostov_sankt.astype({'price': np.float})
price.info()
#date = tp_rostov_sankt.astype({'date': np.float})
#the_price_of_wheat['date'] = pd.to_datetime(the_price_of_wheat['date'], format='%Y%m%d-%H%M%S')

"""### Упражнение 4

Добавьте подписи величин по осям Х и У, а также заголовок диаграммы. 
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

price_chart = tp_rostov_sankt.plot.scatter(x='price', y='date')
plt.title("title")
plt.xlabel("xlabel")
plt.ylabel("ylabel")

"""### Упражнение 5
Добавьте легенду к графикам. Также измените тип маркеров для графиков. 
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

price_chart = tp_rostov_sankt.plot.scatter(x='price', y='date')
plt.title("title")
plt.xlabel("xlabel")
plt.ylabel("ylabel")
plt.plot([1,2,3,4])
plt.show()