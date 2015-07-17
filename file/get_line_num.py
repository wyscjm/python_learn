#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File:	get_line_num.py
Author: wyscjm
Email:	w079064@163.com
Github: https://github.com/wyscjm
Date:	2015-05-14
Ver:	V0.1
Description: 
    get all file's line num under a dir
"""
import os

def get_file(dir):
    files = []
    if os.path.isdir(dir):
        for parent,dirnames,filenames in os.walk(dir):
            for filename in filenames:
                file = os.path.join(parent,filename)
                files.append(file)
                print file
    print "file num:", len(files)
    return files
    print "get_file"

def get_num(file):
    num = 0
    file_object = open(file)
    lines = file_object.readlines()
    num = len(lines)
    return num
    print "file num is:"

def get_resume():
    files = get_file("/home/ww/project/resumefactory")
    total_line_num = 0
    for file in files:
        total_line_num += get_num(file)
    print "resum total_line_num:", total_line_num



if __name__ == '__main__':
    get_resume()
    
