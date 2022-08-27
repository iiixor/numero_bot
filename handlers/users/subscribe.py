from aiogram import types
from loader import dp, bot
from aiogram.types import CallbackQuery

from keyboards.inline.inline_switсh_language import *
from keyboards.inline.callback_datas import *
from filters.emoji import *
from parsing_data.parsing_main import *
from keyboards.default.menu import *
from keyboards.inline import subscribe_inline_button

@dp.message_handler(text=f'Оформить подписку')
async def bot_data_request(message: types.Message):
    text = f'# ДОБАВИТЬ КНОПКУ НА ПЛАТЕЖУ'
    # в переменную photo присваиваем фото(как абсолютный путь), которое в дальнешем будем отправлять
    # методом message.answer_photo отправляем фото и передаем туда photo
    # методом message.answer отправляем текст и передаем туда text
    await message.answer(text)
    # await bot.delete_message(message.chat.id, message.message_id)

@dp.message_handler(text=f'Назад')
async def bot_data_request(message: types.Message):
    text = f'Выберете одну из кнопок:'
    await message.answer(text, reply_markup=menu)
    # await bot.delete_message(message.chat.id, message.message_id)


@dp.callback_query_handler(subscribe_callback.filter(type='yes'))
async def bot_get_russian(call: CallbackQuery):
    allert_text = f'# ДОБАВИТЬ ПЛАТЕЖКУ'
    await call.answer(allert_text, show_alert=False)
