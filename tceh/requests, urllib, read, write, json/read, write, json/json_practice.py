# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 15:53:07 2019

@author: Lvov_AS
"""

import json
from read_write import read_file_w2


if __name__=='__main__':
    data=read_file_w2('data.json')
    print('Raw data is ', data, type(data))
    print()
    
    #From string to object
    obj = json.loads(data)
    print(obj, type(obj))
    print()
    print(obj['object'], obj['boolean'])
    print()
    
    #From object to string
    print('dumping object to text:')
    obj['new-value'] = 'secret'
    print(json.dumps(obj, sort_keys=True, indent=4))
    