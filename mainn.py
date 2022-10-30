import pandas as pd

import configg
from aiogram import Bot, Dispatcher, executor
from configg import BOT_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import pandas

bot = Bot(BOT_TOKEN, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

if __name__ == "__main__":


    from aiogram import executor
    from sambot import dp
    executor.start_polling(dp)