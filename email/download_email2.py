import getpass, imaplib

M = imaplib.IMAP4("imap.163.com")
user = "w079064@163.com"
passwd = "wys08257307qaz"
M.login(user, passwd)
M.select("w079064@163.com")
typ, data = M.search(None, 'ALL')
for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    print 'Message %s\n%s\n' % (num, data[0][1])
M.close()
M.logout()
