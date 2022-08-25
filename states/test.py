from aiogram.dispatcher.filters.state import StatesGroup, State


# машина состояний
class Test(StatesGroup):
    Q1 = State()
    Q2 = State()
