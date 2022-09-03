from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from filters.emoji import *
# создаем кнопки
# в keyboard находится двумерный массив
# в прицнипе как матрицой можно задаавать ряды строки кнопкам
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f'Личный кабинет 👤')
        ],
        [
            KeyboardButton(text=f'Посмотреть гороскоп ☯️')
        ],
        [
            KeyboardButton(text=f'Посмотреть квадрат пифагора ⚛️')
        ]
    ],
    # делаем нормальный размер клавиатуры
    resize_keyboard=True
)
