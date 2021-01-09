import requests
import json

def sendsms():
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
            'authorization': 'noyaAWs9wUgpJtGvhK50PN8r1dY3CiEqTkbFMeS7OR2ZjxQ4ufW9FG8NcOCfX35yLS1d0ta4rewVsBIz',
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

