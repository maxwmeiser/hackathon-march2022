from email import header
import requests
import json

# This function takes in text and uses FunTranslations Yoda API to translate into Yoda language and return new text
def getYodaTranslation(text):
    url = "https://api.funtranslations.com/translate/yoda.json"

    querystring = {"text": text}

    header = {"X-FunTranslations-Api-Secret":"G2Ygw8PEz6lqpGWdvFaV2QeF"}

    res = requests.post(url,headers=header,data=querystring)

    res_json = json.loads(res.text)

    translated_content = res_json["contents"]["translated"]

    return translated_content





# //https://api.funtranslations.com/translate/yoda.json?text=Master%20Obiwan%20has%20lost%20a%20planet.

# G2Ygw8PEz6lqpGWdvFaV2QeF : API key