from aiogram import types
from loader import dp, bot
import aiogram.utils.markdown as fmt

@dp.message_handler(commands=['info'])
async def information(message: types.Message):
    text = [
        'Данный телеграм бот был создан командой @Delpy_Bot, чтобы любой пользователь мог с лёгкостью узнать:\n',
        '<i>- Нумерологическую психоматрицу</i>',
        '<i>- Ежедневный гороскоп по каждому знаку зодиака</i>\n',    
        'В данном боте Вы можете бесплато дважды в сутки узнать гороскоп по каждому знаку зодиака и дважды просмотреть нумерологическую психоматрицу'
    ]
    await message.answer('\n'.join(text))    