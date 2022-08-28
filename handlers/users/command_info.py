from aiogram import types
from loader import dp, bot
import aiogram.utils.markdown as fmt

@dp.message_handler(commands=['info'])
async def information(message: types.Message):
    text = [
        'В данном телеграм боте Вы сможете узнать:',
        '<i>- Нумерологическую психоматрицу</i>',
        '<i>- Ежедневный гороскоп по каждому знаку зодиака</i>',    
    ]
    await message.answer('\n'.join(text))    