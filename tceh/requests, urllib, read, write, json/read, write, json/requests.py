# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 17:08:57 2019

@author: Lvov_AS
"""
'''
Реализовать следующую логику: получать при помощи requests данные сервиса 
https://jsonplaceholder.typicode.com/
(сущность можно выбрать любую, например:
https://jsonplaceholder.typicode.com/comments),
выводить в консоль все пары заголовки, сохранять полученный json в файл на диск

'''
import requests

__author__ = 'ASLvov'

'''def get_from_site(sitename):
    r = requests.get(sitename)
    print(r.status_code)
    print(r.headers)
    print(r.content)'''
    
def get_from_site(sitename):    
    r = requests.get(sitename)
    print(r.status_code, r.headers)
    print(r.content)
    
    # s = 'http://petstore.swagger.io/v2/pet/89?tags=string&filter=sad'
    
if __name__ == '__main__':
    site = 'https://jsonplaceholder.typicode.com/'
    get_from_site(site)
    #find_pet_by_tag('string')
    