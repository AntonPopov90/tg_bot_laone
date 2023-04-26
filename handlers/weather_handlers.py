from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from apis.api_weather import get_weather_by_place


class WeatherState(StatesGroup):
    city = State()


async def get_weather_forecast(message: types.Message):
    """Takes name of city from user and save it to WeatherState FSM"""
    await WeatherState.city.set()
    await message.reply("В каком городе интереcует погода?")


async def get_weather_in_location(message: types.Message, state: FSMContext) -> None:
    """Depending on the user's message, run function which returns weather forecast"""
    if message.text:
        try:
            result = get_weather_by_place(message.text)
            await message.reply((f'Погода в городе {message.text}: \n'
                                 f'Температура {result["temp"]} С\n'
                                 f'Скорость ветра {result["wind"]} м/с'
                                 ))
            await state.finish()
        except Exception:
            await message.reply('Похоже вы ввели что то не то. Пожалуйста, вернитесь в меню')
            await state.finish()
    await state.finish()


def register_handler(disp: Dispatcher):
    disp.register_message_handler(get_weather_forecast, commands=['weather'], content_types=['text'])
    disp.register_message_handler(get_weather_in_location, content_types=['text'], state=WeatherState.city)
