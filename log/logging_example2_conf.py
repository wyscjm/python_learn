#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File:	logging_example2_conf.py
Author: wyscjm
Email:	w079064@163.com
Github: https://github.com/wyscjm
Date:	2015-05-04
Ver:	V0.1
Source: http://blog.csdn.net/chosen0ne/article/details/7319306
Description: 
    teach me use conf file to write log

"""

import logging
import logging.config

logging.config.fileConfig('./conf/logging.conf')

logger = logging.getLogger("simpleExample")
a = "abc"

logger.debug("debug message:%s",a)
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")
