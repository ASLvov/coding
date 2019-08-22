# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 09:58:54 2019

@author: Lvov_AS
"""

import urllib
import urllib2

__author__= 'ASLvov'

def get_habrahabr():
    response = urllib2.urlopen('http://habrahabr.ru/')
    print(response.code)
    print(response.info())
    html = response.read()
    response.clode()
    
    print(html)
    
def find_pet_by_tag(tag):
    url = 'http://petstore.swagger.io/v2/pet/findByTags'
    query_args = {'tags': tag}
    data = urllib.urlencode(query_args)
    full_url = '{}?{}'.format(url,data)
    print(full_url)
    
    request = urllib2.Request(full_url, headers={
            'Accept': 'application/json'
            # 'Accept': 'application/xml'
            })
    response = urllib2.urlopen(request)
    print(response.info())
    print(response.read())
    response.close()
    
if __name__ == '__main__':
    #get_habrahabr()
    find_pet_by_tag('string')