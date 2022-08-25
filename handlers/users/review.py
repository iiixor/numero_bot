from aiogram import types
from loader import dp
from aiogram.types import CallbackQuery


from keyboards.inline.inline_switсh_language import *
from keyboards.inline.callback_datas import *
from filters.emoji import *


# @dp.message_handler ловит только сообщение 'Оставить отзыв'
@dp.message_handler(text=f'Отзывы {emoji_star}')
async def bot_portfolio(message: types.Message):
    # задаем текст, который будем выводить
    text = 'Выберете одну из кнопок:'
    # выводим текст методом message.answer и в аргументе предаем текст
    await message.answer(text, reply_markup=review_buttons)


# @dp.callback_query_handler специальный декоратор для
# отлавливания нажатия на инлай кнпоку
# фильтруем по парметру вида(см callback_datas) ну и собсна предаем туда его
# название, см (inline_switсh_language)


@dp.callback_query_handler(review_callback.filter(platform='platform_1'))
# в этой строке всегда всегда все стабильно, кроме callback_data: dict
# это опициональный параметр
async def bot_get_platform_1(call: CallbackQuery, callback_data: dict):
    # задаем текст, который будет присылаться в алерте
    allert_text = '# ДОБАВИТЬ ФУНКЦИОНАЛ'
    # при нажатии показывается алерт
    await call.answer(allert_text, show_alert=True)
    # все, что ниже опиционально
    print(f'callback_data_dict = {callback_data}')
    language = callback_data.get('language')


@dp.callback_query_handler(review_callback.filter(platform='write_a_review'))
async def bot_write_review(call: CallbackQuery, callback_data: dict):
    allert_text = '# ДОБАВИТЬ ФУНКЦИОНАЛ'
    await call.answer(allert_text, show_alert=True)
    print(f'callback_data_dict = {callback_data}')


    # вот как можно отправить опрос
    # await message.answer_poll(question='Выберете свою оценку', options=['5', '4', '3', '2', '1'], is_anonymous=False)
    # QESTION:  передаетеся название опроса
    # в options передаютеся поля опроса
