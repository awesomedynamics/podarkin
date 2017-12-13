import telebot

bot = telebot.TeleBot("452734858:AAH4JHqKW1MX2XjU2t8pvs1I-idowOvL4hA")

office_words = ["ОФИС", "ОФИСА" , "ОФИСНОЕ", "ОФИСНЫЕ"]
coworking_words = ["КОВОРКИНГ"]
event_words = ["МЕРОПРИЯТИЕ", "ПРЕЗЕНТАЦИЯ","КОНФЕРЕНЦИЯ","ПРЕЗЕНТАЦИЮ","КОНФЕРЕНЦИЮ","ТРЕНИНГ","КУРСЫ","ПЛОЩАДКА","ПОМЕЩЕНИЕ","ПЛОЩАДКУ","ПЛОЩАДКИ","КОРПОРАТИВНАЯ","ВЕЧЕРИНКА"]
date_words = ["ЯНВАРЯ","ФЕВРАЛЯ","МАРТА","АПРЕЛЯ","МАЯ","ИЮНЯ","ИЮЛЯ","АВГУСТА","СЕНТЯБРЯ","ОКТЯБРЯ","НОЯБРЯ","ДЕКАБРЯ"]
yes_words = ["ДА","ХОЧУ","БУДУ","НАВЕРНОЕ","ВОЗМОЖНО"]

answers = {
    "office_1": "Я покажу что у нас есть, сколько человек у вас в команде ?",
    "office_2": "У нас офисы от 4 человек, показать тебе офисы на четверых или рассказать о коворкинге ?",
    "office_3": "Вот что у нас есть на четверых",
    "office_4": "Вот что у нас есть на пятерых",
    "coworking_1": "Мы предлагаем плавающее рабочее место от 500 рублей в день, хочешь забронировать ?",
    "coworking_2": "Оставь телефон и мы тебе перезвоним",
    "coworking_3": "Спасибо, жди звонка!",
    "event_1": "Мы можем вместить до 150 человек - сколько вас будет ?",
    "event_2": "круто, когда планируете мероприятие ?",
    "event_3": "сколько часов потребуется ?",
}

urls = {
    "office_1": "",
    "office_2": "",
    "office_3": "http://tablica.work/#office#!/tproduct/34756154-1507644732627", # офис на четверых
    "office_4": "http://tablica.work/#!/tproduct/34756154-1498486301712", # офис на пятерых
    "coworking_1": ""
}

#handling start or help command
@bot.message_handler(commands=['start','help'])
def start_command(message: telebot.types.Message):
    #message_dict = message.__dict__
    startText = "Привет! Я - Мистер Подаркин ! Хочешь подарок ? Придется отгадать загадку! \n Первый нужно получить прямо сейчас, остальные - когда захочешь!"
    bot.send_message(message.chat.id, startText)
    commands = ["/Gift 1", "/Gift 2", "/Gift 3", "/Gift 5", "/Gift 6", "Gift 7"]
    answer = "\n".join(commands)
    bot.send_message(message.chat.id, answer)

#handling /gifts
@bot.message_handler(commands=['gifts'])
def gifts(message: telebot.types.Message):
    gifts = ["/Gift 1", "/Gift 2", "/Gift 3", "/Gift 5", "/Gift 6", "Gift 7"]
    answer = "\n".join(gifts)
    bot.send_message(message.chat.id, answer)

#handling free text message
@bot.message_handler()
def free_text(message: telebot.types.Message):

    answer = answers[step]
    bot.send_message(message.chat.id, answer)


@bot.message_handler(commands=['gift_1'])
def gifts(message: telebot.types.Message):
    gifts = ["/Gift 1", "/Gift 2", "/Gift 3", "/Gift 5", "/Gift 6", "Gift 7"]
    answer = "\n".join(gifts)
    bot.send_message(message.chat.id, answer)



bot.polling()