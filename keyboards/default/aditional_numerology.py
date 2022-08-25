from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from filters.emoji import *

aditional_numerology = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f'English {emoji_engflag}')
        ],
        [
            KeyboardButton(text=f'Русский {emoji_ruflag}')
        ]
    ],
    resize_keyboard=True
)
