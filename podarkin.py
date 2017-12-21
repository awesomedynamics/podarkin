import telebot
import pymongo
import pprint

from pymongo import MongoClient

client = MongoClient("ds141786.mlab.com:41786", username = 'podarkin', password = 'podarkin', authSource = 'heroku_q51pzrtm')
db = client["heroku_q51pzrtm"]
gifts_collection = db.gifts


pprint.pprint(gifts_collection.find_one())



bot = telebot.TeleBot("474328854:AAEkbRpz5JWow9xD9LEJ42XC1eeRc79ZizU")

# подарки: 1 - билеты в чг 2 - банка черной икры 3 - коврик для йоги 4 - спа 5 - колючий коврик 6 - 7 -

#handling start or help command
@bot.message_handler(commands=['start','help'])
def start_command(message: telebot.types.Message):
    #message_dict = message.__dict__
    startText = "Привет! Я - Мистер Подаркин ! Хочешь подарок ? \n Первый нужно получить прямо сейчас, остальные - когда захочешь! \n Можно забрать все сразу или растянуть хоть на год "
    bot.send_message(message.chat.id, startText)
    commands = ["/gift_1", "/gift_2", "/gift_3", "/gift_5", "/gift_6", "/gift_7"]
    answer = "\n".join(commands)
    bot.send_message(message.chat.id, answer)

#handling /gifts
@bot.message_handler(commands=['gifts'])
def gifts(message: telebot.types.Message):
    gifts = ["/gift_1", "/gift_2", "/gift_3", "/gift_5", "/gift_6", "/gift_7"]
    answer = "\n".join(gifts)
    bot.send_message(message.chat.id, answer)

@bot.message_handler(commands=['gift_1'])
def gift_1(message: telebot.types.Message):
    answer = open("ticket.png","rb")
    bot.send_photo(chat_id = message.chat.id, photo = answer)
    answer_text = "У тебя всего один день чтобы собрать вещи :)"
    bot.send_message(chat_id=message.chat.id, text = answer_text)

@bot.message_handler(commands=['gift_2'])
def gift_2(message: telebot.types.Message):
    answer = open("ticket.png","rb")
    bot.send_photo(chat_id = message.chat.id, photo = answer)

@bot.message_handler(commands=['gift_3'])
def gift_3(message: telebot.types.Message):
    answer = open("ticket.png","rb")
    bot.send_photo(chat_id = message.chat.id, photo = answer)

@bot.message_handler(commands=['gift_4'])
def gift_4(message: telebot.types.Message):
    answer = open("ticket.png","rb")
    bot.send_photo(chat_id = message.chat.id, photo = answer)

@bot.message_handler(commands=['gift_5'])
def gift_5(message: telebot.types.Message):
    answer = open("ticket.png","rb")
    bot.send_photo(chat_id = message.chat.id, photo = answer)

@bot.message_handler(commands=['gift_6'])
def gift_6(message: telebot.types.Message):
    answer = open("ticket.png","rb")
    bot.send_photo(chat_id = message.chat.id, photo = answer)

@bot.message_handler(commands=['gift_7'])
def gift_7(message: telebot.types.Message):
    answer = open("ticket.png","rb")
    bot.send_photo(chat_id = message.chat.id, photo = answer)
    answer_text = "У тебя всего один день чтобы собрать вещи :)"
    bot.send_message(chat_id=message.chat.id, text = answer_text)

#handling free text message
@bot.message_handler()
def free_text(message: telebot.types.Message):

    answer = "Я не могу думать ни о чем кроме подарков! Забери их все!"
    bot.send_message(message.chat.id, answer)






bot.polling()