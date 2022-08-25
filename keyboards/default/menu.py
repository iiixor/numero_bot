from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from filters.emoji import *
# создаем кнопки
# в keyboard находится двумерный массив
# в прицнипе как матрицой можно задаавать ряды строки кнопкам
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f'Посмотреть квадрат пифагора ⚛️'),
        ],
        [
            KeyboardButton(text=f'Посмотреть гороскоп ☯️')
        ]
        # [
            # KeyboardButton(text=f'Поменять язык {emoji_ruflag}'),
            # KeyboardButton(text=f'Пройти опрос {emoji_paper_pen}'),
            # KeyboardButton(text=f'Прайс {emoji_abacus}')
        # ],
        # [
        #     KeyboardButton(text=f'Отзывы {emoji_star}'),
        #     KeyboardButton(text=f'Прайс {emoji_abacus}')
        # ],
    ],
    # делаем нормальный размер клавиатуры
    resize_keyboard=True
)
