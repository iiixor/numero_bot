from aiogram import types
from loader import dp, bot
from aiogram.types import CallbackQuery

from keyboards.inline.inline_switсh_language import switch_language
from keyboards.inline.callback_datas import switch_callback
from keyboards.default import menu
from filters.emoji import *


# если в боте сообщение Поменять язык или Switch language
@dp.message_handler(text=f'Поменять язык {emoji_ruflag}')
async def bot_switch_language(message: types.Message):
    text = 'Выберете язык:'
    # задаем текст, который будем выводить (в переменную url)
    # выводим текст методом message.answer и в аргументе предаем текст
    await message.answer(text, reply_markup=switch_language)


# после шага выше спавняться кнопки, которые заданы в
# keyboads -> inline -> switch_language


@dp.callback_query_handler(switch_callback.filter(language='russian'))
async def bot_get_russian(call: CallbackQuery, callback_data: dict):
    text = '# ДОБАВИТЬ ФУНКЦИОНАЛ'
    await call.answer(text)
    print(f'callback_data_dict = {callback_data}')
    language = callback_data.get('language')
    await call.message.answer(f"Вы поменяли язык на Русский")


@dp.callback_query_handler(switch_callback.filter(language='english'))
async def bot_get_russian(call: CallbackQuery, callback_data: dict):
    text = '# ДОБАВИТЬ ФУНКЦИОНАЛ'
    await call.answer(text, show_alert=True)
    print(f'callback_data_dict = {callback_data}')
    language = callback_data.get('language')
    await call.message.answer(f"You've changed language on English")
