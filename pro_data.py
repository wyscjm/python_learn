#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: 
Author: 
Email: 
Github: 
Description: 
"""

import os
import matplotlib.pyplot as plt
from matplotlib import pylab
import numpy as np

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        if not height:
            height = 0
            plt.text(rect.get_x() + rect.get_width()/2., 1.05*(height+1), '%d'%int(height),
                ha='center', va='bottom')
            continue
        plt.text(rect.get_x() + rect.get_width()/2., 1.05*(height), '%d'%int(height),
                ha='center', va='bottom')

def pro_data(file):
    times = 0
    read_one_all = []
    read_three_all = []

    assert(os.path.isfile(file))

    fin = open(file)
    for line in fin:
        line = line.strip()
        line = line.replace("ALL TAG","ALL")
        a = line.split(" ")
        read_three = {}
        read_one = {}
        if a[3] == "ALL":
            dt = "2015-" + a[1] + " " + a[2]
            read_three["datetime"] = dt
            a[5] = a[5][:-1]
            read_three["tag_num"] = a[5]
            print a[6]
            if a[6]:
                read_three["tag"] = a[6].split(",")
            else:
                read_three["tag"] = []
            #read_three["tag"] = filter(lambda e:e=='',read_three["tag"])
            read_three_all.append(read_three)
        if a[3] == "TAG":
            dt = "2015-" + a[1] + " " + a[2]
            read_one["datetime"] = dt
            a[5] = a[5][:-1]
            read_one["tag_num"] = a[5]
            a[6] = a[6][:-1]
            read_one["tag"] = a[6].split(":")
            #read_one["tag"] = filter(lambda e:e=='',read_one["tag"])
            read_one_all.append(read_one)

    #file
    file_one = "./read_one.pro"
    file_three = "./read_three.pro"

    if os.path.isfile(file_one):
        os.remove(file_one)

    fp = open(file_one,"w")
    for line in read_one_all:
        line = str(line) + "\n"
        fp.write(line)

    fp = open(file_three,"w")
    for line in read_three_all:
        line = str(line) + "\n"
        fp.write(line)

    #picture
    #read_one
    lg = len(read_one_all)
    dates = []
    data = []
    cal_data = {}
    for read_one in read_one_all:
        dates.append(read_one["datetime"])
        data.append(read_one["tag_num"])
        #if read_one["tag_num"] == '7':
        #    print read_one
        #    continue
        if not cal_data.has_key(read_one["tag_num"]):
            cal_data[read_one["tag_num"]] = 0
        cal_data[read_one["tag_num"]] = cal_data[read_one["tag_num"]] + 1
    x = cal_data.keys()
    y = cal_data.values()
    x.sort()
    p_read_one = {}
    for i in x:
        p_read_one[i] = cal_data[i]

    #read_three
    lg = len(read_three_all)
    dates = []
    data = []
    cal_data = {}
    for read_three in read_three_all:
        dates.append(read_three["datetime"])
        data.append(read_three["tag_num"])
        #if read_three["tag_num"] == '7':
        #    print read_three
        #    continue
        if not cal_data.has_key(read_three["tag_num"]):
            cal_data[read_three["tag_num"]] = 0
        cal_data[read_three["tag_num"]] = cal_data[read_three["tag_num"]] + 1
    x = cal_data.keys()
    y = cal_data.values()
    x.sort()
    p_read_three = {}
    for i in x:
        p_read_three[i] = cal_data[i]
    
    x1 = p_read_one.keys()
    x2 = p_read_three.keys()
    x = list( set( x1 + x2))
    for i in x:
        if not p_read_one.has_key(i):
            p_read_one[i] = 0
        if not p_read_three.has_key(i):
            p_read_three[i] = 0
    x.sort()
    y1 = []
    y2 = []
    for i in x:
        y1.append(p_read_one[i])
        y2.append(p_read_three[i])
    print "y1:", y1
    print "y2:", y2

    """
    pylab.xlabel("read_num")
    pylab.ylabel("count_num")
    pylab.title("test")
    pylab.gca().set_yscale('log')
     
    dim = len(x)
    w = 0.35
    ind = np.arange(dim)
    p1 = plt.bar(ind, y1, w,color='y')
    p2 = plt.bar(ind+w, y2, w,color='r')
    plt.ylabel('Count')
    plt.xlabel('read num')
    plt.xticks(ind+w/2.,x)
    #plt.yticks(np.arange(0,700,50))
    plt.legend( (p1[0],p2[0]), ('read_one','read_three'),loc = 'upper center')

    autolabel(p1)
    autolabel(p2)
    plt.show()
    """

    #tag analysis

    

#    print read_three_all

if __name__ == "__main__":
    file = "./tag_reader.log"
    pro_data(file)
