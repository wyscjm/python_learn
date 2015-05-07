#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File:	createDaemon.py
Author: wyscjm
Email:	w079064@163.com
Github: https://github.com/wyscjm
Date:	2015-05-04
Ver:	V0.1
Description: create a daemon: write a msg 
    to /tmp/daemon.log every 2 seconds
source: http://blog.csdn.net/mr_jj_lian/article/details/7252222
        http://www.open-open.com/bbs/view/1319506853577
"""


def createDaemon():
    """create a daemon"""
    import os

    #create fork 1
    try:
        if os.fork() > 0:
            os._exit(0)
    except OSError, error:
        print 'fork #1 failed:%d(%s)'% (eror.errno,error.strerror)
        os._exit(1)

    #it separates the son from father
    os.chdir('/')
    os.setsid()
    os.umask(0)

    #create fork 2
    try:
        pid = os.fork()
        if pid > 0:
            print 'Daemon PID %d' % pid
            os._exit(0)
    except OSError,error:
        print 'fork #2 failed:%d(%s)' % (error.errno,error.strerror)
        ox._exit(1)

    funzioneDamo()

def funzioneDamo():
    import time
    fd = open('/tmp/daemone.log','w')
    while True:
        fd.write(time.ctime()+'\n')
        fd.flush()
        time.sleep(2)
    fd.close()

if __name__ == '__main__':
    createDaemon()
