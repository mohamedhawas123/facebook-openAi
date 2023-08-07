
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import facebook
import requests
import time
import random
from chatterbot.response_selection import get_most_frequent_response
from pyarabic.araby import strip_tashkeel

access_token="EAAH52kKpkgQBAHPgbPX2fzBCTzTfuER2fhUv2KZBhGZC097KIE88Q2YDDfh1vaQTFvNUQV1ATnu35R5VUHvU5sDJicRCJneEtM0A338B7t710LuotBrPkeTJzQ7Ql6cFk5Xu26Jx6ZC4nfF1WxZCOsnOMjv6wBdZAojGZAY1I2VR9kF2UYz3oBYZCjJGrZAbJc2XvZCE2nziyi2IszocgvmQR"
access_token_tosend = "EAAH52kKpkgQBAADWnZATXQI00YZAI9g6pwaIqSeZCHZCC51I1nRivTcA20yjIggvS4SMg5DmlCqWyH44QmSF3ZAevDzQEBLZA4ZAyOOHnfkjnd68uZCNSo8e0FW9p937xFXU3I5cBs2ZCntbbihhnAwu9EcsR08EAFaBD2BWIhk94bgKMAll8XL4xstTTWGegHhWElvHvxxypZCZCnXC6CfK4YG"
page_id="105047379246204"


def preprocess_arabic(text):
    return strip_tashkeel(text)

def get_messages():
    latest_message = None
    
    url = f"https://graph.facebook.com/v16.0/{page_id}/conversations"
    params = {
        "fields": 'messages{message, created_time, from}',
        'access_token': access_token
    }

    response = requests.get(url, params=params)
    data = response.json()

    if 'messages' in data['data'][0]:
        messages = data['data'][0]['messages']['data']
        if messages:
            latest_message = messages[0]

    return latest_message

def send_message(messagetosend, sender_id):
    if not messagetosend:
        return
    url = f"https://graph.facebook.com/v16.0/{page_id}/conversations"
    params = {
        "fields": 'messages{message, created_time, from}',
        'access_token': access_token

    }

    response = requests.get(url, params=params)
    data = response.json()

    # sender_id = data['data'][0]['messages']['data'][0]['from']['id']


    to_sendurl = f"https://graph.facebook.com/v16.0/me/messages?access_token={access_token_tosend}"
    headers = {"Content-Type": "application/json"}
    datatosend = {
        "recipient": {"id": sender_id},
        "message": {'text': f'{messagetosend}'}
    }
    restosend = requests.post(to_sendurl, headers=headers, json=datatosend)
    print(restosend.content)
    return restosend



chatbot = ChatBot('Charlie', 
logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
)

trainer = ListTrainer(chatbot)



trainer.train([
    preprocess_arabic("هاي"),
        preprocess_arabic("هاي اهلا"),
    preprocess_arabic("ب 15 الف جنية"),
    preprocess_arabic("مواصفاته ايه ؟"),
    preprocess_arabic("رام 8 و كرت شاشه 2 جيجا"),
    preprocess_arabic("ايه طرق الدفع ؟"),
    preprocess_arabic("فودافون كاش"),
    preprocess_arabic("ينفع الغي اوردر ؟"),
        preprocess_arabic("ليه ؟"),
    preprocess_arabic("مش عاجبني"),
        preprocess_arabic("مستعمل ولا جديد"),
    preprocess_arabic("جديد يا فندم"),
        preprocess_arabic("فيه تقسيط ؟"),
    preprocess_arabic("لا يفندم"),



])

trainer.train([
     preprocess_arabic("مواصفاته ايه "),
    preprocess_arabic("رام 8 و كرت شاشه 2 جيجا"),
])

trainer.train([
    preprocess_arabic("عندكوا ايه"),
        preprocess_arabic("فيه لابات"),
])

trainer.train([
    preprocess_arabic("مواصفاته ايه"),
        preprocess_arabic("رام 8 و كرت شاشه 2 جيجا"),
])

trainer.train([
    preprocess_arabic("ايه الالوان المتاحه"),
        preprocess_arabic("فيه اسود بس"),
])

trainer.train([
    preprocess_arabic("بكام اللاب توب"),
        preprocess_arabic("15 الف"),
])

trainer.train([
    preprocess_arabic("بكام لو سمحت"),
        preprocess_arabic("15 الف"),
])

trainer.train([
    preprocess_arabic("لو سمحت بكام"),
        preprocess_arabic("15 الف"),
])

trainer.train([
    preprocess_arabic("كام السعر"),
        preprocess_arabic("15 الف"),
])







   

# graph = facebook.GraphAPI(access_token= access_token)

# conversations = graph.get_connections(page_id, 'conversations', fields='updated_time')
# last_conversation = conversations['data'][0]['id']
# message_id = graph.get_connections(last_conversation, 'messages')['data'][0]['id']

# print(message_id)
# message =requests.get(f"http://graph.facebook.com/v16.0/{message_id}?access_token={access_token}")
# print(message.content)