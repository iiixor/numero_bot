from aiogram import types
from loader import dp
from aiogram.types import CallbackQuery


from keyboards.inline.inline_switсh_language import *
from keyboards.inline.callback_datas import *
from filters.emoji import *


# @dp.message_handler ловит только сообщение 'Оставить отзыв'
@dp.message_handler(text=f'Прайс {emoji_abacus}')
async def bot_portfolio(message: types.Message):
    # задаем текст, который будем выводить
    text = f"Выберете одну из услуг:"
    # выводим текст методом message.answer и в аргументе предаем текст
    await message.answer(text, reply_markup=price_buttons)


# @dp.callback_query_handler специальный декоратор для
# отлавливания нажатия на инлай кнпоку
# фильтруем по парметру вида(см callback_datas) ну и собсна предаем туда его
# название, см (inline_switсh_language)


@dp.callback_query_handler(price_callback.filter(type='TG_Bots'))
# в этой строке всегда всегда все стабильно, кроме callback_data: dict
# это опициональный параметр
async def bot_get_platform_1(call: CallbackQuery, callback_data: dict):
    # задаем текст, который будет присылаться в алерте
    text = [f"<b>Разработка Telеgram ботов со следующим функционалом:</b> {emoji_robot}",
            "- Размещение на собственном хостинге",
            "- Подключение базы данных SQL",
            "- Настройка переадресации",
            "- Внедрение любого внутреннего функционала Теlеgram'a"]
    # при нажатии показывается алерт
    await call.message.answer('\n'.join(text))


@dp.callback_query_handler(price_callback.filter(type='ggsh_api'))
# в этой строке всегда всегда все стабильно, кроме callback_data: dict
# это опициональный параметр
async def bot_get_platform_2(call: CallbackQuery, callback_data: dict):
    # задаем текст, который будет присылаться в алерте
    text = [f"<b>Полная работа с Google Таблицами:</b> {emoji_statistics}",
            "- Разработка сводных таблиц",
            "- Автоматизация бизнес процессов",
            "- Работа с API через Python",
            "- Оформление базы данных"]
    # при нажатии показывается алерт
    await call.message.answer('\n'.join(text))
