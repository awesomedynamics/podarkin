import telebot
#import pymongo
#import pprint
from telebot import types
#from pymongo import MongoClient
#import time


no_keyboard = types.ReplyKeyboardRemove()

commands = ["GUESS WHAT?", "GUESS WHERE?", "GUESS WHO?", "GUESS HOW MUCH?","asdasdasd","asdasdasd","asdasdasdasd"]

#client = MongoClient("ds141786.mlab.com:41786", username = 'podarkin', password = 'podarkin', authSource = 'heroku_q51pzrtm')
#db = client["heroku_q51pzrtm"]
#gifts_collection = db.gifts


#pprint.pprint(gifts_collection.find_one())



bot = telebot.TeleBot("668546995:AAHHSnncgjXOLMwsHBHIrgYKMixhE_xPIoQ")

# подарки: 1 - билеты в чг 2 - банка черной икры 3 - коврик для йоги 4 - спа 5 - колючий коврик 6 - свечка  7 - рик и морти

#handling start or help command
@bot.message_handler(commands=['start','help'])
def start_command(message: telebot.types.Message):


    #message_dict = message.__dict__
    #startText = "GUESS WHAT ?"
    #bot.send_message(message.chat.id, startText)


    markup = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)

    markup.row(commands[0])

    bot.send_message(message.chat.id, "GUESS WHAT ?",
                     reply_markup=markup)

# билет в парк
@bot.message_handler(regexp=commands[0])
def gift_1(message: telebot.types.Message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.row(commands[1])
    answer = open("ticketlego.png","rb")
    answer_text = "🔥"
    bot.send_photo(chat_id=message.chat.id, photo=answer)
    bot.send_message(chat_id=message.chat.id, text = answer_text, reply_markup=markup)

#билет на самолет
@bot.message_handler(regexp=commands[1])
def gift_2(message: telebot.types.Message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.row(commands[2])
    answer = open("airticket.png","rb")
    bot.send_message(chat_id=message.chat.id, text="🔥",reply_markup=markup)
    bot.send_photo(chat_id = message.chat.id, photo = answer)

#кто
@bot.message_handler(regexp=commands[2])
def gift_3(message: telebot.types.Message):
    bot.send_message(chat_id=message.chat.id, text="@filissimos @katarinawin")
    bot.send_photo(chat_id=message.chat.id, photo=answer)

#черная икра
@bot.message_handler(regexp=commands[3])
def gift_4(message: telebot.types.Message):
    bot.send_message(chat_id=message.chat.id, text="твой баланс 💸 1400 AED - загуглишь сам")

#handling free text message
@bot.message_handler()
def free_text(message: telebot.types.Message):

    answer = "вынь хуй изо рта плиз и жми кнопки"
    bot.send_message(message.chat.id, answer)


bot.polling()