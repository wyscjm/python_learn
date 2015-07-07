#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File:	js_test1.py
Author: wyscjm
Email:	w079064@163.com
Github: https://github.com/wyscjm
Date:	2015-07-07
Ver:	V0.1
Description: 
    测试JS脚本
"""
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://ehire.51job.com/MainLogin.aspx")

js="var q=document.getElementById(\"txtMemberNameCN\");q.style.border=\"1px solid red\";"

driver.execute_script(js)

time.sleep(3)

driver.find_element_by_id("txtMemberNameCN").send_keys("username")
time.sleep(3)

driver.quit()

