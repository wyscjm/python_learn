#-*- coding:UTF-8 -*-
#@小五义 http://www.cnblogs.com/xiaowuyi

import imaplib, string, email
import os
M = imaplib.IMAP4("imap.163.com")
t=0
try:
    try:
        M.login('w079064@163.com','wys08257307qaz')####YYYY为密码
    except Exception,e:
        #print "wrong!"
        print 'login error: %s' % e
        M.close()
    
    print M.list()
    M.select('INBOX',False)
    
   # result, message = M.select()
    typ, data = M.search(None, 'Unseen')
    for num in string.split(data[0]):
        try:
            typ, data = M.fetch(num, '(UID BODY.PEEK[])')
            msg = email.message_from_string(data[0][1])
            t=t+1
            filename=str(t)+".eml"
            f=open(filename,'wb')
            f.write(str(msg))
            f.close
        except Exception,e:
            print 'got msg error: %s' % e            
    print "OK!"
    M.logout()
except Exception, e:
    print 'imap error: %s' % e
    M.close()
