import logging
import time
import telebot
import keys as key
import aiogram


bot = telebot.TeleBot(key.API_KEY)

logging.basicConfig(level=logging.INFO)

print("Bot started")


@bot.message_handler(commands=['hi', 'hello', 'hey'])
def hello(message):
    bot.send_message(message.chat.id, f"Howdy, {message.from_user.first_name} how are you doing?")
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "How can I help you sweetheart?")

@bot.message_handler()
def get_user_session_info(message):
    if message.text == ['user']:
        bot.send_message(message.chat.id, "Hi user", parse_mode='html')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f"Your user_id is: {message.from_user.id}",  parse_mode='html')

    bot.send_message(message.chat.id, message, parse_mode='html')


bot.infinity_polling()
