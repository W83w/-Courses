# -*- coding: utf-8 -*-
"""Копия блокнота "ifcycle.ipynb"

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12caEA5_RKqTJyDnM-FY71_qCIimUZx76

# Упражнения на знания условий и циклов

## Инструкция по выполнению задания

Ниже находится несколько  упражнений, представляющих собой код с пропущенными фрагментами, которые надо воспроизвести. Часть из этих упражнений очень простые, над некоторыми надо хорошенько подумать. 

Чтобы выполнить это задание, нужно сохранить копию файла себе на Google Диск.


После выполнения задания, его нужно отправить на проверку. Для этого достаточно предоставить доступ к файлу и отправить ссылку в соответствующее поле LMS курса.




Удачи в выполнении заданий!

### Упражнение 1
Исправьте ошибки в коде программы, чтобы она заработала
"""

if 5 > 3:
    print('True')

"""### Упражнение 2
Поменяйте else на elif, чтобы последняя ветвь условия работала также, как с else
"""

x = 5
y = 2
if x < 6:
  print('сработало первое условие')
elif x % y == 1:
  print('сработало второе условие')
elif x % y > 2 or x >= 6:
  print('остался else')

"""### Упражнение 3
Напишите цикл, который выводит на экран каждый второй элемент списка
"""

every2ndElement = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
for i in every2ndElement:
    if i % 2 == 0:
        print(i)

"""### Упражнение 4
Переделайте программу так, чтобы она работала также, но в основе был цикл while вместо for
"""

fromForToWhile = []
i = 0
while len(fromForToWhile) < 10:
    i = i + 1
    fromForToWhile.append(i)
print(fromForToWhile)

"""### Упражнение 5
Программа ниже прекратит свое выполнение с ошибкой. Добавьте условие, чтобы избежать появление ошибки. Изменять содержимое списка нельзя 
"""

someList = [8, 15, 6, 67, 0, 13, 1, 34]
for i in someList:
    try:
        print(1/i)
    except:
        print('ошибка')