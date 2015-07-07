#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File:	js_test2.py
Author: wyscjm
Email:	w079064@163.com
Github: https://github.com/wyscjm
Date:	2015-07-07
Ver:	V0.1
Description: 
    测试JS脚本
"""
from selenium import webdriver
import time,os

driver = webdriver.Firefox()
file_path = "file://" + os.path.abspath('js.html')
driver.get(file_path)

#js="var q=document.getElementById(\"txtMemberNameCN\");q.style.border=\"1px solid red\";"

driver.execute_script('$("#tooltip").fadeOut();')
time.sleep(5)

button = driver.find_element_by_class_name("btn")
driver.execute_script('$(arguments[0]).fadeOut()',button)
time.sleep(5)

driver.quit()

