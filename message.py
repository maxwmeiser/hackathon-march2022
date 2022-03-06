from re import X
import requests
from yoda import getYodaTranslation


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

def formatForYoda(quote):

    # A dream is your creative vision for your life in the future. You must break out of your  
    # comfort zone to become comfortable with the unfamiliar and the unknown.
    
    speaker = ""
    # take what's inside quotations and save the person who said it
    if ((quote.count('-') == 1) == True):
        speaker = quote.split('-')[1]
    
    if speaker == "null":
        speaker = ""

    result = quote.split('"')[1::2]

    # result = result.split(".")

    result = result[0].lower()

    result = result.split('.')

    punc = '!()-[]{};:'"\,<>./?@#$%^&*_~"

    for i, element in enumerate(result):

        for x in result[i]:
            if x in punc:
                result[i] = result[i].replace(x,"")

        result[i] = getYodaTranslation(result[i])


    newQuote = ""
    for i, element in enumerate(result):
        if(result[i] != ""):
            newQuote = newQuote + result[i] + ". "

    result = "\" " + newQuote + " \" - Yoda"

    if((speaker == "") == False):
        result = result + " (inspired by " + speaker + ")"

    return result
