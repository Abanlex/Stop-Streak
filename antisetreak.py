#!/usr/bin/env/python
#By s4ur0n (@NN2ed_s4ur0n)
 
import imaplib
 
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('username@gmail.com', 'Your-password-here')
mail.select()   # Or mail.select('INBOX')
#result, data = mail.search(None, '(X-GM-RAW "Search term... I.e. 1x1.gif"')
result, data = mail.search(None, 'ALL')
 
id_list = data[0].split()
for id in reversed(range(0, len(id_list))):
    email_id = id_list[id]
    result, data = mail.fetch(email_id, '(RFC822)')
    raw_email = data[0][1]
    if ('streak-pt-mark' or 'https://mailfoogae.appspot.com/') in raw_email:
        print raw_email
        print '\r\nWarning!\r\nTraced by: '
        print raw_email[raw_email.rfind('sender=3D')+9:raw_email.find('&amp;amp')].replace('%40','@')
        raw_input('Press ENTER to continue...')
 
mail.logout()
