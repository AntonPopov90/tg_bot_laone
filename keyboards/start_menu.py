from aiogram import types
from create_bot import dp


async def set_default_commands(disp: dp) -> None:
    """ Menu button with different choices"""
    await disp.bot.set_my_commands(
        [
            types.BotCommand("weather", "Узнать погоду"),
            types.BotCommand("exchange", "Конвертер валют"),
            types.BotCommand("picture", "Прислать картинку"),
            types.BotCommand("pollz", "Создать опрос")
        ]
    )
