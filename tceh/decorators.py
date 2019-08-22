# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 09:48:34 2019

@author: Lvov_AS
"""


'''
******************************************************************************


                        ЗАДАЧИ НА ДЕКОРАТОРЫ


******************************************************************************
'''
from functools import wraps, reduce
import datetime
import time


##############################################################################
def cancel_decorator(func):
    '''
    Декоратор, отменяющий выполнение любой декорированной функции
    '''
    @wraps(func)
    def cancel(*args, **kwargs):
        print('{} is cancelled!' .format(func.__name__))
    return cancel
##############################################################################


##############################################################################
def speedometer_decorator(func):
    '''
    Декоратор, который измеряет скорость выполнения функции
    '''
    @wraps(func)
    def speedometer(*args, **kwargs):
        start_moment = datetime.datetime.now()
        func(*args, **kwargs)
        end_moment = datetime.datetime.now()
        print('Function completed for {} seconds' .format(end_moment-start_moment))
    return speedometer
##############################################################################


##############################################################################
class Counter:
    '''
    класс для подсчета количества вызова функций со статичным методом подсчета
    '''
    dictionary={} #словарь, который будет хранить счетчики функций
    
    @staticmethod
    def counter_decorator(f):
        '''
        Декоратор, который считает сколько раз выполнялась функция
        '''
        @wraps(f)
        def counter_function(*args, **kwargs):
            if f.__name__ in Counter.dictionary.keys():
                Counter.dictionary[f.__name__]+=1
            else:
                Counter.dictionary[f.__name__]=1
            print('The function {} was called {} time(s)' .format(f.__name__,Counter.dictionary[f.__name__]))
            f(*args,**kwargs)
        return counter_function
##############################################################################


##############################################################################
def logger_decorator(func):
    '''
    Декоратор, который логгирует процесс выполнения функции
    '''
    @wraps(func)
    def log(*args, **kwargs):
        print('Декоратор создан!')
        time.sleep(1)
        print('Начато выполнение функции!')
        func(*args, **kwargs)
        time.sleep(1)
        print('Закончено выполнение функции!')
    return log
##############################################################################


##############################################################################
def exception_catcher_decorator(f):
    '''
    Декоратор, который ловит исключения
    '''
    @wraps(f)
    def exception_catcher(*args, **kwargs):
        try:
            f(*args,**kwargs)
        except Exception as ex:
            print('Exception {} detected' .format(ex))
    return exception_catcher
##############################################################################



@Counter.counter_decorator
@cancel_decorator
#@speedometer_decorator
#@logger_decorator
#@exception_catcher_decorator
def adding(*params):
    summ=0
    time.sleep(0.5)
    for n in params:
        summ+=n
    print('The sum is - ', summ)

@Counter.counter_decorator
#@cancel_decorator
@speedometer_decorator
@logger_decorator
#@exception_catcher_decorator
def multiplication(*params):
    mult=1
    time.sleep(1)
    for n in params:
        mult*=n
    print('The composition is - ', mult)
    
@Counter.counter_decorator
#@cancel_decorator
@speedometer_decorator
@logger_decorator
@exception_catcher_decorator
def somefunc(*params):
    some_sum=0
    for n in params:
        some_sum+=n
    print(some_sum)

if __name__=="__main__":
    adding(10,105,3,40)
    print('------------------------------------------')
    multiplication(2,6,45,72,25)
    print('------------------------------------------')
    multiplication(3,10,20)
    print('------------------------------------------')
    somefunc(2,4,6)
    #ЗАДАЧИ на map/filter/reduce/lambda
    print('------------------------------------------')
    print('При помощи map посчитать остаток от деления на 5 для чисел: [1, 4, 5, 30, 99]')
    mass1=[1,4,5,30,99]
    print(list(map(lambda x:x%5,mass1)))
    print('------------------------------------------')
    print('При помощи map превратить все числа из массива [3, 4, 90, -2] в строки')
    mass2=[3, 4, 90, -2]
    print(list(map(str,mass2)))
    print('------------------------------------------')
    print('При помощи filter убрать из массива [\'some\', 1, \'v\', 40, \'3a\', str] все строки')
    mass3=['some', 1, 'v', 40, '3a', str]
    print(list(filter(lambda a: type(a)!=str,mass3)))
    print('------------------------------------------')
    print('При помощи reduce посчитать количество букв в словах: [\'some\', \'other\', \'value\']')
    mass4=['some', 'other', 'value']
    print(reduce(lambda x,y:x+y,list(len(s) for s in mass4)))