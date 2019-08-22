# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:24:55 2019

@author: Lvov_AS
"""

'''
TODO:
Обратиться с странице https://habrahabr.ru/. Получить текст страницы.
При помощи регулярных выражений нужно получить все ссылки со страницы на другие.
Ответить себе на вопрос удобно ли так делать?
'''

import requests
import re
from read_write import write_to_file

def get_site_text(sitename):
    r = requests.get(sitename)
    if r.status_code==200:
        return r.text

def get_links_with_regular(content):
    link_pattern=r'href="(.*?)"'
    write_to_file('links_from_site.txt', str(re.findall(link_pattern,content,flags=re.IGNORECASE)))
    print('Finished!')
    
def main():
    print('Print url to start:')
    sitename=input()
    content=get_site_text(sitename)
    get_links_with_regular(content)
    
if __name__=='__main__':
    main()
else:
    print('Something goes wrong, shutting down!')
