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
import json
from read_write import write_to_file

__author__ = 'ASLvov'

def get_headers_from_site(sitename):
    r = requests.get(sitename)
    if r.status_code==200:
        headers_dict=dict(r.headers)
        for index, value in headers_dict.items():
            print(index, ':', value)
        return json.dumps(headers_dict, sort_keys=True, indent=4)

if __name__ == '__main__':
    site = 'https://jsonplaceholder.typicode.com/comments/'
    headers_data=get_headers_from_site(site)
    write_to_file('datafile.json', headers_data)