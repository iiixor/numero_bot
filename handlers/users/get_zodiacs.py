from aiogram import types
from loader import dp, bot
from aiogram.types import CallbackQuery

from keyboards.inline.inline_switсh_language import *
from keyboards.inline.callback_datas import *
from filters.emoji import *
from parsing_data.parsing_main import *
from parsing_data.zodiac_parsing import *
from keyboards.default import aditional_numerology
from keyboards.default.aditional_numerology import *

# # 
# #
# #
#
# from datetime import datetime #библиотека для работы с датами
# #создаем класс для даты последнего юза
# class previousDate:
#
#     #устанавливаем нереальную дату для инициализации
#     def __init__(self, Date = datetime(1900,1,1,1,1,1)):
#          self._Date = Date
#
#     # getter method
#     def get_Date(self):
#         return self._Date
#
#     # setter method
#     def set_Date(self, value):
#         self._Date = value
#
# #создаем переменную для проверки доступа к Бонусу
# def square_Access(prev, cur):
#     access = False
#     #сравниваем сколько прошло времени с последнего юза
#     if (cur - prev._Date).total_seconds() > 86400: # 86400 секунд = 24 часа
#         access = True
#         #в случае, если прошло более 24 часов, устанавливаем новую последнюю дату
#         prev.set_Date(cur)
#     return access
#
# prevDate = previousDate()
#
# #отправляем в нашу переменную доступа объект последней даты и текущую дату
# if (square_Access(prevDate, datetime.now())):
#     FSM_square()
#
#     async def bonus(message: types.Message):
#     con = sqlite3.connect("users.db")
#     cur = con.cursor()
#     user = message.from_user.id
#     sql = "UPDATE ids SET balance = balance + ? \
#     WHERE user_id = ?"
#     val = (15, user)
#     cur.execute(sql, val)
#     con.commit()
#     await bot.send_message(message.chat.id, "Вам выдан бонус в качестве 15 монеток")
#     cur.close()
# #
# #
# #

# @dp.message_handler ловит только сообщение 'Получить информацию'
@dp.message_handler(text=f'Посмотреть гороскоп ☯️')
async def bot_zodiac_request(message: types.Message):
    text = f'Выберете знак зодиака:'
    # в переменную photo присваиваем фото(как абсолютный путь), которое в дальнешем будем отправлять
    # методом message.answer_photo отправляем фото и передаем туда photo
    # методом message.answer отправляем текст и передаем туда text
    await message.answer(text, reply_markup=zodiacs)
    # await bot.delete_message(message.chat.id, message.message_id)

@dp.message_handler(text=f'Козерог ♑️')
async def bot_zodiac_request(message: types.Message):
    text = get_today_horoscope('capricorn')
    await message.answer(text)


@dp.message_handler(text=f'Водолей ♒️')
async def bot_zodiac_request(message: types.Message):
    text = get_today_horoscope('aquarius')
    await message.answer(text)


@dp.message_handler(text=f'Рыбы ♓️')
async def bot_zodiac_request(message: types.Message):
    text = get_today_horoscope('pisces')
    await message.answer(text)


@dp.message_handler(text=f'Овен ♈️')
async def bot_zodiac_request(message: types.Message):
    text = get_today_horoscope('aries')
    await message.answer(text)


@dp.message_handler(text=f'Телец ♉️')
async def bot_zodiac_request(message: types.Message):
    text = get_today_horoscope('taurus')
    await message.answer(text)


@dp.message_handler(text=f'Близнецы ♊️')
async def bot_zodiac_request(message: types.Message):
    text = get_today_horoscope('gemini')
    await message.answer(text)


@dp.message_handler(text=f'Рак ♋️')
async def bot_zodiac_request(message: types.Message):
    text = get_today_horoscope('cancer')
    await message.answer(text)


@dp.message_handler(text=f'Лев ♌️')
async def bot_zodiac_request(message: types.Message):
    text = get_today_horoscope('leo')
    await message.answer(text)


@dp.message_handler(text=f'Дева ♍️')
async def bot_zodiac_request(message: types.Message):
    text = get_today_horoscope('virgo')
    await message.answer(text)


@dp.message_handler(text=f'Весы ♎️')
async def bot_zodiac_request(message: types.Message):
    text = get_today_horoscope('libra')
    await message.answer(text)


@dp.message_handler(text=f'Скорпион ♏️')
async def bot_zodiac_request(message: types.Message):
    text = get_today_horoscope('scorpio')
    await message.answer(text)


@dp.message_handler(text=f'Стрелец ♐️')
async def bot_zodiac_request(message: types.Message):
    text = get_today_horoscope('sagittarius')
    await message.answer(text)
