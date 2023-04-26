from aiogram import types
from aiogram.types import ReplyKeyboardMarkup


def create_exchange_keyboard() -> ReplyKeyboardMarkup:
    """keyboard to choose needed currency"""
    kb = [
        [types.KeyboardButton(text="RUB")],
        [types.KeyboardButton(text="EUR")],
        [types.KeyboardButton(text="USD")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, one_time_keyboard=True)
    return keyboard
