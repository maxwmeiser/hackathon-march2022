from alert import email_message
from message import getMotivationalQuote, formatForYoda, addPersonalMessage
from yoda import getYodaTranslation
#from message import getMotiMessage
import schedule
import time

#this function takes in input to personalize the message
def personalize_message():
    print('Motivational Yoda shall be delivered. If you dont want to submit your information, leave the field blank and hit enter.')
    senderIn = input('Please input your name: ')
    recipientIn = input("Please enter the recipient's name: ")
    bodyIn = input('Please enter the body of your personal message: ')
    quoteIn = formatForYoda(getMotivationalQuote())
    return addPersonalMessage(senderIn,recipientIn,quoteIn,bodyIn)


#this function takes in input to determine what address to send the message to. returns a string for third argument of email_message
def get_recip_address():
    print('How would you like the recipient to recieve your messages?\n1. Email\n2. Text Message\n3. Cancel')
    mediumPick = input('#> ')
    match mediumPick:
        case '1':
            return input("Please enter the recipient's email address: ")
        case '2':
            userCarrier = input("Please select the recipient's service carrier: \n1. AT&T\n2. Boost Mobile\n3. Sprint\n4. T-Mobile\n5. Verizon\n6. Virgin Mobile\n7. Cancel\n#> ")
            if userCarrier != 7:
                userNumber = input("Please enter the recipient's phone number: ")
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
    email_message("You recieved a MotiYoda!",completeMessage,userAddress)

completeMessage = personalize_message()

userAddress = get_recip_address()
while userAddress == 'invalid' and userAddress != 'quit':
    userAddress = get_recip_address()

RUN = True

if userAddress == 'quit':
    RUN = False



if RUN:
    send_message()


#schedule.every(30).seconds.do(send_message)

#while RUN:
#    schedule.run_pending()
#    time.sleep(1)
