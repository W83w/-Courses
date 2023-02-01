# -*- coding: utf-8 -*-
"""г2 у5 з3.ipynb



Ссылка на сайт
"""

#https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/

link = 'https://pro-katalog.ru/category/noutbuki'

import requests

cookies = {
    '_ym_uid': '1616661207763271544',
    '_ym_d': '1663424427',
    '__ddg1_': '83Ffnluv63rwe2MHhPNO',
    'tmr_lvid': 'ec909d6bd0626bcb7353ff87094f443c',
    'tmr_lvidTS': '1616661206317',
    '_ga': 'GA1.2.1283363942.1666370669',
    'tmr_detect': '1%7C1667230005197',
    '_gid': 'GA1.2.1931147048.1667230005',
    '_ym_isad': '1',
    'tmr_reqNum': '337',
}

headers = {
    'authority': 'pln-pskov.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_ym_uid=1616661207763271544; _ym_d=1663424427; __ddg1_=83Ffnluv63rwe2MHhPNO; tmr_lvid=ec909d6bd0626bcb7353ff87094f443c; tmr_lvidTS=1616661206317; _ga=GA1.2.1283363942.1666370669; tmr_detect=1%7C1667230005197; _gid=GA1.2.1931147048.1667230005; _ym_isad=1; tmr_reqNum=337',
    'referer': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}

response = requests.get(link, cookies=cookies, headers=headers)

import pandas as pd
import requests
import bs4

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"} # информация для сервера

r = requests.get(link,  headers=headers) # запрос
print(r) # если ответ на запрос имеет код 200, то все хорошо
regions = bs4.BeautifulSoup(r.text) #создаем объект, где будет информация с сайта

print(type(regions.text))
regions.text

"""Получил модели ноутбуков

"""

models_netbooc = regions.find_all('span', {'class': 'product-list-item-info__title'})
print(models_netbooc)
print(type(models_netbooc))

#product-item__prices

"""Получил характеристики ноутбуков

"""

specifications = regions.find_all('span', {'class': 'features-list-item__value'})
print(specifications)
print(type(specifications))

prise = regions.find_all('div', {'class': 'offers-price-list-item'})
print(prise)
print(type(prise))

"""Теперь получу стоимость из разных магазинов """

prise = regions.find_all('span', {'class': 'offers-price-list-item__value'})
print(prise)
print(type(prise))

"""Вывожу 1 элемент что бы проверить подходят ли данные"""

from tables import link
print(type(models_netbooc[0].text))
models_netbooc[0].text

from tables import link
print(type(specifications[0].text))
specifications[0].text

d = 0
spisok = []
spisok1 = []
for i in specifications:
  spisok.append(i)
  if len(spisok) >= 5:
    spisok1.append(spisok)
    spisok.clear

spisok1

from tables import link
prise[0].text

"""Модели ноутбуков"""

#from requests.auth import models
from re import T
sort = ['/', '/', '/news/', '/maps/', '/informers/', '/soft/', '/catalog/', '\n']
models_b = []
for i in range(len(models_netbooc)):
  if i in sort:
    pass
  else:
    models_b.append(models_netbooc[i].text)
print(models_b)
print(len(models_b))

"""Хочу обединть спецификации"""

from re import T
sort = ['/', '/', '/news/', '/maps/', '/informers/', '/soft/', '/catalog/', '\n']
specifications_ = []
for i in range(len(specifications)):
  if i in sort:
    pass
  else:
    specifications_.append(specifications[i].text)
#print(specifications_)
#print(type(specifications_))
#print(len(specifications_))


d = 0
spisok = []
processor = []
specifications_sort = []
screen_resolution = []
RAM = []
Drive = []
OS = []
Laptop_weight = []
for i in specifications_:
  spisok.append(i)
  #if len(spisok) >= 5:
    #specifications_sort.append(spisok)
    #print(len(specifications_sort))
    #spisok.clear
  
  for ii in spisok:
    if ii == spisok[0]:
      screen_resolution.append(spisok[0])
    elif ii == spisok[1]:
      processor.append(spisok[1])
    elif ii == spisok[2]:
      RAM.append(spisok[2])
    elif ii == spisok[3]:
      Drive.append(spisok[3])
    elif ii == spisok[4]:
      OS.append(spisok[4])
    elif ii == spisok[5]:
      Laptop_weight.append(spisok[5])
      #print(len(specifications_sort))
      spisok.clear()
      


#specifications_sort

screen_resolution

sort = ['/', '/', '/news/', '/maps/', '/informers/', '/soft/', '/catalog/', '\n']
prise_shop = []
shop = []
for i in range(len(prise)):
  #print(links[i].text)
  prise_shop.append(prise[i].text)
print(prise_shop)
print(type(prise_shop))
str(prise_shop)

clear_prise = []
for i in prise_shop:
  if i in sort:
    pass
  else:
    clear_prise.append(i) 
print(len(clear_prise))


spisok = []
prise_sort = []
for i in clear_prise:
  spisok.append(i)
  if len(spisok) >= 5:
    prise_sort.append(spisok)
    spisok.clear

prise_sort

Laptop_weight

processor

from pandas.core.groupby.groupby import F
from re import split
netbook_praise = []
b = 0 
j = 0
g = 0
p = 0
for pp in range(15):
  for i in range(70):
    j = j+1
    g = g +1
    p = p + 1
    netbook_praise.append([models_b[p],processor[i], screen_resolution[i],RAM[j],
                         Drive[p], OS[0],Laptop_weight[p],clear_prise[j]])
    if j == 15:
      j = 0
    if g == 70:
      g = 0
    if p == 10:
      p = 0
#for i in range(len(videocart)): 
  #for j in range(len(clear_prise)):
    #for g in range(len(specifications_sort)):
      #if i == j and j== g:
        #netbook_praise.append([videocart[i], clear_prise[j], specifications_sort[g]])
      #else:
        #pass
print(netbook_praise)

columns = ['прозводитель','модель_процессора', 'разрешение', 'Оперативная_память', 'Носмтель', 'ОС', 'Вес', 'Цена']
values  = [netbook_praise[0]]
values

table = pd.DataFrame(data = netbook_praise, columns=columns)
table

compression_opts = dict(method='zip',
                        archive_name='region.csv')  
table.to_csv('region.zip', index=False,
          compression=compression_opts)