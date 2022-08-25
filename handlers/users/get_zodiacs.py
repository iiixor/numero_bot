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


dp.message_handler(text=f'Скорпион ♏️')
async def bot_zodiac_request(message: types.Message):
    text = get_today_horoscope('scorpio')
    await message.answer(text)

dp.message_handler(text=f'Стрелец ♐️')
async def bot_zodiac_request(message: types.Message):
    text = get_today_horoscope('sagittarius')
    await message.answer(text)