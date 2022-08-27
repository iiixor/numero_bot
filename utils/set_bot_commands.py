from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand('menu', 'Перейти в главное меню'),
        types.BotCommand('info', 'Получить информацию о боте')
    ])
