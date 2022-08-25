from aiogram import types
from loader import dp, bot
from aiogram.types import CallbackQuery

from keyboards.inline.inline_switсh_language import *
from keyboards.inline.callback_datas import *
from filters.emoji import *


# @dp.message_handler ловит только сообщение 'Получить информацию'
@dp.message_handler(text=f'Посмотреть квадрат пифагора ⚛️')
async def bot_info(message: types.Message):
    text = f'Введите дату рождения в формате:\n День.Месяц.Год \n <i>Например: 29.05.1980</i>'
    # в переменную photo присваиваем фото(как абсолютный путь), которое в дальнешем будем отправлять
    # методом message.answer_photo отправляем фото и передаем туда photo
    # методом message.answer отправляем текст и передаем туда text
    await message.answer(text)
    # await bot.delete_message(message.chat.id, message.message_id)

@dp.message_handler()
async def bot_info(message: types.Message):
    date_for_parsing = message.text
    date_for_parsing  = date_for_parsing.split('.')
    days = date_for_parsing[0]
    months = date_for_parsing[1]
    years = date_for_parsing[2]
    await message.answer('Формирую квадрат Пифагора...')
