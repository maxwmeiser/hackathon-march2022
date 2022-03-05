from alert import email_message
from yoda import getYodaTranslation
from message import getMotiMessage

if __name__ == '__main__':
    email_message("TEST TRANSLATION",getYodaTranslation(getMotiMessage),"zyns.net@gmail.com")
    #print('MESSAGE| Subject: '+sys.argv[1]+' |Body: '+sys.argv[2]+' |Recipient: '+sys.argv[3])