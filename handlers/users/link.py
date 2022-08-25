from aiogram import types
from loader import dp
from aiogram.types import CallbackQuery


from keyboards.inline.inline_switсh_language import *
from keyboards.inline.callback_datas import *
from filters.emoji import *


# @dp.message_handler ловит только сообщение 'Перейти на сайт'
@dp.message_handler(text=f'Пройти опрос {emoji_paper_pen}')
async def bot_link(message: types.Message):
    # задаем текст, который будем выводить (в переменную url)
    text = 'Перейдите по одной из ссылок ниже:'
    # выводим текст методом message.answer и в аргументе предаем текст
    await message.answer(text, reply_markup=poll_buttons)


@dp.callback_query_handler(poll_callback.filter(platform='google_forms'))
async def bot_get_russian(call: CallbackQuery, callback_data: dict):
    allert_text = f'# ДОБАВИТЬ ССЫЛКУ НА GOOGLE FORMS'
    await call.answer(allert_text, show_alert=True)
    print(f'callback_data_dict = {callback_data}')
    language = callback_data.get('language')
