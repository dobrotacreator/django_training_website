import requests

token = '5796609948:AAHDqrOOsKi8M07j71LaKmCfswU5yZWq6HE'
chat_id = '-654080597'
text = 'Test_2'

def sendTelegram():
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text,
    })

sendTelegram()