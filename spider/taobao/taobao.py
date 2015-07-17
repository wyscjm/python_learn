#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File:	taobao.py
Author: wyscjm
Email:	w079064@163.com
Github: https://github.com/wyscjm
Date:	2015-07-12
Ver:	V0.1
Description: 
    记录淘宝网址的一些功能
"""
import os
import ConfigParser
#import selenium
from selenium import webdriver

DEFAULT_PROJECT = os.path.join("/home/ww/github/python_learn/spider/",'taobao')
DEFAULT_CONFIG = os.path.join(DEFAULT_PROJECT,'my.config')

URL_LOGIN = "https://login.taobao.com/member/login.jhtml"



class Taobao(object):
    """
    淘宝网站相关
    """
    config = None
    browser = None
    def __init__(self):
        """构造函数"""
        self._init_config()
        self._init_web()
        
    def __del__(self):
        """析构函数"""

    def _init_web(self):
        """初始化浏览器
        """

    def _init_config(self):
        """初始化浏览器"""
        self.config = ConfigParser.RawConfigParser()
        self.config.read(DEFAULT_CONFIG)
        print self.config.sections()

    def update_coin_everyday(self):
        """
        获取淘金币每天
        """

if __name__ == '__main__':

    taobao = Taobao()

