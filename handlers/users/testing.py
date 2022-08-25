from gettext import dpgettext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types


@dp.message_handler(Command('test'))
async def enter_test(message: types.Message):
    # Сюда попадает сообщение пользователю, что он начал тестирование
    await message.answer('Вы начали тестирование!. \n')

    # Тут находится то, что отвечает бот
    await Test.Q1.set()
    # await Test.first()

    @dp.message_handler(state=Test.Q1)
    async def answer_q1(message: types.Message, state: FSMContext):
         # Присвоение состояния ответа на первый вопрос
         answer = message.text
         
         await state.update_data(answer1=answer)
         await message.answer('Вопрос n2. \n \n')
         await Test.next()

    @dp.message_handler(state=Test.Q2)
    async def answer_q2(message: Types.Message, state: FSMContext):
        # Присвоение состояния ответа на второй вопрос
        data = await state.get_data()
        answer1 = data.get('answer1')
        answer2 = message.text

        await message.answer('Спасибо за ваши ответы!')
        await message.answer(f'Ответ 1: {answer1}')
        await message.answer(f'Ответ 2: {answer2}')
        # тут находятся ответы
        await state.finish()
        # сброс состояния
