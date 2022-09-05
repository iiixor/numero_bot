from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot
# достаем menu из дир-и delpy_bot -> keyboards -> default
from keyboards.default import menu
from filters.emoji import *

import sqlite3
from utils.db_api.sqlite import Database

db = Database()

# @dp.message_handler ловит только комманду /start
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(user_id=message.from_user.id, name=message.from_user.full_name, subscribe=False, FSM_horoscope=0, FSM_square=0)
    except sqlite3.IntegrityError as err:
        print(err)

    text = f'<b>Вселенский</b> приветсвует Вас, {message.from_user.full_name} 👋'

    await message.answer(text, reply_markup=menu)
