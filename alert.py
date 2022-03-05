#utilized https://www.youtube.com/watch?v=B1IsCbXp0uE

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
    print('past send_message')
    server.quit()



    #def main():
    #    email_message("thet2","test2","zyns.net@gmail.com")

if __name__ == '__main__':
    print('getting here')
    email_message("message test", "test 2", "zyns.net@gmail.com")
