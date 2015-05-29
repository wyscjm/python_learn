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
import ConfigParser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

#DEFAULT_URL = "www.tieba.baidu.com"
DEFAULT_URL = "http://tieba.baidu.com/f?kw=%CE%D2%D3%FB%B7%E2%CC%EC&fr=index"

def wait(ntime):
    """等候
    """
    time.sleep(ntime)

def open_url(browser, url):
    """打开网页
    """
    assert(browser and url)

    try:
        browser.get(url)
    except Exception, message:
        raise message

def check_control(browser, control_name, tag="name", timeout=1):
    """检查控件是否存在
    """
    assert(tag in ["name", "id", "class_name", "link_text", "css_selector"])
    assert(browser and control_name)

    try:
        ###判断是否存在control元素
        if tag == "name":
            WebDriverWait(browser, timeout).until(lambda x: x.find_element_by_name(control_name))
        elif tag == "id":
            WebDriverWait(browser, timeout).until(lambda x: x.find_element_by_id(control_name))
        elif tag == "class_name":
            WebDriverWait(browser, timeout).until(lambda x: x.find_element_by_class_name(control_name))
        elif tag == "css_selector":
            WebDriverWait(browser, timeout).until(lambda x: x.find_element_by_css_selector(control_name))
        elif tag == "link_text":
            WebDriverWait(browser, timeout).until(lambda x: x.find_element_by_link_text(control_name))
        ###判断control元素是否可见
        if tag == "name":
            if not browser.find_element_by_name(control_name).is_displayed():
                return False 
        elif tag == "id":
            if not browser.find_element_by_id(control_name).is_displayed():
                return False
        elif tag == "class_name":
            if not browser.find_element_by_class_name(control_name).is_displayed():
                return False
        elif tag == "css_selector":
            if not browser.find_element_by_css_selector(control_name).is_displayed():
                return False
        elif tag == "link_text":
            if not browser.find_element_by_link_text(control_name).is_displayed():
                return False
        return True
    except Exception:
        return False

def get_controls(browser, control_name, tag="name", timeout=1):
    """获取控件
    """
    assert(tag in ["name", "id", "class_name", "link_text", "css_selector"])
    assert(browser and control_name)

    try:
        if tag == "name":
            webelems = WebDriverWait(browser, timeout).until(lambda x: x.find_elements_by_name(control_name))
        elif tag == "id":
            webelems = WebDriverWait(browser, timeout).until(lambda x: x.find_elements_by_id(control_name))
        elif tag == "class_name":
            webelems = WebDriverWait(browser, timeout).until(lambda x: x.find_elements_by_class_name(control_name))
        elif tag == "css_selector":
            webelems = WebDriverWait(browser, timeout).until(lambda x: x.find_elements_by_css_selector(control_name))
        elif tag == "link_text":
            webelems = WebDriverWait(browser, timeout).until(lambda x: x.find_elements_by_link_text(control_name))
        return webelems
    except Exception:
        return []

def input_text(browser, text_name, content, tag="name", idx=0, timeout=1):
    """输入文本
    """
    assert(tag in ["name", "id"])
    assert(browser and text_name)

    try:
        if tag == "name":
            webelems = WebDriverWait(browser, timeout).until(lambda x: x.find_elements_by_name(text_name))
        elif tag == "id":
            webelems = WebDriverWait(browser, timeout).until(lambda x: x.find_elements_by_id(text_name))
        webelems[idx].clear()
        webelems[idx].send_keys(content.decode("utf8", "ignore"))
    except Exception, message:
        raise message

input_textarea = input_password = input_text

def click_linktext(browser, link_text, tag="link_text", idx=0, timeout=1):
    """单击超链接文字
    """
    assert(tag in ["name", "link_text"])
    assert(browser and link_text)

    try:
        if tag == "link_text":
            webelems = WebDriverWait(browser, timeout).until(lambda x: x.find_elements_by_link_text(link_text))
        elif tag == "name":
            webelems = WebDriverWait(browser, timeout).until(lambda x: x.find_elements_by_name(link_text))
        webelems[idx].click()
    except Exception, message:
        raise message

def click_button(browser, button_name, tag="name", idx=0, timeout=1):
    """单击按钮
    """
    assert(tag in ["name", "id", "class_name", "css_selector"])

    try:
        if tag == "name":
            webelems = WebDriverWait(browser, timeout).until(lambda x: x.find_elements_by_name(button_name))
        elif tag == "id":
            webelems = WebDriverWait(browser, timeout).until(lambda x: x.find_elements_by_id(button_name))
        elif tag == "class_name":
            webelems = WebDriverWait(browser, timeout).until(lambda x: x.find_elements_by_class_name(button_name))
        elif tag == "css_selector":
            webelems = WebDriverWait(browser, timeout).until(lambda x: x.find_elements_by_css_selector(button_name))
        webelems[idx].click()
    except Exception, message:
        raise message

click_image = click_submit = click_button


class URL_Spider(object):
    _name = "spider"
    _url = ''
    browser = None
    def init(self):
        self.browser = webdriver.Firefox()

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

class File_Spider(object):
    file_dir = ""
    def set(self, dir):
        self.file_dir = dir

if __name__ == '__main__':
    
    dir = os.path.join(os.getenv("HOME"),".wwconf")
    config_file = os.path.join(dir,"reg_cl.cfg")
    config = ConfigParser.ConfigParser()
    config.read(config_file)

    username = config('User','name')
    password = config('User','password')

    #1.爬code

    #2.注册

    """
    #wirte
    config.add_section('User')
    config.set('User','name','王威')
    config.set('User','password','08257307qaz')
    with open('/home/ww/.wwconf/reg_cl.cfg','wb') as configfile:
        config.write(configfile)
    """
    """
    count = 0
    while True:
        time.sleep(2)
        count += 1
        print count
    """
        

