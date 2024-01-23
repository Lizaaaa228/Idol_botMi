import telebot
from telebot import types

# вставь сюда свой токен
token = "6935244452:AAGS4MdZh_N6jZLga6qTU0CZBvqtSLo1Z1E"
bot = telebot.TeleBot(token=token)


def filter_password(message):
    password = "хомяк"
    return password in message.text


@bot.message_handler(commands=['start'])
def start_func(message):
    bot.send_message(chat_id=message.chat.id, text=f'Привет, {message.from_user.first_name}\n'
                                                   f'В этом боте ты можешь пройти квиз про обычную девушку и её мечту!\n'
                                                   f'Чтобы начать историю нажми /start_story \n'
                                                   f'Если хочешь узнать что я могу жми /command_bot')


@bot.message_handler(content_types=['photo'])
def echo_photo(message):
    data = message.json
    photo = data['photo'][-1]['file_id']
    bot.send_photo(chat_id=message.chat.id, photo=photo)
    bot.send_message(chat_id=message.chat.id, text="Это фото, я угадал?")


@bot.message_handler(content_types=['video'])
def echo_video(message):
    data = message.json
    video = data['video']['file_id']
    bot.send_video(chat_id=message.chat.id, video=video)
    bot.send_message(chat_id=message.chat.id, text="Это видео, я угадал?")


from qiez_twee import epilog


@bot.message_handler(commands=['start_story'])
def start_func(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("SM Entertainment")
    item2 = types.KeyboardButton("STAR Entertainment")
    item3 = types.KeyboardButton("DP Entertainment")

    markup.add(item1, item2, item3)
    bot.send_message(chat_id=message.chat.id, text=epilog, reply_markup=markup)
    file = open("./Mie.jpg", "rb")
    bot.send_photo(message.chat.id, file)


from qiez_twee import command


@bot.message_handler(commands=['command_bot'])
def start_func(message):
    bot.send_message(chat_id=message.chat.id, text=command)


from qiez_twee import SM
from qiez_twee import STAR
from qiez_twee import DP
from qiez_twee import perfect_vocal
from qiez_twee import kpop_dance
from qiez_twee import dance
from qiez_twee import vocal
from qiez_twee import hiphop_dance
from qiez_twee import normal_vocal
from qiez_twee import no
from qiez_twee import the_end1
from qiez_twee import the_end12
from qiez_twee import the_end2
from qiez_twee import the_end3
from qiez_twee import the_end32


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == "private":
        if message.text == "SM Entertainment":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Превосходный вокал")
            item2 = types.KeyboardButton("Танцы k-pop")
            back = types.KeyboardButton("Назад")

            markup.add(item1, item2, back)

            bot.send_message(chat_id=message.chat.id, text=SM, reply_markup=markup)
            file = open("./sm.jpg", "rb")
            bot.send_photo(message.chat.id, file)

        elif message.text == "Превосходный вокал":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Да!")
            item2 = types.KeyboardButton("Нет")

            markup.add(item1, item2)

            bot.send_message(chat_id=message.chat.id, text=perfect_vocal, reply_markup=markup)
            file = open("./p5.jpg", "rb")
            bot.send_photo(message.chat.id, file)

        elif message.text == "Да!":
            bot.send_message(chat_id=message.chat.id, text=the_end1)
            file = open("./p12.jpg", "rb")
            bot.send_photo(message.chat.id, file)

        elif message.text == "Танцы k-pop":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Да")
            item2 = types.KeyboardButton("Нет")

            markup.add(item1, item2)

            bot.send_message(chat_id=message.chat.id, text=kpop_dance, reply_markup=markup)
            file = open("./p1.jpg", "rb")
            bot.send_photo(message.chat.id, file)

        elif message.text == "Да":
            bot.send_message(chat_id=message.chat.id, text=the_end12)
            file = open("./p14.jpg", "rb")
            bot.send_photo(message.chat.id, file)

        elif message.text == "Нет":
            bot.send_message(chat_id=message.chat.id, text=no)
            file = open("./p9.jpg", "rb")
            bot.send_photo(message.chat.id, file)

        if message.text == "STAR Entertainment":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Вокал")
            item2 = types.KeyboardButton("Танцы")
            back = types.KeyboardButton("Назад")

            markup.add(item1, item2, back)
            bot.send_message(chat_id=message.chat.id, text=STAR, reply_markup=markup)
            file = open("./star1.jpg", "rb")
            bot.send_photo(message.chat.id, file)

        elif message.text == "Вокал":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Да!!")
            item2 = types.KeyboardButton("Нет")

            markup.add(item1, item2)
            bot.send_message(chat_id=message.chat.id, text=vocal, reply_markup=markup)
            file = open("./p3.jpg", "rb")
            bot.send_photo(message.chat.id, file)

        elif message.text == "Да!!":
            bot.send_message(chat_id=message.chat.id, text=the_end2)
            file = open("./p16.jpg", "rb")
            bot.send_photo(message.chat.id, file)

        elif message.text == "Танцы":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Да!!")
            item2 = types.KeyboardButton("Нет")

            markup.add(item1, item2)
            bot.send_message(chat_id=message.chat.id, text=dance, reply_markup=markup)
            file = open("./p4.jpg", "rb")
            bot.send_photo(message.chat.id, file)

        elif message.text == "Да!!":
            bot.send_message(chat_id=message.chat.id, text=the_end2)
            file = open("./p16.jpg", "rb")
            bot.send_photo(message.chat.id, file)

        elif message.text == "DP Entertainment":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Средний вокал")
            item2 = types.KeyboardButton("Танцы хип-хоп")
            back = types.KeyboardButton("Назад")

            markup.add(item1, item2, back)
            bot.send_message(chat_id=message.chat.id, text=DP, reply_markup=markup)
            file = open("./dp.jpg", "rb")
            bot.send_photo(message.chat.id, file)

        elif message.text == "Средний вокал":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Да!!!")
            item2 = types.KeyboardButton("Нет")

            markup.add(item1, item2)
            bot.send_message(chat_id=message.chat.id, text=normal_vocal, reply_markup=markup)
            file = open("./p6.jpg", "rb")
            bot.send_photo(message.chat.id, file)

        elif message.text == "Да!!!":
            bot.send_message(chat_id=message.chat.id, text=the_end3)
            file = open("./p17.jpg", "rb")
            bot.send_photo(message.chat.id, file)

        elif message.text == "Танцы хип-хоп":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Да!)")
            item2 = types.KeyboardButton("Нет")
            back = types.KeyboardButton('Назад')

            markup.add(item1, item2, back)
            bot.send_message(chat_id=message.chat.id, text=hiphop_dance, reply_markup=markup)
            file = open("./p11.jpg", "rb")
            bot.send_photo(message.chat.id, file)

        elif message.text == "Да!)":
            bot.send_message(chat_id=message.chat.id, text=the_end32)
            file = open("./p14.jpg", "rb")
            bot.send_photo(message.chat.id, file)

        elif message.text == 'Назад':  # добавлена строка для обработки кнопки "Назад"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("SM Entertainment")
            item2 = types.KeyboardButton("STAR Entertainment")
            item3 = types.KeyboardButton('DP Entertainment')

            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, "Добро пожаловать обратно в главное меню!", reply_markup=markup)


bot.infinity_polling()

