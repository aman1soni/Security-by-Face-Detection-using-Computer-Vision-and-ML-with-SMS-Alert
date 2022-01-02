import requests
import json

def sendsms():
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
            'authorization': '//YOUR_FAST2SMS_API_KEY',
            'sender_id': 'FSTSMS',
            'message': "Alert! Someone aunthenticated user try to access your personal computer.\n\nMessage sent by Admin.\n\nThanks",
            'language': 'english',
            'route': 'p',
            'numbers': 8290532795
             }
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)
    print(dic.get('return'))

sendsms()

