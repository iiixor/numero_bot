from aiogram import types
from loader import dp, bot
from aiogram.types import CallbackQuery

from keyboards.inline.inline_switсh_language import *
from keyboards.inline.callback_datas import *
from filters.emoji import *
from parsing_data.parsing_main import *


# @dp.message_handler ловит только сообщение 'Получить информацию'
@dp.message_handler(text=f'Посмотреть квадрат пифагора ⚛️')
async def bot_data_request(message: types.Message):
    text = f'Введите дату рождения в формате:\n День.Месяц.Год \n <i>Например: 29.05.1980</i>'
    # в переменную photo присваиваем фото(как абсолютный путь), которое в дальнешем будем отправлять
    # методом message.answer_photo отправляем фото и передаем туда photo
    # методом message.answer отправляем текст и передаем туда text
    await message.answer(text)
    # await bot.delete_message(message.chat.id, message.message_id)

@dp.message_handler()
async def bot_pif_square(message: types.Message):
    date_for_parsing = message.text
    date_for_parsing  = date_for_parsing.split('.')
    days = date_for_parsing[0]
    months = date_for_parsing[1]
    years = date_for_parsing[2]
    text = ''
    for item in get_pifagor(days, months, years):
        text = text + f'{item}' + '\n'
    await message.answer('Формирую квадрат Пифагора...')
    await message.answer(text)
    await message.answer('Выберете один из показателей:', reply_markup=skills_buttons)


    @dp.callback_query_handler(skills_callback.filter(type='character'))
    async def bot_get_skill(call: CallbackQuery):
        for item in get_skill_from_parsing(days, months, years, '1'):
            await message.answer(item)
        # await message.answer('Выберете один из показателей:', reply_markup=skills_buttons)


    @dp.callback_query_handler(skills_callback.filter(type='energy'))
    async def bot_get_skill(call: CallbackQuery):
        for item in get_skill_from_parsing(days, months, years, '2'):
            await message.answer(item)
        # await message.answer('Выберете один из показателей:', reply_markup=skills_buttons)

    @dp.callback_query_handler(skills_callback.filter(type='interest'))
    async def bot_get_skill(call: CallbackQuery):
        for item in get_skill_from_parsing(days, months, years, '3'):
            await message.answer(item)



    @dp.callback_query_handler(skills_callback.filter(type='health'))
    async def bot_get_skill(call: CallbackQuery):
        # await bot.delete_message(message.chat.id, message.message_id)
        for item in get_skill_from_parsing(days, months, years, '4'):
            await message.answer(item)


    @dp.callback_query_handler(skills_callback.filter(type='logic'))
    async def bot_get_skill(call: CallbackQuery):
        for item in get_skill_from_parsing(days, months, years, '5'):
            await message.answer(item)


    @dp.callback_query_handler(skills_callback.filter(type='labour'))
    async def bot_get_skill(call: CallbackQuery):
        for item in get_skill_from_parsing(days, months, years, '6'):
            await message.answer(item)


    @dp.callback_query_handler(skills_callback.filter(type='luck'))
    async def bot_get_skill(call: CallbackQuery):
        for item in get_skill_from_parsing(days, months, years, '7'):
            await message.answer(item)          


    @dp.callback_query_handler(skills_callback.filter(type='duty'))
    async def bot_get_skill(call: CallbackQuery):
        for item in get_skill_from_parsing(days, months, years, '8'):
            await message.answer(item) 


    @dp.callback_query_handler(skills_callback.filter(type='memory'))
    async def bot_get_skill(call: CallbackQuery):
        for item in get_skill_from_parsing(days, months, years, '9'):
            await message.answer(item) 


    @dp.callback_query_handler(skills_callback.filter(type='сommitment'))
    async def bot_get_skill(call: CallbackQuery):
        for item in get_skill_from_parsing(days, months, years, '10'):
            await message.answer(item) 


    @dp.callback_query_handler(skills_callback.filter(type='family'))
    async def bot_get_skill(call: CallbackQuery):
        for item in get_skill_from_parsing(days, months, years, '11'):
            await message.answer(item) 


    @dp.callback_query_handler(skills_callback.filter(type='stability'))
    async def bot_get_skill(call: CallbackQuery):
        for item in get_skill_from_parsing(days, months, years, '12'):
            await message.answer(item) 


    @dp.callback_query_handler(skills_callback.filter(type='self_esteem'))
    async def bot_get_skill(call: CallbackQuery):
        for item in get_skill_from_parsing(days, months, years, '13'):
            await message.answer(item) 


    @dp.callback_query_handler(skills_callback.filter(type='material_independence'))
    async def bot_get_skill(call: CallbackQuery):
        for item in get_skill_from_parsing(days, months, years, '14'):
            await message.answer(item) 


    @dp.callback_query_handler(skills_callback.filter(type='talant'))
    async def bot_get_skill(call: CallbackQuery):
        for item in get_skill_from_parsing(days, months, years, '15'):
            await message.answer(item) 


    @dp.callback_query_handler(skills_callback.filter(type='tempepament'))
    async def bot_get_skill(call: CallbackQuery):
        for item in get_skill_from_parsing(days, months, years, '16'):
            await message.answer(item) 


    @dp.callback_query_handler(skills_callback.filter(type='spirit'))
    async def bot_get_skill(call: CallbackQuery):
        for item in get_skill_from_parsing(days, months, years, '17'):
            await message.answer(item) 

# @dp.callback_query_handler(skills_callback.filter(type='character'))
# async def bot_get_skill(call: CallbackQuery):
#     days = bot_pif_square()
#     print(days)
        # for item in get_skill(days, months, years, '1'):
        #     await message.answer(item)
    # text = ''
    # for item in get_skill(days, months, years, '4'):
    #     text = text + f'{item}' + '\n'
    #     await message.answer(item)
    # await message.answer(text)
