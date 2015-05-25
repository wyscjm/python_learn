#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File:	download_email5.py
Author: wyscjm
Email:	w079064@163.com
Github: https://github.com/wyscjm
Date:	2015-05-18
Ver:	V0.1
Description: 

"""

""" GMail archiver 1.1
 
This program will download and archive all you emails from GMail.
Simply enter your login and password, and all your emails will
be downloaded from GMail and stored in a standard mbox file.
This inclues inbox, archived and sent mails, whatever label you applied.
Spam is not downloaded.
 
This mbox files can later on be opened with almost any email client (eg. Evolution).
 
Author:
    Sébastien SAUVAGE - sebsauvage at sebsauvage dot net
    Webmaster for http://sebsauvage.net/
 
License:
 
    This program is distributed under the OSI-certified zlib/libpnglicense .
    http://www.opensource.org/licenses/zlib-license.php
 
    This software is provided 'as-is', without any express or implied warranty.
    In no event will the authors be held liable for any damages arising from
    the use of this software.
 
    Permission is granted to anyone to use this software for any purpose,
    including commercial applications, and to alter it and redistribute it freely,
    subject to the following restrictions:
 
        1. The origin of this software must not be misrepresented; you must not
           claim that you wrote the original software. If you use this software
           in a product, an acknowledgment in the product documentation would be
           appreciated but is not required.
 
        2. Altered source versions must be plainly marked as such, and must not
           be misrepresented as being the original software.
 
        3. This notice may not be removed or altered from any source distribution.
 
Requirements:
 
    - a GMail account with IMAP enabled in settings.
    - GMail settings in english
    - Python 2.5
"""
import imaplib,getpass,os
import re

list_response_pattern = re.compile(r'\((?P<flags>.*?)\) "(?P<delimiter>.*)" (?P<name>.*)')

def parse_list_response(line):
    flags, delimiter, mailbox_name = list_response_pattern.match(line).groups()
    mailbox_name = mailbox_name.strip('"')
    return (flags, delimiter, mailbox_name)

print "GMail archiver 1.1"
#user = raw_input("Enter your GMail username:")
#pwd = getpass.getpass("Enter your password: ")
user = "852567029"
pwd = "wys08257307qaz"
#m = imaplib.IMAP4_SSL("imap.qq.com")
m = imaplib.IMAP4("imap.qq.com")
m.login(user,pwd)

try:
    typ, mailbox_data = m.list()
    for line in mailbox_data:
        flags, delimiter, mailbox_name = parse_list_response(line)
        m.select(mailbox_name, readonly=True)
        typ, msg_ids = m.search(None, 'ALL')
        print mailbox_name, typ, msg_ids        
finally:
    try:
        m.close()
    except:
        pass

"""
m.select("INBOX")
resp, items = m.search(None, "ALL")
items = items[0].split()
print "Found %d emails." % len(items)
count = len(items)
for emailid in items:
    print "Downloading email %s (%d remaining)" % (emailid,count)
    resp, data = m.fetch(emailid, "(RFC822)")
    email_body = data[0][1]
    # We duplicate the From: line to the beginning of the email because mbox format requires it.
    from_line = "from:unknown@unknown"
    try:
        from_line = [line for line in email_body[:16384].split('\n') if line.lower().startswith('from:')][0].strip()
    except IndexError:
        print "  'from:' unreadable."
    email_body = "From %s\n%s" % (from_line[5:].strip(),email_body)
    file = open("%s.mbox"%user,"a")
    file.write(email_body)
    file.write("\n")
    file.close()
    count -= 1
"""
print "All done."
