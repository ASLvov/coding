# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 15:53:45 2019

@author: Lvov_AS
"""

from flask import Flask

app=Flask(__name__)

@app.route('/hello/<user>')
def home(user):
    return 'Hello my friend ' + user + '!'

@app.route('/add/<a>/<b>')
def add(a,b):
    answer=int(a)+int(b)
    return 'The sum is ' + str(answer)

@app.route('/longstr/<str1>/<str2>/<str3>')
def longstr(str1, str2, str3):
    dc={len(str1):str1, len(str2):str2, len(str3):str3}
    index=max(len(str1),len(str2),len(str3))
    return 'The longest word is: ' + dc[index]

@app.route('/file/<path:filename>')
def if_file(filename):
    pref='Yes, I can open file: ' + filename + '\n'
    try:
        with open(filename) as f:
            pref+=f.read()
            print(pref)
            return pref
    except:
        return 'There is no such file or directory'
    


if __name__=='__main__':
    app.run()