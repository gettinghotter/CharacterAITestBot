import telebot
import webbrowser
bot = telebot.TeleBot('6551916291:AAHrq33hbQzlJWy7mubjsNM2laiGrDOM7DA')


@bot.message_handler(commands=['developer'])
def main(message):
    bot.send_message(message.chat.id,'https://github.com/gettinghotter')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,f'Привет, {message.from_user.first_name} {message.from_user.last_name}  это бот, который будет делать что-то. Введи /help для помощи. Еще разрабатывается...')

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



bot.infinity_polling(none_stop=True)