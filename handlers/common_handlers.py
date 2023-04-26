from aiogram import types, Dispatcher
from aiogram.types import ContentType


async def greeting_bot(message: types.Message) -> None:
    """greeting handler"""
    await message.reply("Привет, нажми на кнопку 'Menu' и выбери что тебя интересует")


def register_handlers(disp: Dispatcher):
    """send greeting message to new chat members"""
    disp.register_message_handler(greeting_bot, commands=['start'], content_types=[ContentType.NEW_CHAT_MEMBERS])
