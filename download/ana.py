#!/usr/bin/env python # -*- coding: utf-8 -*-

"""
File:	ana.py
Author: wyscjm
Email:	w079064@163.com
Github: https://github.com/wyscjm
Date:	2015-11-07
Ver:	V0.1
Description: 
    1.分析文件链接
"""
import os


import re
#zhPattern = re.compile(u'[\u4e00-\u9fa5\+')

def is_chinese(uchar):
        """判断一个unicode是否是汉字"""
        if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
                return True
        else:
                return False

def ana_mag(source ):
    """ 分析文件里有maget的链接"""
    links = []
    new_link = ""
    if(source):
        print "analysis start... " 
        for line in source:
            line = line.decode("gb2312", "ignore").strip()
            if new_link:
                #后面链接的有汉字就停止解析
                if line:
                    #match = zhPattern.search(line.strip().decode("gb2312",'ignore'))
                    for  by in line:
                        if is_chinese(by):
                            links.append(new_link)
                            new_link = ""
                            continue
                    new_link += line
                else:
                    links.append(new_link)
                    new_link = ""
                    continue
            else:
                if "magnet:?" in line:
                    new_link = line.strip()
                    print "start:", new_link
    else:
        print "please input a valid source"
    print "links[%d]:" % len(links),links
    return links


if __name__ == '__main__':
    print "请察看文件"
    file = "link_file.txt"
    source_texts = ["/mnt/hgfs/share/1.txt","/mnt/hgfs//share/2.txt"]
    links = []
    for source in source_texts:
        file_object = open(source)
        links = links + ana_mag(file_object)

    text_infile = ''
    for link in links:
        text_infile += '\r\n' + link
    print text_infile
    open(file,'w').write(text_infile)
    print links

