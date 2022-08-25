from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from keyboards.inline.callback_datas import *
from filters.emoji import *


# пишем ссылки для тех кнопок, которые перекидывают на ссылки
GIT_HUB_LINK = "https://github.com/wywdelpy"
KWORK_LINK = "https://kwork.ru/user/alex_odin"
ADMIN_LINK = "https://t.me/wywmusic"
GOOGLE_FORM_LINK = 'https://forms.gle/tvdUTDby1CVD4yno7'

# по своей структуре очень похоже на созадние обычных кнопок
# добавляем клавиатуру и передаем в нее метод inline_keyboard
# внутри которого добавляем сами кнопки с обязательным параметром text
# также внутрь передаем callback_data для созданию тригера на кнопку тк сказать
# обратите внимание на то, как меняется callback_data при первом упоминании и при втором


switch_language = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [
            InlineKeyboardButton(text=f'Русский {emoji_ruflag}', callback_data=switch_callback.new(language='russian'))
        ],
        [
            InlineKeyboardButton(text=f'English {emoji_engflag}', callback_data="switcher:english")
        ]
    ]
)

# по сути то же самое, что сверху
# однако тут обратите внимание, что еще передается url, данный параметр
# при нажатии кнопку пересылает по ссылке

media_buttons = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
        [
            InlineKeyboardButton(text=f'Git Hub {emoji_cat}', callback_data=media_callback.new(platform='git_hub'), url=GIT_HUB_LINK)
        ],
        [
            InlineKeyboardButton(text=f'Kwork {emoji_chain}', callback_data="media:kwork", url=KWORK_LINK)
        ],
        [
            InlineKeyboardButton(text=f'Задать вопрос {emoji_questionmark}', callback_data="media:answer", url=ADMIN_LINK),
            InlineKeyboardButton(text=f'Рассказать друзьям 💁‍♀️', switch_inline_query='Вот, как разрабатывают ботов!')
        ]
    ]
)

# по сути то же самое, что сверху

poll_buttons = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [
            InlineKeyboardButton(text='Google Forms', callback_data=poll_callback.new(platform='google_forms'), url=GOOGLE_FORM_LINK)
        ]
    ]
)

# на этом шаге, я думаю понятно, как создавать кнопки в этой дир-и

review_buttons = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [
            InlineKeyboardButton(text='Платформа №1', callback_data=review_callback.new(platform='platform_1'))
        ],
        [
            InlineKeyboardButton(text='Оставить отзыв', callback_data="review:write_a_review")
        ]
    ]
)


price_buttons = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
        [
            InlineKeyboardButton(text=f'Разработка Telegram ботов {emoji_robot}', callback_data=price_callback.new(type='TG_Bots'))
        ],
        [
            InlineKeyboardButton(text=f'Работа с API Google Sheets {emoji_statistics}', callback_data="price:ggsh_api")
        ]
    ]
)
