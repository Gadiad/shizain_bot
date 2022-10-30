# - *- coding: utf-8 - *-
#from imp import reload
import telebot
import importlib
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from aiogram import types
#from mainn import bot, dp
#from PIL import Image, ImageEnchance
import os
import time
import json
import configg
import logging
from configg import *
from flask import Flask, request
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
#from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import pandas as pd
from aiogram import Bot, Dispatcher, executor
from configg import BOT_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from configg import admin_id
import sys
from importlib import reload
#importlib.reload(sys)
#reload(sys).setdefaultencoding("UTF8")
#sys.setdefaultencoding("UTF8")
bot = telebot.TeleBot('5714150030:AAGatoCz_E_CryJVeYhtSP4XEGs33hr15OY')
#bot = dp

server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

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


@bot.message_handler(Command("start"))
#@dp.message_handler(commands=["start"])
async def echo(message: Message):
    sti = open('sticker.webp', 'rb')
    await message.answer_animation(sti)
    text = "Привет! Мы - Рита и Женя☀ Мы студентки Школы Дизайна НИУ ВШЭ✌ Дожили уже до 4 курса на направлении " \
           "Анимация " \
           "и иллюстрация, после 1 года обучения пошли на специализацию Мультимедийный дизайн✊ Здесь будет информация " \
           "о полезных дизайн-штуках, различные материалы, работы лучших учеников да и вообще обо всем в сфере " \
           "дизайна❤️Рады тебя видеть! Напиши, как нам обращаться к тебе (имя и фамилия на английском языке! Например, Alexander Kurushin)?)️ "
    await message.answer(text=text)


@server.route(f"/{BOT_TOKEN}",methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@bot.message_handler(Command("ourinfo"))
async def show_items(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Евгения Никонова")
    keyboard.add(button_1)
    button_2 = types.KeyboardButton(text="Рита Лучникова")
    keyboard.add(button_2)
    await message.answer(f"{get_name(message)}, нажми на одну из кнопок ", reply_markup=keyboard)
    # await message.answer(f"Катюш, нажми на одну из кнопок", reply_markup=keyboard)


@bot.message_handler(Command("bestworks"))
async def show_items(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Лучшие работы учеников в области того-то")
    keyboard.add(button_1)
    button_2 = types.KeyboardButton(text="Лучшие работы учеников в области сего-то")
    keyboard.add(button_2)
    await message.answer(f"{get_name(message)}, нажми на одну из кнопок ", reply_markup=keyboard)



@bot.message_handler()
async def echo(message: Message):
    # if message.text == "каналы":
    #   text="\n".join(channels)
    # else:
    if message.text == 'Евгения Никонова':
        sti = open('Nikonova.jpg', 'rb')
        await message.answer_animation(sti)
        await message.answer(
            text="Привет! Я - Евгения Никонова, студентка 4 курса Школы Дизайна НИУ ВШЭ направления Анимации и иллюстрации✌ Специализация - Мультимидийный Дизайн \n О себе: симпатичная девушка из Мытищ, люблю свою кошку, встречаюсь с блаблаблаблаблаблаблаблаблаблаблаблаблаблаблабла и по жизни не высыпаюсь. Кстати, как там Андрей? Как его волейбольные успехи? Не надумал ли он сдавать физику ЕГЭ?")
    elif message.text == 'Рита Лучникова':
        stik = open('Luchnikova.jpg', 'rb')
        await message.answer_animation(stik)
        await message.answer(
            text=f"Привет! Я - Рита Лучникова, студентка 4 курса Школы Дизайна НИУ ВШЭ направления Анимации и иллюстрации✌ Специализация - Мультимидийный Дизайн. \n Где-то вдали пролетает комета, \n Празднично вьюга свирепствует где-то, \n Звери все ждут наступление лета, \n Я ж ослеплен проникающим светом. \n Свет этот льется повсюду, с небес,\n Он попадает и в море, и в лес,\n Где же источник? Хотелось бы знать,\n Может, покажешь иль скажешь мне, мать?)\n Холод окутывал тело мое,\n Сердце проткнуло стальное копье,\n Долго меня терзало мученье,\n Тьма без веселья - тоже ученье.\n Многое понял, узнал я ответ,\n Как да и кто излучает сей свет.\n Стало теплее, муки пропали,\n Все тараканы навзничь упали.\n Кто ж произвел необычный эффект?\n Чья красота и чей интеллект?\n Я скажу тихо, но все же послушай:\n Свет и тепло ты мне даришь, лягуша... ")
    elif message.text == 'Лучшие работы учеников в области того-то':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton(text="Работа Жени Кудрявцевой 100 баллов 2022")
        keyboard.add(button_1)
        button_2 = types.KeyboardButton(text="Работа Кати Ярославской 90 баллов 2018")
        keyboard.add(button_2)
        await message.answer(f"{get_name(message)}, нажми на одну из кнопок ", reply_markup=keyboard)
    elif message.text == 'Лучшие работы учеников в области сего-то':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton(text="Работа Риты Понасенко 95 баллов 2021")
        keyboard.add(button_1)
        button_2 = types.KeyboardButton(text="Работа Саши Гудкова 90 баллов 2019")
        keyboard.add(button_2)
        await message.answer(f"{get_name(message)}, нажми на одну из кнопок ", reply_markup=keyboard)
    else:
        d = {
            'name': [message.text],
            'id': [message.from_user.id]
        }
        write(d)
        text = f"Ok, {get_name(message)}, теперь нажми на кнопку Меню, чтобы увидеть, какие функции доступны  "
        await message.answer(text=text)
#@dp.message_handler("Лучшие работы учеников в области того-то")

async def show_items(message: types.Message):
    if message.text == 'Лучшие работы учеников в области того-то':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton(text="Работа Жени Кудрявцевой 100 баллов 2022")
        keyboard.add(button_1)
        button_2 = types.KeyboardButton(text="Работа Кати Ярославской 90 баллов 2018")
        keyboard.add(button_2)
        await message.answer(f"{get_name(message)}, нажми на одну из кнопок ", reply_markup=keyboard)
    elif message.text == 'Лучшие работы учеников в области сего-то':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton(text="Работа Риты Понасенко 95 баллов 2021")
        keyboard.add(button_1)
        button_2 = types.KeyboardButton(text="Работа Саши Гудкова 90 баллов 2019")
        keyboard.add(button_2)
        await message.answer(f"{get_name(message)}, нажми на одну из кнопок ", reply_markup=keyboard)


if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
#updater = Updater("5714150030:AAGatoCz_E_CryJVeYhtSP4XEGs33hr15OY")
#dpp = updater.dispatcher
#updater.start_polling()
#updater.idle()


#bot.polling(none_stop=True)

#async def show_items(message: types.Message):
 #   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  #  button_1 = types.KeyboardButton(text="Работа Жени Кудрявцевой 100 баллов 2022")
  #  keyboard.add(button_1)
   # button_2 = types.KeyboardButton(text="Работа Кати Ярославской 90 баллов 2018")
    #keyboard.add(button_2)
    #await message.answer(f"{get_name(message)}, нажми на одну из кнопок ", reply_markup=keyboard)
