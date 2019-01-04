import requests
import misc
from yobit import get_btc
from time import sleep
# import json

token = misc.token

# https://api.telegram.org/bot555124927:AAHECnH8PLdaMMwGNznyk3E7qlXxnbCzWrA/sendmessage?chat_id=463507577&text=hi
URL = 'https://api.telegram.org/bot' + token + '/'




def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()



def get_message():
    
 

    data = get_updates()
    
    chat_id = data['result'][-1]['message']['chat']['id']
    message_text = data['result'][-1]['message']
    
    message =  {'chat_id': chat_id,
                'text': message_text}

    return message    
  
def send_message(chat_id, text='Пожалуйста,подождите'):
	url =  URL = 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
	requests.get(url)





def main():
    # d = get_updates()

        while True:
        answer = get_message()
        chat_id = answer['chat_id']
        text = answer['text'] 

        if text == '/btc':
            send_message(chat_id, get_btc()) 

        sleep(1)   
    
    


if __name__ == '__main__':
    main()
