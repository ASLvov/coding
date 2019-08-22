# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 14:44:08 2019

@author: Lvov_AS
"""

'''
**********************************************
THE FIRST WAY OF READING
**********************************************
'''
def read_file_w1(filename):
    try:
        f=open(filename)
        print('There is a text from file \'{}\':\n' .format(filename))
        content=f.read()
        f.close()
    except:
        return 'Something goes wrong!'
    return content

'''
**********************************************
THE SECOND WAY OF READING
**********************************************
'''
def read_file_w2(filename):
    with open(filename) as f:
        return f.read()

'''
**********************************************
THE WAY  OF WRITING
**********************************************
'''
def write_to_file(filename, content, mode='w'):
    with open(filename, mode=mode) as f:
        return f.write(content)
    


def main():
    name_of_file='textfile.txt'
    text=read_file_w1(name_of_file)
    print(text)
    
    write_to_file(name_of_file, text)
    write_to_file(name_of_file, '\nsome new line', 'a')

    
if __name__=='__main__':
    try:
        main()
    except:
        print('Something goes wrong!')