from alert import email_message
from message import getMotivationalQuote, formatForYoda, addPersonalMessage
from yoda import getYodaTranslation
from validate_email_address import validate_email
#from message import getMotiMessage
import schedule
import time

#this function takes in input to personalize the message
def personalize_message():
    print("\n\n-------MotiYoda: SMS/Email-------\n##Welcome to MotiYoda! Send a personalized message to a friend\n through text or email with an included\n inspirational quote from Yoda himself.\n If you dont want to submit your information,\n leave the field blank and hit enter.##\n")
    senderIn = input('Please input your name: ')
    recipientIn = input("Please enter the recipient's name: ")
    bodyIn = input('\nPlease enter the body of your personal message: ')
    quoteIn = formatForYoda(getMotivationalQuote())
    return addPersonalMessage(senderIn,recipientIn,quoteIn,bodyIn)


#this function takes in input to determine what address to send the message to. returns a string for third argument of email_message
def get_recip_address():
    print('\nHow would you like the recipient to recieve your messages?\n1. Email\n2. Text Message\n3. Cancel')
    mediumPick = input('#> ')
    match mediumPick:
        case '1':    
            emailIn = input("\nPlease enter the recipient's email address: ")
            while not validate_email(emailIn) and emailIn != "exit":
                emailIn = input('Invalid email address. Please try again or enter "exit" to quit: ')
            if emailIn == "exit":
                return "quit"
            return emailIn
        case '2':
            phoneAddress = ""
            while not validate_email(phoneAddress) and phoneAddress != "quit":
                userCarrier = input("\nPlease select the recipient's service carrier: \n1. AT&T\n2. Boost Mobile\n3. Sprint\n4. T-Mobile\n5. Verizon\n6. Virgin Mobile\n7. Cancel\n#> ")
                if userCarrier != '7':
                    userNumber = input("\nPlease enter the recipient's phone number: ")
                match userCarrier:
                    case '1':
                        phoneAddress = userNumber + '@mms.att.net'
                    case '2':
                        phoneAddress = userNumber + '@myboostmobile.com'
                    case '3':
                        phoneAddress = userNumber + '@pm.sprint.com'
                    case '4':
                        phoneAddress = userNumber + '@tmomail.net'
                    case '5':
                        phoneAddress = userNumber + '@vzwpix.com'
                    case '6':
                        phoneAddress = userNumber + '@vmpix.com'
                    case '7':
                        phoneAddress = "quit"
                    case _:
                        print('Invalid menu selection')
                        phoneAddress = 'invalid'
            return phoneAddress
        case '3':
            return 'quit'
        case _:
            print('Invalid menu selection. Please try again')
            return 'invalid'

def send_message():
    email_message("You recieved a MotiYoda!",completeMessage,userAddress)

completeMessage = personalize_message()

userAddress = get_recip_address()
while userAddress == 'invalid' and userAddress != "quit":
    userAddress = get_recip_address()

RUN = True

if userAddress == "quit":
    RUN = False



if RUN:
    print('\nMessage sent!\n')
    send_message()


#schedule.every(30).seconds.do(send_message)

#while RUN:
#    schedule.run_pending()
#    time.sleep(1)
