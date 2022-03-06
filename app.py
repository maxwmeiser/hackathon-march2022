from alert import email_message
from message import getMotivationalQuote, formatForYoda
from yoda import getYodaTranslation
#from message import getMotiMessage
import schedule
import time

#this function takes in input to determine what address to send the message to. returns a string for third argument of email_message
def get_recip_address():
    print('Motivational Yoda.. blah blah blah. How would you like to recieve your messages?\n1. Email\n2. Text Message\n3. Cancel')
    mediumPick = input('#> ')
    match mediumPick:
        case '1':
            return input('Please enter your email address: ')
        case '2':
            userCarrier = input('Please select your service carrier: \n1. AT&T\n2. Boost Mobile\n3. Sprint\n4. T-Mobile\n5. Verizon\n6. Virgin Mobile\n7. Cancel\n#> ')
            userNumber = input('Please enter your phone number: ')
            match userCarrier:
                case '1':
                    return userNumber + '@mms.att.net'
                case '2':
                    return userNumber + '@myboostmobile.com'
                case '3':
                    return userNumber + '@pm.sprint.com'
                case '4':
                    return userNumber + '@tmomail.net'
                case '5':
                    return userNumber + '@vzwpix.com'
                case '6':
                    return userNumber + '@vmpix.com'
                case '7':
                    return 'quit'
                case _:
                    print('Invalid menu selection')
                    return 'invalid'
        case '3':
            return 'quit'
        case _:
            print('Invalid menu selection. Please try again')
            return 'invalid'

def send_message():
    unformattedQuote = getMotivationalQuote()
    formattedQuote = formatForYoda(unformattedQuote)
    email_message("Today's MotiYoda",formattedQuote,userAddress)

userAddress = get_recip_address()
while userAddress == 'invalid' and userAddress != 'quit':
    userAddress = get_recip_address()

RUN = True

if userAddress == 'quit':
    RUN = False

schedule.every(15).seconds.do(send_message)

while RUN:
    schedule.run_pending()
    time.sleep(1)
