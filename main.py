import re
import json
import telebot
import keys as key

bot = telebot.TeleBot(key.API_KEY)


def start_bot(file):
    with open(file) as bot_responses:
        print("Bot started")
        return json.load(bot_responses)


bot_responses_data = start_bot("bot_responses.json")


def grab_random_responses(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())

    for data_response in bot_responses_data:
        required_response = 0
        required_words = data_response["required_words"]

        if required_words:
            for word in split_message:
                if word in required_words:
                    required_response += 1



while True:
    answers = input("User: ")
    print("Bot: ", grab_random_responses(answers))

# print("Bot started")
# @bot.message_handler(commands=['hi', 'hello', 'hey'])
# def help(message):
#     bot.send_message(message.chat.id, "Howdy, how are you doing?")
#
#
# @bot.message_handler(commands=['help'])
# def help(message):
#     bot.send_message(message.chat.id, "How can I help you sweetheart?")


bot.infinity_polling()
