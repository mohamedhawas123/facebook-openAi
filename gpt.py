import pandas as pd
import openai
from bot import get_messages, send_message
openai.api_key = "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"
import requests



def get_api_response(prompt: str) -> str | None:
    text: str | None = None

    try:

        
        headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "82c45f8938mshd4299b0cbc6fab8p168798jsne36e71d4d35e",
	"X-RapidAPI-Host": "openai80.p.rapidapi.com"
}

        data = {
	"model": "text-davinci-003",
	"prompt": prompt,
	"max_tokens": 250,
	"temperature": 0,
	"top_p": 1,
	"n": 1,
	"stream": False,
	"logprobs": None,
	"stop": ""
}

        response = requests.post("https://openai80.p.rapidapi.com/completions", headers=headers, json=data)
        if response.status_code == 200:
            choices = response.json().get('choices')[0]
            text = choices.get('text')

    except Exception as e:
        print('ERROR:', e)

    return text



# def get_api_response(prompt: str) -> str | None:
#     text: str | None = None

#     try:
#         response: dict = openai.Completion.create(
#             model='text-davinci-003',
#             prompt=prompt,
#             temperature=0.9,
#             max_tokens=150,
#             top_p=1,
#             frequency_penalty=0,
#             presence_penalty=0.6,
#             # stop=[' Human:', ' AI:']
#         )

#         choices: dict = response.get('choices')[0]
#         text = choices.get('text')

#     except Exception as e:
#         print('ERROR:', e)

#     return text


def update_list(message: str, pl: list[str]):
    pl.append(message)


def create_prompt(message: str, pl: list[str]) -> str:
    p_message: str = f'\nHuman: {message}'
    update_list(p_message, pl)
    prompt: str = ''.join(pl)
    return prompt


def get_bot_response(message: str, pl: list[str]) -> str:
    prompt: str = create_prompt(message, pl)
    bot_response: str = get_api_response(prompt)
    

    if bot_response:


        update_list(bot_response, pl)
        pos: int = bot_response.find('\nAI: ')
        bot_response = bot_response[pos + 5:]
    else:
        bot_response = 'Something went wrong...'

    return bot_response


def main():
    prompt_list: list[str] = [
        '\nAI: always answer in  arabic language',
        '\nAI: you are a human make food order'
        '\nAI: when a user make an order ask him what he want to order',
        '\nAI: when a user say hello or hi ask him if he want to see the menu',
        '\nAI: ask him what is name , phone number, and the address',
              '\nAI: you have menu ',
              '\nAI: the menu contains large pizza costs 20EGP',
            '\nAI: the menu contains medium pizza costs 10EGP',
            '\nAI: the menu contains burger costs 10EGP',
            '\nAI: when he make the order, tell him the total cost'

              
                              
                              ]

    while True:


        # user_input: str = input()
        # response: str = get_bot_response(user_input, prompt_list)
        # print(response)
        latest_message = get_messages()
        if latest_message:
            sender_id = int(latest_message['from']['id'])



            response: str = get_bot_response(latest_message['message'], prompt_list)
            print(response)
            send_message(response, sender_id)


if __name__ == '__main__':

    main()



# 'you are bot sell products',
#     'you have product smart watch',
#     'the samrt watch has many features '
# '    Comes in a classic aesthetic design and includes a sports band as a gift'
# 'The watch is made of comfortable non-allergenic materials.'
# 'Has 11 watch faces to choose from and customize the background according to your preference.'
# 'Supports both Android and iOS systems, and can be connected to your phone via the FITPRO app.'
# 'Supports multiple languages, including Arabic and English.'
# 'Can receive notifications for messages (SMS), WhatsApp, and Facebook.'
# 'Includes medical measurements such as oxygen level, blood pressure, and heart rate monitoring.'
# 'Tracks various sports activities such as walking, running, and cycling, and records details such as calorie consumption and running duration.'
# 'Can track your sleep hours to help you maintain a healthy sleeping pattern.'
# 'Allows you to make and receive calls and control the watch using touch or buttons.'
# 'Has a camera remote feature, clear speaker, and phone-finding option.'
# 'the samrt watch has has  Description like '\

# 'Model: T55'
# 'Battery size: 170mAh'
# 'Band size: 260x20x2.3mm'
# 'Display: 1.3-inch touchscreen with a metal frame using TFT technology for higher quality and faster response with a thinner screen.'
# 'RAM: 128MB'
# 'Bluetooth: 4.0'
# 'System requirements: iOS 9.0 or higher / Android 5.0 or higher'
# 'Distance: Approximately 8-10 meters'
# 'Screen resolution: 240x240 pixels'
# 'Watch size: 44mm'
# 'Battery: Lithium battery'
# 'Operating voltage: 4.2'
# 'Battery life: Approximately 1.5-3 days'
# 'Charging time: Approximately 1.5 hours'

# 'Color: Black.'
#         'price: 400 egp'             