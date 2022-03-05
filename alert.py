#utilized https://www.youtube.com/watch?v=B1IsCbXp0uE

import sys
import smtplib
from email.message import EmailMessage

def email_message(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "motiyoda2022@gmail.com"
    msg['from'] = user
    password = "glvslxmkxcsfidxo"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
    email_message(sys.argv[1],sys.argv[2],sys.argv[3])
    print('MESSAGE| Subject: '+sys.argv[1]+' |Body: '+sys.argv[2]+' |Recipient: '+sys.argv[3])
