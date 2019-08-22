# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:07:55 2019

@author: Lvov_AS
"""

'''

Игра в пятнашки. 

Игровое поле 4х4, числа от 1 до 15 в клетках и одна пустая клетка. Вначале игры
все клетки перемешиваются случайным образом. Пользователю необходимо переместить
числа таким образом, чтобы они расположились по порядку от меньшего к большему, а
пустая клетка оказалась в правом нижнем углу поля.
Для перестановки клеток нужно использовать клавиши:
'w' - вверх
's' - вниз
'a' - влево
'd' - вправо

Выходить за пределы поля нельзя!
После каждого хода поле должно отрисовываться заново, должна выполняться проверка окончания игры.


''' 
import random
import pandas as pd
from IPython.display import clear_output

def create_field (s=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,' ']):
    random.shuffle(s)
    new_field=['','','','']
    j=0
    for i in range(0,4):
        new_field[i]=[s[j],s[j+1],s[j+2],s[j+3]]
        j+=4
    return new_field

def check_win(live_field, model=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,' ']]):
    if live_field==model:
        print("Вы выиграли!")
        return True
    else: 
        return False
    
def draw_field(live_field):
    df=pd.DataFrame(data=live_field, columns=['','','',''], index=['','','',''])
    print(df)
    
def check_possible(field,step):
    for i in range(4):
        for j in range(4):
            if field[i][j]==' ':
                a=i
                b=j
    if (a==0 and step=='w') or (a==3 and step=='s') or (b==0 and step=='a') or (b==3 and step=='d'):
        print("Неверный шаг")
        return False
    else:
        return True
        

def game(live_field):
    step=input("Ваш шаг: ")
    if step=="End":
        raise Exception
    if check_possible(live_field,step):
        for i in range(4):
                for j in range(4):
                    if live_field[i][j]==' ':
                        a=i
                        b=j
        if step=="w":
            live_field[a][b]=live_field[a-1][b]
            live_field[a-1][b]=' '
        elif step=="s":
            live_field[a][b]=live_field[a+1][b]
            live_field[a+1][b]=' '
        elif step=="a":
            live_field[a][b]=live_field[a][b-1]
            live_field[a][b-1]=' '
        elif step=="d":
            live_field[a][b]=live_field[a][b+1]
            live_field[a][b+1]=' '
        else:
            print("Для перестановки клеток нужно использовать клавиши: 'w' - вверх; 's' - вниз; 'a' - влево; 'd' - вправо")
        draw_field(live_field)
    

field=create_field()
draw_field(field)

while check_win(field)!= True:
    try:
        game(field)
    except Exception:
        print("Вы завершили игру!")
        break

    
