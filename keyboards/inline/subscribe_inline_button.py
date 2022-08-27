from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from keyboards.inline.callback_datas import *
from filters.emoji import *

subscribe_button = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [
            InlineKeyboardButton(text=f'Оформить подписку', callback_data=subscribe_callback.new(type='yes'))
        ]
    ]
)
