import telebot

bot = telebot.TeleBot("474328854:AAEkbRpz5JWow9xD9LEJ42XC1eeRc79ZizU")

# подарки: 1 - билеты в чг 2 - банка черной икры 3 - коврик для йоги

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
    gifts = ["/Gift 1", "/Gift 2", "/Gift 3", "/Gift 5", "/Gift 6", "Gift 7"]
    answer = "\n".join(gifts)
    bot.send_message(message.chat.id, answer)

@bot.message_handler(commands=['gift_1'])
def gift_1(message: telebot.types.Message):
    answer = open("ticket.png","rb")
    bot.send_photo(chat_id = message.chat.id, photo = answer)

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

#handling free text message
@bot.message_handler()
def free_text(message: telebot.types.Message):

    answer = "Я не могу думать ни о чем кроме подарков! Забери их все!"
    bot.send_message(message.chat.id, answer)






bot.polling()