import telebot
#import pymongo
#import pprint
from telebot import types
#from pymongo import MongoClient
#import time


no_keyboard = types.ReplyKeyboardRemove()

commands = ["подарок раз!", "подарок два!", "подарок три!", "подарок четыре!", "подарок пять!", "подарок шесть!"]

#client = MongoClient("ds141786.mlab.com:41786", username = 'podarkin', password = 'podarkin', authSource = 'heroku_q51pzrtm')
#db = client["heroku_q51pzrtm"]
#gifts_collection = db.gifts


#pprint.pprint(gifts_collection.find_one())



bot = telebot.TeleBot("536919687:AAGxrbL3RM_6tjIe9ouaDi5caAvMxdgva8M")

# подарки: 1 - билеты в чг 2 - банка черной икры 3 - коврик для йоги 4 - спа 5 - колючий коврик 6 - свечка  7 - рик и морти

#handling start or help command
@bot.message_handler(commands=['start','help'])
def start_command(message: telebot.types.Message):


    #message_dict = message.__dict__
    startText = "Привет! Я - Твой клевый Санта ! Хочешь подарок ? Выбирай и жми кнопочку !"
    bot.send_message(message.chat.id, startText)


    markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)

    markup.row(commands[0],commands[1],commands[2])
    markup.row(commands[3], commands[4], commands[5])

    bot.send_message(message.chat.id, "выбери подарок:",
                     reply_markup=markup)

# билет в черногорию
@bot.message_handler(regexp=commands[0])
def gift_1(message: telebot.types.Message):
    answer = open("ticket.png","rb")
    answer_text = "сюрприз! ты не поверишь, но мы едем в черногорию 🏂"
    bot.send_photo(chat_id=message.chat.id, photo=answer)
    bot.send_message(chat_id=message.chat.id, text = answer_text)

#спа отель
@bot.message_handler(regexp=commands[1])
def gift_2(message: telebot.types.Message):
    answer = open("spa.png","rb")
    bot.send_message(chat_id=message.chat.id, text="little SPArty never killed nobody 🛀")
    bot.send_photo(chat_id = message.chat.id, photo = answer)

#колючий коврик
@bot.message_handler(regexp=commands[2])
def gift_3(message: telebot.types.Message):
    answer = open("kovplace.png", "rb")
    bot.send_message(chat_id=message.chat.id, text="а этот колючий подарок нужно будет поискать, вот подсказка:")
    bot.send_photo(chat_id=message.chat.id, photo=answer)

#черная икра
@bot.message_handler(regexp=commands[3])
def gift_4(message: telebot.types.Message):
    answer = open("ikra.jpg","rb")
    bot.send_message(chat_id=message.chat.id, text="ты же любишь черный ?!")
    bot.send_photo(chat_id = message.chat.id, photo = answer)

#рик и морти
@bot.message_handler(regexp=commands[4])
def gift_5(message: telebot.types.Message):
    bot.send_message(chat_id=message.chat.id, text="а это просто осквонченный подарок, сможешь отыскать ?!")
    answer = open("toshiba.jpg","rb")
    bot.send_photo(chat_id = message.chat.id, photo = answer)

# свечка
@bot.message_handler(regexp=commands[5])
def gift_6(message: telebot.types.Message):
    bot.send_message(chat_id=message.chat.id, text="тут будет сложно, найдешь с такой подсказкой ?!")
    answer = open("parma.png", "rb")
    bot.send_photo(chat_id=message.chat.id, photo=answer)


#handling free text message
@bot.message_handler()
def free_text(message: telebot.types.Message):

    answer = "Я не могу думать ни о чем кроме подарков! Забери их все -- !"
    bot.send_message(message.chat.id, answer)


bot.polling()