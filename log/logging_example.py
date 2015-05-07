#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File:	logging_example.py
Author: wyscjm
Email:	w079064@163.com
Github: https://github.com/wyscjm
Date:	2015-05-04
Ver:	V0.1
Description: 
    1.teach me how to use logging module
"""

import logging
import logging.handlers

handler = logging.handlers.RotatingFileHandler('log/logging_example.log', maxBytes = 1024*1024, backupCount = 5)
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

formatter = logging.Formatter(fmt)  #实例化
handler.setFormatter(formatter)

logger = logging.getLogger('tst')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.info('first info message')
logger.debug('first debug message')
