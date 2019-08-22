# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 21:28:51 2019

@author: Александр
"""
'''
**************************************************************


                        RANDOM GENERATOR


**************************************************************
'''

import random

def gen(a,b,c): #Generator, where a - min value, b - max value, c - quantity of number
    some=0
    while some<c:
        some+=1
        yield random.randrange(a,b)
        

        
'''
**************************************************************


                        RANGE GENERATOR


**************************************************************
'''        
def generator_range(a,b,c=1): #Generator, where a - start, b - stop, c - step
    while a<b:
        yield a
        a+=c
    
'''
**************************************************************


                        MAP GENERATOR


**************************************************************
'''      
def map_generator(func, somelist):
    for n in somelist:
        yield func(n)

'''
**************************************************************


                        ENUMERATE GENERATOR


**************************************************************
''' 
def enumerate_generator(somelist):
    index=0
    for n in somelist:
        yield (index,n)
        index+=1
        
'''
**************************************************************


                        ZIP GENERATOR


**************************************************************
''' 
def zip_generator(list1, list2):
    for n in range(len(list1)):
        yield (list1[n],list2[n])
        

if __name__=='__main__':
    summary1=[]
    summary2=[]
    summary3=[]
    summary4=[]
    
    rand=gen(1,10000,5)
    while True:
        try:
            x=next(rand)
            summary1.append(x)
        except:
            print('The result of random generator is: \n{}\n' .format(summary1))
            break
    
    my_range=generator_range(1,6,1)
    while True:
        try:
            x=next(my_range)
            summary2.append(x)
        except:
            print('The result of range generator is:\n{}\n' .format(summary2))
            break 
    
    
    my_map=map_generator(lambda x: x*x, summary2)
    while True:
        try:
            x=next(my_map)
            summary3.append(x)
        except:
            print('The result of map generator is:\n{}\n' .format(summary3))
            break
    
    my_enum=enumerate_generator(summary3)
    while True:
        try:
            x=next(my_enum)
            print('The element with index {} is {}' .format(x[0],x[1]))
        except:
            print()
            break
    
    my_zip=zip_generator(summary3,summary2)
    while True:
        try:
            x=next(my_zip)
            summary4.append(x)
        except:
            print('The result of zip generator is:\n{}\n' .format(summary4))
            break