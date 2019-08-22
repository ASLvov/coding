# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
import re
from read_write import read_file_w2

def date_location_text_parser(text):
    date_pattern=r'(\[.*/.*/.* ..:..:..])'
    location_pattern=r'(\[\D.*\D:\d*])'
    text_pattern=r'(\w* TABLE .*\n)'
    dates=re.findall(date_pattern, text)
    locations=re.findall(location_pattern,text)
    texts=re.findall(text_pattern,text)
    for index in range(len(dates)):
        print(dates[index], ':', locations[index], ':', texts[index])

def main():
    filename='ParseData.txt'
    text=read_file_w2(filename)
    date_location_text_parser(text)

if __name__=='__main__':
    main()
else:
    print('Something wrong!')