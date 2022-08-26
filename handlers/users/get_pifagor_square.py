from aiogram import types
from loader import dp, bot
from aiogram.types import CallbackQuery

from keyboards.inline.inline_switсh_language import *
from keyboards.inline.callback_datas import *
from filters.emoji import *
from parsing_data.parsing_main import *
from keyboards.default import aditional_numerology


# @dp.message_handler ловит только сообщение 'Получить информацию'
@dp.message_handler(text=f'Посмотреть квадрат пифагора ⚛️')
async def bot_data_request(message: types.Message):
    text = f'Введите дату рождения в формате:\n\n<b>День.Месяц.Год</b>\n\n<i>Например: 29.05.1980</i>'
    # в переменную photo присваиваем фото(как абсолютный путь), которое в дальнешем будем отправлять
    # методом message.answer_photo отправляем фото и передаем туда photo
    # методом message.answer отправляем текст и передаем туда text
    await message.answer(text)
    # await bot.delete_message(message.chat.id, message.message_id)


@dp.message_handler(text=f'Характер')
async def bot_data_request(message: types.Message):
    print(message.text)
    for item in get_skill_from_parsing('1'):
        await message.answer(item)
    # await message.answer('Выберете один из показателей:', reply_markup=skills_buttons)


@dp.message_handler(text=f'Энергия')
async def bot_data_request(message: types.Message):
    print(message.text)
    for item in get_skill_from_parsing('2'):
        await message.answer(item)
    # await message.answer('Выберете один из показателей:', reply_markup=skills_buttons)

@dp.message_handler(text=f'Интерес')
async def bot_data_request(message: types.Message):
    print(message.text)
    for item in get_skill_from_parsing('3'):
        await message.answer(item)
    # await message.answer('Выберете один из показателей:', reply_markup=skills_buttons)


@dp.message_handler(text=f'Здоровье')
async def bot_data_request(message: types.Message):
    print(message.text)
    for item in get_skill_from_parsing('4'):
        await message.answer(item)
    # await message.answer('Выберете один из показателей:', reply_markup=skills_buttons)


@dp.message_handler(text=f'Логика, Интуиция')
async def bot_data_request(message: types.Message):
    print(message.text)
    for item in get_skill_from_parsing('5'):
        await message.answer(item)
    # await message.answer('Выберете один из показателей:', reply_markup=skills_buttons)


@dp.message_handler(text=f'Труд')
async def bot_data_request(message: types.Message):
    print(message.text)
    for item in get_skill_from_parsing('6'):
        await message.answer(item)
    # await message.answer('Выберете один из показателей:', reply_markup=skills_buttons)


@dp.message_handler(text=f'Удача')
async def bot_data_request(message: types.Message):
    print(message.text)
    for item in get_skill_from_parsing('7'):
        await message.answer(item)
    # await message.answer('Выберете один из показателей:', reply_markup=skills_buttons)


@dp.message_handler(text=f'Чувство долга')
async def bot_data_request(message: types.Message):
    print(message.text)
    for item in get_skill_from_parsing('8'):
        await message.answer(item)
    # await message.answer('Выберете один из показателей:', reply_markup=skills_buttons)


@dp.message_handler(text=f'Память')
async def bot_data_request(message: types.Message):
    print(message.text)
    for item in get_skill_from_parsing('9'):
        await message.answer(item)
    # await message.answer('Выберете один из показателей:', reply_markup=skills_buttons)

@dp.message_handler(text=f'Целеустремленность')
async def bot_data_request(message: types.Message):
    print(message.text)
    for item in get_skill_from_parsing('10'):
        await message.answer(item)
    # await message.answer('Выберете один из показателей:', reply_markup=skills_buttons)


@dp.message_handler(text=f'Семья')
async def bot_data_request(message: types.Message):
    print(message.text)
    for item in get_skill_from_parsing('11'):
        await message.answer(item)
    # await message.answer('Выберете один из показателей:', reply_markup=skills_buttons)


@dp.message_handler(text=f'Стабильность')
async def bot_data_request(message: types.Message):
    print(message.text)
    for item in get_skill_from_parsing('12'):
        await message.answer(item)
    # await message.answer('Выберете один из показателей:', reply_markup=skills_buttons)


@dp.message_handler(text=f'Самоценка')
async def bot_data_request(message: types.Message):
    print(message.text)
    for item in get_skill_from_parsing('13'):
        await message.answer(item)
    # await message.answer('Выберете один из показателей:', reply_markup=skills_buttons)


@dp.message_handler(text=f'Материальная независимость')
async def bot_data_request(message: types.Message):
    print(message.text)
    for item in get_skill_from_parsing('14'):
        await message.answer(item)
    # await message.answer('Выберете один из показателей:', reply_markup=skills_buttons)


@dp.message_handler(text=f'Талант')
async def bot_data_request(message: types.Message):
    print(message.text)
    for item in get_skill_from_parsing('15'):
        await message.answer(item)
    # await message.answer('Выберете один из показателей:', reply_markup=skills_buttons)


@dp.message_handler(text=f'Темеперамент')
async def bot_data_request(message: types.Message):
    print(message.text)
    for item in get_skill_from_parsing('16'):
        await message.answer(item)
    # await message.answer('Выберете один из показателей:', reply_markup=skills_buttons)


@dp.message_handler(text=f'Духовность')
async def bot_data_request(message: types.Message):
    print(message.text)
    for item in get_skill_from_parsing('17'):
        await message.answer(item)
    # await message.answer('Выберете один из показателей:', reply_markup=skills_buttons)



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
    await message.answer(text)
    # await message.answer('Хотите получить данные по показателям?', reply_markup=choice_buttons)

    
    await message.answer('Выберете один из показателей:', reply_markup=aditional_numerology)




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
