from PIL import Image, ImageEnhance
import os
import time
import pandas as pd
from aiogram import types
import telebot
bot = telebot.TeleBot('5714150030:AAGatoCz_E_CryJVeYhtSP4XEGs33hr15OY')
filename = 'user_info.csv'

def write(usr):
    try:
        df = pd.read_csv(filename)
        if ((df['id'] == usr['id'][0]).any()):
            pass
        else:
            df = df.append(pd.DataFrame(usr))
            df.to_csv(filename, index=False)
    except:
        df = pd.DataFrame(usr)
        df.to_csv(filename, index=False)


def get_name(message):
    df = pd.read_csv(filename)
    print(df[df['id'] == message.from_user.id]['name'].iloc[0])
    return df[df['id'] == message.from_user.id]['name'].iloc[0]


users = {}


@bot.message_handler(commands=["start"])
async def echo(message):
    #sti = open('sticker.webp', 'rb')
    #await message.answer_animation(sti)
    text = "Привет! Мы - Рита и Женя☀ Мы студентки Школы Дизайна НИУ ВШЭ✌ Дожили уже до 4 курса на направлении " \
           "Анимация " \
           "и иллюстрация, после 1 года обучения пошли на специализацию Мультимедийный дизайн✊ Здесь будет информация " \
           "о полезных дизайн-штуках, различные материалы, работы лучших учеников да и вообще обо всем в сфере " \
           "дизайна❤️Рады тебя видеть! Напиши, как нам обращаться к тебе (имя и фамилия)?)️ "
    bot.send_message(message.from_user.id, text)

bot.polling(none_stop=True,interval=0)
