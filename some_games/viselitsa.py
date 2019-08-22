# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 10:25:27 2019

@author: Lvov_AS
"""
import random

WORDS=[
       'виселица',
       'слово',
       'человек'
       ]

MAX_ERRORS=8

def select_random_word():
    return random.choice(WORDS)

def get_status(word):
    statuses=[]
    for letter in word:
        statuses.append(False)
    return statuses

def print_the_word(statuses, word):
    for index, letter in enumerate(word):
        if statuses[index]:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()
    
def is_finished(statuses, errors_counter):
    if errors_counter>=MAX_ERRORS:
        return True
    
    for status in statuses:
        if not status:
            return False
    return True

def is_guessed(letter,word,statuses):
    if letter not in word:
        return False
    for index, l in enumerate(word):
        if letter==l:
            statuses[index]=True
    return True
    
def main():
    word=select_random_word()
    statuses=get_status(word)
    errors_counter=0
    print_the_word(statuses, word)
    while not is_finished(statuses, errors_counter):
        print('Осталось ', MAX_ERRORS-errors_counter, ' ошибок')
        letter=input('Введите букву: ')
        if not is_guessed(letter, word, statuses):
            errors_counter+=1
        print_the_word(statuses, word)
            
    if errors_counter>=MAX_ERRORS:
        print('Вы проиграли!')
    else:
        print('Вы выиграли!')


main()