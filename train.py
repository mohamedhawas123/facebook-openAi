from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import csv
from chatterbot.response_selection import get_most_frequent_response
from pyarabic.araby import strip_tashkeel


bot = ChatBot(
    'ArabicBot',
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],

    response_selection_method=get_most_frequent_response, 
     logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
        }
    ]
)

def preprocess_arabic(text):
    return strip_tashkeel(text)

trainer = ListTrainer(bot)

# Train the bot on Arabic text


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
    preprocess_arabic("بكام اللاب "),
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


# استخدام chatterbot للرد على الأسئلة
while True:
    try:
        user_input = input("")
        bot_response = bot.get_response(user_input)
        print(bot_response)

    # إيقاف البرنامج عند الضغط على Ctrl-C
    except KeyboardInterrupt:
        break