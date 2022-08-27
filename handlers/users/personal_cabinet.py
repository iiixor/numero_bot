from aiogram import types
from loader import dp, bot
from aiogram.types import CallbackQuery

from keyboards.inline.inline_switсh_language import *
from keyboards.inline.callback_datas import *
from filters.emoji import *
from parsing_data.parsing_main import *
from keyboards.default.menu import *
from keyboards.inline.subscribe_inline_button import *
from data.config import admins


# @dp.message_handler ловит только сообщение 'Получить информацию'
@dp.message_handler(text=f'Личный кабинет 👤')
async def bot_data_request(message: types.Message):
    subscribe_format=''
    if message.from_user.id in admins:
        subscribe_format='Полный'
    else:
        subscribe_format='Бесплатный'
    text = [
    f'<b>Ваше имя:</b> {message.from_user.full_name}',
    f'<b>Ваш ID:</b> {message.from_user.id}',
    f'<b>Формат подписки</b>: {subscribe_format}'
    ]
    # в переменную photo присваиваем фото(как абсолютный путь), которое в дальнешем будем отправлять
    # методом message.answer_photo отправляем фото и передаем туда photo
    # методом message.answer отправляем текст и передаем туда text
    await message.answer("\n".join(text), reply_markup=subscribe_button)
    # await bot.delete_message(message.chat.id, message.message_id)
