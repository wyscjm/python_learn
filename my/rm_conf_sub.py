#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File:	rm_conf_sub.py
Author: wyscjm
Email:	w079064@163.com
Github: https://github.com/wyscjm
Date:	2015-05-07
Ver:	V0.1
Description: 
    将目录下的配置文件（即.list和.bak）的
    后缀名去除
"""
import os
import sys
import re
import shutil
reload(sys)
sys.setdefaultencoding('utf-8')

def mvconfsuffix(dir):
    dir = os.path.abspath(dir)
    files = os.listdir(dir)
    for file in files:
        if file.endswith(".dist"):
            new_file = re.sub(".dist","",file)
            path = os.path.abspath(dir)
            filename = os.path.join(path,file)
            new_filename = os.path.join(path,new_file)
            shutil.copyfile(filename,new_filename)
        elif file.endswith(".bak"):
            new_file = re.sub(".bak","",file)
            path = os.path.abspath(dir)
            filename = os.path.join(path,file)
            new_filename = os.path.join(path,new_file)
            shutil.copyfile(filename,new_filename)
    print "rm conf subffix"


if __name__ == '__main__':
    from optparse import OptionParser
    USAGE = """
    @python rm_conf_sub.py -d dirtoparse
    """
    parser = OptionParser(usage=USAGE)
    parser.add_option("-d","--dirtoparse",
                        dest="dirtoparse",default=".",
                        help="Please input you directory")
    options, args = parser.parse_args()
    mvconfsuffix(options.dirtoparse)

