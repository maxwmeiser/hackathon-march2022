from email import header
import requests
import json

url = "https://api.funtranslations.com/translate/yoda.json"

querystring = {"text":"problem"}

header = {"X-FunTranslations-Api-Secret":"G2Ygw8PEz6lqpGWdvFaV2QeF"}

response = requests.post(url,headers=header,data=querystring)

json_data = json.loads(response.text)

print(response.text)



# //https://api.funtranslations.com/translate/yoda.json?text=Master%20Obiwan%20has%20lost%20a%20planet.

# G2Ygw8PEz6lqpGWdvFaV2QeF : API key