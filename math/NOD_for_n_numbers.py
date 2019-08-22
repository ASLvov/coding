import math
from collections import Counter

# Функция разложения числа на произведение простых чисел
def prost (x):
    res=[]
    for i in range(2,int(math.sqrt(x))+1):
        while x%i==0:
            res.append(i)
            x=x/i
    if x!=1: res.append(int(x))
    return res

# Ввод первончальных данных: количество чисел и сами числа
my_list=[]
size=int(input('Введите количество элементов - '))
for i in range(1,size+1):
    n=int(input('Число ' + str(i) + ' - '))
    my_list.append(n)


# Разложение введенных чисел на простые
razl=[]
for i in range(size):
    razl.append(prost(my_list[i]))

# Поиск пересечений в получившихся списках
common_items = list((Counter(razl[0]) & Counter(razl[1])).elements())
if size>2:
    for i in range(2,size):
        common_items = list((Counter(razl[i]) & Counter(common_items)).elements())

# Собственно нахождение НОД
NOD=1
for i in range(len(common_items)):
    NOD=NOD*common_items[i]

print('Наибольший общий делитель равен: ', NOD)
