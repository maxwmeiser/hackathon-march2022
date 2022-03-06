from re import X
import requests
from yoda import getYodaTranslation

# This function pulls from Motivational Quotes RapidAPI and returns random quote
def getMotivationalQuote():
    url = "https://motivational-quotes1.p.rapidapi.com/motivation"

    payload = "{\n    \"key1\": \"value\",\n    \"key2\": \"value\"\n}"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "motivational-quotes1.p.rapidapi.com",
        'x-rapidapi-key': "bfce1ab576msh7ba183efa6c3bc7p19f616jsn9d5dafbaf327"
        }

    res = requests.request("POST", url, data=payload, headers=headers)

    return res.text

# This function takes in a quote, formats accordingly in order to "Yodafy", and returns Yodafied quote
def formatForYoda(quote):
    
    speaker = ""
    # take what's inside quotations and save the person who said it
    if ((quote.count('-') == 1) == True):
        speaker = quote.split('-')[1]
    
    # if speaker is 'null', change it to empty string
    if speaker == "null":
        speaker = ""

    # take what's inside quotations and store it in result
    result = quote.split('"')[1::2]

    # lowercase the entire quote... quote should only be in result[0]
    result = result[0].lower()

    # break up quote into seperate sentences
    result = result.split('.')

    punc = '!()-[]{};:'"\,<>./?@#$%^&*_~"

    # for each sentence, take out any punctuation... helps translation
    for i, element in enumerate(result):

        for x in result[i]:
            if x in punc:
                result[i] = result[i].replace(x,"")

        # get yoda translation of sentence
        result[i] = getYodaTranslation(result[i])

    # reformat quote to include ""'s and speaker (if there is one)
    newQuote = ""
    for i, element in enumerate(result):
        if(result[i] != ""):
            newQuote = newQuote + result[i] + ". "

    result = "\" " + newQuote + " \" - Yoda"

    # if speaker, add it to end
    if((speaker == "") == False):
        result = result + " (inspired by " + speaker + ")"


    # return yodafied quote
    return result


# This function takes in sender, recipient, quote, and body, and returns edited message according to inputs
def addPersonalMessage(sender, recipient, quote, body):
    wholeMessage = quote


    if(body != ""):
        wholeMessage = body + "\n\n" + wholeMessage

    if(recipient != ""):
        wholeMessage = "Hi " + recipient + ",\n\n" + wholeMessage


    if(sender != ""):
        wholeMessage = wholeMessage + "\n\n" + "From: " + sender   


    
    
    return wholeMessage


