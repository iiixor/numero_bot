from aiogram import types
from loader import dp, bot
from aiogram.types import CallbackQuery

from keyboards.inline.inline_switсh_language import *
from keyboards.inline.callback_datas import *
from filters.emoji import *
from parsing_data.parsing_main import *

@dp.callback_query_handler(skills_callback.filter(type='character'))
async def bot_get_skill(call: CallbackQuery):
    for item in get_skill(days, months, years, '1'):
        await message.answer(item)


@dp.callback_query_handler(skills_callback.filter(type='energy'))
async def bot_get_skill(call: CallbackQuery):
    for item in get_skill(days, months, years, '2'):
        await message.answer(item)


@dp.callback_query_handler(skills_callback.filter(type='interest'))
async def bot_get_skill(call: CallbackQuery):
    for item in get_skill(days, months, years, '3'):
        await message.answer(item)


@dp.callback_query_handler(skills_callback.filter(type='health'))
async def bot_get_skill(call: CallbackQuery):
    for item in get_skill(days, months, years, '4'):
        await message.answer(item)
 

@dp.callback_query_handler(skills_callback.filter(type='energy'))
async def bot_get_skill(call: CallbackQuery):
    for item in get_skill(days, months, years, '5'):
        await message.answer(item)


@dp.callback_query_handler(skills_callback.filter(type='energy'))
async def bot_get_skill(call: CallbackQuery):
    for item in get_skill(days, months, years, '6'):
        await message.answer(item)


@dp.callback_query_handler(skills_callback.filter(type='energy'))
async def bot_get_skill(call: CallbackQuery):
    for item in get_skill(days, months, years, '7'):
        await message.answer(item)


@dp.callback_query_handler(skills_callback.filter(type='energy'))
async def bot_get_skill(call: CallbackQuery):
    for item in get_skill(days, months, years, '8'):
        await message.answer(item)   


@dp.callback_query_handler(skills_callback.filter(type='energy'))
async def bot_get_skill(call: CallbackQuery):
    for item in get_skill(days, months, years, '9'):
        await message.answer(item)      



@dp.callback_query_handler(skills_callback.filter(type='energy'))
async def bot_get_skill(call: CallbackQuery):
    for item in get_skill(days, months, years, '10'):
        await message.answer(item)  