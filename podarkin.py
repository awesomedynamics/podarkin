import telebot
import pymongo
import pprint
from telebot import types
from pymongo import MongoClient
import time


no_keyboard = types.ReplyKeyboardRemove()

client = MongoClient("ds141786.mlab.com:41786", username = 'podarkin', password = 'podarkin', authSource = 'heroku_q51pzrtm')
db = client["heroku_q51pzrtm"]
gifts_collection = db.gifts


pprint.pprint(gifts_collection.find_one())



bot = telebot.TeleBot("474328854:AAEkbRpz5JWow9xD9LEJ42XC1eeRc79ZizU")

# подарки: 1 - билеты в чг 2 - банка черной икры 3 - коврик для йоги 4 - спа 5 - колючий коврик 6 - свечка  7 - рик и морти

#handling start or help command
@bot.message_handler(commands=['start','help'])
def start_command(message: telebot.types.Message):


    #message_dict = message.__dict__
    startText = "Привет! Я - Мистер Подаркин ! Хочешь подарок ? \n Можно забрать все сразу или растянуть хоть на год! "
    bot.send_message(message.chat.id, startText)
    commands = ["подарок 1", "подарок 2", "подарок 3", "подарок 4", "подарок 5", "подарок 6"]

    markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)

    markup.row(commands[0],commands[1],commands[2])
    markup.row(commands[3], commands[4], commands[5])

    bot.send_message(message.chat.id, "выбери подарок:",
                     reply_markup=markup)

# билет в черногорию
@bot.message_handler(regexp='подарок 1')
def gift_1(message: telebot.types.Message):
    answer = open("ticket.png","rb")
    answer_text = "это должен был быть сюрприз :)"
    bot.send_photo(chat_id=message.chat.id, photo=answer)
    bot.send_message(chat_id=message.chat.id, text = answer_text)

#спа отель
@bot.message_handler(regexp='подарок 2')
def gift_2(message: telebot.types.Message):
    answer = open("spa.png","rb")
    bot.send_message(chat_id=message.chat.id, text="немножко СПА")
    bot.send_photo(chat_id = message.chat.id, photo = answer)

#колючий коврик
@bot.message_handler(regexp='подарок 3')
def gift_3(message: telebot.types.Message):
    answer = open("kovplace.jpg","rb")
    bot.send_photo(chat_id = message.chat.id, photo = answer)

#черная икра
@bot.message_handler(regexp='подарок 4')
def gift_4(message: telebot.types.Message):
    answer = open("kovplace.jpg","rb")
    bot.send_message(chat_id=message.chat.id, text="а тут нужно будет поискать, вот подсказка:")
    bot.send_photo(chat_id = message.chat.id, photo = answer)

#рик и морти
@bot.message_handler(regexp='подарок 5')
def gift_5(message: telebot.types.Message):
    bot.send_message(chat_id=message.chat.id, text="а это просто осквонченный подарок!")
    answer = open("ticket.png","rb")
    bot.send_photo(chat_id = message.chat.id, photo = answer)

# просто новый коврик или свечка или что еще 
@bot.message_handler(regexp='подарок 6')
def gift_6(message: telebot.types.Message):
    answer = open("ticket.png","rb")
    bot.send_photo(chat_id = message.chat.id, photo = answer)


#handling free text message
@bot.message_handler()
def free_text(message: telebot.types.Message):

    answer = "Я не могу думать ни о чем кроме подарков! Забери их все!"
    bot.send_message(message.chat.id, answer)


bot.polling()