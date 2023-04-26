from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from apis.api_exchange import get_exchange_rate


from keyboards.exchange_keyboard import create_exchange_keyboard


class CurrencyStage(StatesGroup):
    """FSM to save bot state"""
    currency = State()
    currency_value = State()


async def exchange_access(message: types.Message) -> None:
    """Offers to choose a currency and launches the desired handler"""
    await CurrencyStage.currency.set()
    await message.reply('Выберите валюту', reply_markup=create_exchange_keyboard())


async def get_currency_name(message: types.Message, state: FSMContext) -> None:
    """save currency_value to FSM"""
    if message.text =='RUB' or message.text =='EUR' or message.text =='USD':
        await CurrencyStage.currency_value.set()
        await state.update_data(currency=message.text)
        await message.reply('Теперь введите сумму')
    else:
        await message.reply('Пожалуйста, вернитесь в меню и выберите из списка предлагаемых валют')
        await state.finish()

async def get_currency_value(message: types.Message, state: FSMContext) -> None:
    """returns dict of currency values"""
    await state.update_data(currency_value=message.text)
    data = await state.get_data()
    await state.finish()
    try:
        exchange_dict = get_exchange_rate(data)
        await message.reply(f'{exchange_dict}')
    except ValueError as e:
        await message.reply(f'похоже вы ввели не число, попробуйте заново')


def register_handler(disp: Dispatcher) -> None:
    """resistrate handlers"""
    disp.register_message_handler(exchange_access, commands=['exchange'])
    disp.register_message_handler(get_currency_name, state=CurrencyStage.currency)
    disp.register_message_handler(get_currency_value, state=CurrencyStage.currency_value)
