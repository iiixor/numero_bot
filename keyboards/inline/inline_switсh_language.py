from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from keyboards.inline.callback_datas import *
from filters.emoji import *

ADMIN_LINK = "https://t.me/wywmusic"

skills_buttons = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(text=f'Характер', callback_data=skills_callback.new(type='character')),
        InlineKeyboardButton(text=f'Энергия', callback_data='skill:energy')
    ],
    [
        InlineKeyboardButton(text=f'Интерес', callback_data='skill:interest'),
        InlineKeyboardButton(text=f'Здоровье', callback_data='skill:health')
    ],
    [
        InlineKeyboardButton(text=f'Логика, Интуиация', callback_data='skill:logic'),
        InlineKeyboardButton(text=f'Труд', callback_data='skill:labour')
    ],
    [
        InlineKeyboardButton(text=f'Удача', callback_data='skill:luck'),
        InlineKeyboardButton(text=f'Чувство долга', callback_data='skill:duty')
    ],
    [
        InlineKeyboardButton(text=f'Память', callback_data='skill:memory'),
        InlineKeyboardButton(text=f'Целеустрмленность', callback_data='skill:сommitment')
    ],
    [
        InlineKeyboardButton(text=f'Семья', callback_data='skill:family'),
        InlineKeyboardButton(text=f'Стабильность', callback_data='skill:stability')
    ],
    [
        InlineKeyboardButton(text=f'Самоценка', callback_data='skill:self_esteem'),
        InlineKeyboardButton(text=f'Материальная независимость', callback_data='skill:material_independence')
    ],
    [
        InlineKeyboardButton(text=f'Талант', callback_data='skill:talant'),
        InlineKeyboardButton(text=f'Темперамент', callback_data='skill:tempepament')
    ],
    [
        InlineKeyboardButton(text=f'Духовность', callback_data='skill:spirit'),
    ],

    ]
)
