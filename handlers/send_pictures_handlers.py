import os
import random
from aiogram import types, Dispatcher


async def send_picture(message: types.Message) -> None:
    """send random picture to user"""
    photo = open('media/' + random.choice(os.listdir('media')), 'rb')
    await message.reply_photo(photo)


def register_handler(disp: Dispatcher) -> None:
    """registrate handlers"""
    disp.register_message_handler(send_picture, commands=['picture'])
