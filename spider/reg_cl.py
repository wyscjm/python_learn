#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File:	reg_cl.py
Author: wyscjm
Email:	w079064@163.com
Github: https://github.com/wyscjm
Date:	2015-05-29
Ver:	V0.1
Description: 
    爬取邀请码
    注册
"""
import time
import os

DEFAULT_URL = "www.tieba.baidu.com"

class URL_Spider(Object):
    def en_url(self,url): 
        """ enter a url
        """
        print "enter:", url

    def get_link(self,url, msg):
        """get all link
        """
        links = []
        print links
        return links

class File_Spider(Object):
    file_dir = ""
    def set(self,dir):
        self.file_dir = dir

if __name__ == '__main__':
    count = 0
    while True:
        time.sleep(2)
        count += 1
        print count
        

