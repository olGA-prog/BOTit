import telebot
from telebot import types

bot = telebot.TeleBot('5027886013:AAHs0_BmG8K5ZThWQdoZiMb5tB6wCNdOVFA')


@bot.message_handler(commands=['website'])
def open_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://tproger.ru"))
    bot.send_message(message.chat.id,
                     "Отличный выбор, вот ссылка", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['tele'])
def help(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Хотите познакомиться с автором?", url="https://t.me/vredina_o"))
    bot.send_message(message.chat.id,
                     "Всегда рада вас слышать!", parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    get_mess_bot = message.text.strip().lower()

    if get_mess_bot == "начать тест заново":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Создание игр')
        btn2 = types.KeyboardButton('Мобильные приложения')
        btn3 = types.KeyboardButton('Веб разработка')
        btn4 = types.KeyboardButton('Софт для пк')
        btn5 = types.KeyboardButton('Обработка данных')
        btn6 = types.KeyboardButton('Создание ИИ')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

        final_message = "Решил попробовать что-то ещё? \nВыбери какое направление тебя интересует:"


    elif get_mess_bot == "создание игр":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Под мобильные телефоны')
        btn2 = types.KeyboardButton('Компьютеры и консоли')
        btn3 = types.KeyboardButton('Виртуальная реальность ')
        btn4 = types.KeyboardButton('Веб игры ')
        btn5 = types.KeyboardButton('Начать тест заново')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        final_message = "Крутая тема,но под что хочешь разрабатывать?"
    elif get_mess_bot == "под мобильный телефоны":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курсы по Unity", url="https://itproger.com/tag/unity"))
        final_message = "Для разработки игр под мобильные устройства зачастую используется игровой движок <a href='https://itproger.com/tag/unity'>Unity</a>\nДвижок прост в изучении и вы можете просмотреть курсы по нему по кнопке ниже"

    if get_mess_bot == "мобильные приложения":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('iOS')
        btn2 = types.KeyboardButton('Андроид')
        markup.add(btn1, btn2)
        final_message = "Для разработки игр нужно определиться с направлением. Выбери его:"

    if get_mess_bot == "веб разработка":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Оболочка(front-end)')
        btn2 = types.KeyboardButton('Работа с сервером(back-end)')
        markup.add(btn1, btn2)
        final_message = "Для разработки игр нужно определиться с направлением. Выбери его:"

    if get_mess_bot == "cофт для пк":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Windows')
        btn2 = types.KeyboardButton('Mac')
        btn3 = types.KeyboardButton('Все платформы')
        markup.add(btn1, btn2, btn3)
        final_message = "Для разработки игр нужно определиться с направлением. Выбери его:"

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Создание игр')
        btn2 = types.KeyboardButton('Мобильные приложения')
        btn3 = types.KeyboardButton('Веб разработка')
        btn4 = types.KeyboardButton('Софт для пк')
        btn5 = types.KeyboardButton('Обработка данных')
        btn6 = types.KeyboardButton('Создание ИИ')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        final_message = "Ой! Что-то пошло не так...попробуй нажать на кнопки ниже"

    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    get_mess_bot = message.text.strip().lower()
    if get_mess_bot == "под мобильные телефоны":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Для разработки игр под мобильные устройства зачастую используется игровой"
        " движок Unity. ", url="https://itproger.com/tag/unity?"))
        bot.send_message(message.chat.id, "Всегда рада вас слышать!", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Создание игр')
    btn2 = types.KeyboardButton('Мобильные приложения')
    btn3 = types.KeyboardButton('Веб разработка')
    btn4 = types.KeyboardButton('Софт для пк')
    btn5 = types.KeyboardButton('Обработка данных')
    btn6 = types.KeyboardButton('Создание ИИ')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    send_mess = f"<b>Привет {message.from_user.first_name}{message.from_user.last_name}</b>\n Какое напрвление тебя интересует?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)



bot.polling(none_stop=True)

print()