#utilized youtube.com/watch?v=B1lsCbXp0uE

import smtplib
from email.message import EmailMessage

def email_message(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "motiYoda2022@gmail.com"
    msg['from'] = user
    password = "glvslxmkxcsfidxo"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

    if __name__ == '__main__':
        email_message("the","big test","mame5632@colorado.edu")
