import telebot
from telebot import types

bot = telebot.TeleBot('6551916291:AAHrq33hbQzlJWy7mubjsNM2laiGrDOM7DA')


from characterai import PyCAI

client = PyCAI('81da6bdced6150a7fc939ea82403c9c2910f0b3f')

@bot.message_handler(commands=['dialog'])
def chat(message):
    chat = 'EdSSlsl49k3wnwvMvK4eCh4yOFBaGTMJ7Q9CxtG2DiU'
    participants = chat['participants']

    if not participants[0]['is_human']:
        tgt = participants[0]['user']['username']
    else:
        tgt = participants[1]['user']['username']
    InputText = message.text
    print(InputText)
    while True:
        if len(InputText) != 0:
            data = client.chat.send_message(
                chat['external_id'], tgt, message
            )
            name = data['src_char']['participant']['name']
            text = data['replies'][0]['text']

            print(f"{name}: {text}")


@bot.message_handler(commands=['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Сайт нейросети', url ='https://beta.character.ai/'))
    bot.send_message(message.chat.id,f'Привет, {message.from_user.first_name} {message.from_user.last_name}  это бот, который будет делать что-то. Введи /help для помощи. Еще разрабатывается...', reply_markup=markup)

@bot.message_handler(commands=['developer'])
def main(message):
    bot.send_message(message.chat.id,'https://github.com/gettinghotter')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Для связи с разработчиком напиши /developer')

@bot.message_handler(commands=['messagecommands'])
def main(message):
    bot.send_message(message.chat.id, message)


@bot.message_handler()
def info(message):
    if message.text.lower()  == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')

bot.polling(none_stop=True)