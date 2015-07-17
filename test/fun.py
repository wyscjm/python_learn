#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File:	fun.py
Author: wyscjm
Email:	w079064@163.com
Github: https://github.com/wyscjm
Date:	2015-06-25
Ver:	V0.1
Description: 
    test eval
"""

def _get_dict(d , name):
    if type(d)  == type({}):
        if name in d.keys():
            print dict[name]
            return dict[name]
        else:
            return None
    else:
        return None

f = open('fun.txt','r')
date = f.read()
f.close()

#dict = {"name":"ww", "salary2":"33"}


#print dict["name"]

dict = {"name":"ww", "salary2":"33"}
eval(date)

dict = ["name","ww"]
eval(date)


    



