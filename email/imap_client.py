#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File:	imap_client.py
Author: wyscjm
Email:	w079064@163.com
Github: https://github.com/wyscjm
Date:	2015-05-25
Ver:    V0.1
Description: 
    see: http://pymotw.com/2/imaplib/
    记录impa 邮件接收器
"""

import imaplib
import ConfigParser
import os
import re
import pprint
import email
import time
import email.message

list_response_pattern = re.compile(r'\((?P<flags>.*?)\) "(?P<delimiter>.*)" (?P<name>.*)')
new_message = email.message.Message()
new_message.set_unixfrom('pymotw')
new_message['Subject'] = 'subject goes here'
new_message['From'] = 'pymotw@example.com'
new_message['To'] = 'example@example.com'
new_message.set_payload('This is the body of the message.\n')

def open_connection(verbose=False):
    #Read the config file
    config = ConfigParser.ConfigParser()
    config.read([os.path.expanduser('~/.py_email')])

    # Connect to the server
    hostname = config.get('server','hostname')
    if verbose: print 'Connecting to', hostname
    #connection = imaplib.IMAP4.IMAP4_SSL(hostname)
    connection = imaplib.IMAP4_SSL(hostname)

    # Login our account
    username = config.get('account','username')
    password = config.get('account','password')
    if verbose: print 'Logging in as',username
    connection.login(username,password)
    return connection

def parse_list_response(line):
    flags, delimiter, mailbox_name = list_response_pattern.match(line).groups()
    mailbox_name = mailbox_name.strip('"')
    return (flags,delimiter, mailbox_name)

if __name__ == '__main__':
    c = open_connection(verbose=True)
    try:
        """
        #所有的目录
        typ, data = c.list()
        #名为JUNK的目录
        #typ, data = c.list(directory='Junk')
        #含有messages的目录(未成功)
        #typ, data = c.list(pattern='*Message*')
        #print 'Response code:', typ
        #print 'Response:'
        #import pprint; pprint.pprint(data)

        for line in data:
            print 'Server response:', line
            flags, delimiter, mailbox_name = parse_list_response(line)
            #print 'Parsed response:',(flags, delimiter, mailbox_name)
            print c.status(mailbox_name, '(MESSAGES RECENT UIDNEXT UIDVALIDITY UNSEEN)')
        
        #选择一个邮箱 --- ok
        typ, data = c.select('INBOX')
        print type, data
        num_msgs = int(data[0])
        print 'There arm %d messages in INBOX' % num_msgs

        #查找文本 报错:BAD ['Missing or invalid argument to SEARCH']
        typ, data = c.list()
        for line in data:
            falgs, delimiter, mailbox_name = parse_list_response(line)
            c.select(mailbox_name, readonly=True)
            #typ, msg_ids = c.search(None, 'ALL')
            #typ, msg_ids = c.search(None, '(SUBJECT "test message")')
            typ, msg_ids = c.search(None, '(SUBJECT "test message 2")')
            print mailbox_name, typ, msg_ids
        
        #拉取信息 -ok
        #add at begin: imaplib.Debug = 4
        c.select('INBOX', readonly=True)
        typ, msg_data = c.fetch('1','(BODY.PEEK[HEADER] FLAGS)')
        pprint.pprint(msg_data)

        #显示信息- ok
        c.select('INBOX', readonly=True)
        print 'HEADER:'
        typ, msg_data = c.fetch('1', '(BODY.PEEK[HEADER])')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                print response_part[1]
    
        print 'BODY TEXT:'
        typ, msg_data = c.fetch('1', '(BODY.PEEK[TEXT])')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                print response_part[1]

        print '\nFLAGS:'
        typ, msg_data = c.fetch('1', '(FLAGS)')
        for response_part in msg_data:
            print response_part
            print imaplib.ParseFlags(response_part)

        #完整的信息
        c.select('INBOX',readonly=True)

        typ, msg_data = c.fetch('1','(RFC822)')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1])
                for header in ['subject','to','from']:
                    print '%-8s: %s' % (header.upper(), msg[header])
        """
        #c.append('INBOX', '', imaplib.Time2Internaldate(time.time()), str(new_message))
        c.select('INBOX')
        typ, [msg_ids] = c.search(None, 'SEEN')
        for num in msg_ids.split():
            typ, msg_data = c.fetch(num, '(BODY.PEEK[HEADER])')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    print '\n%s:' % num
                    print response_part[1]

    finally:
        try:
            c.close()
        except:
            pass
        c.logout()
