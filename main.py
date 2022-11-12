import telebot
import keys as key
import logging
import time

bot = telebot.TeleBot(key.API_KEY)

logging.basicConfig(level=logging.INFO)

print("Bot started")
@bot.message_handler(commands=['hi', 'hello', 'hey'])
async def help(message):
    bot.send_message(message.chat.id, "Howdy, how are you doing?")
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "How can I help you sweetheart?")

bot.infinity_polling()
