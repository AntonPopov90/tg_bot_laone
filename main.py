from aiogram import executor
from aiogram.utils.exceptions import NetworkError
from create_bot import dp
from handlers import exchange_handlers, weather_handlers, common_handlers, send_pictures_handlers, pollz_handlers
from keyboards.start_menu import set_default_commands  # main menu keyboard

"""register handlers from handlers package"""
exchange_handlers.register_handler(dp)
weather_handlers.register_handler(dp)
common_handlers.register_handlers(dp)
send_pictures_handlers.register_handler(dp)
pollz_handlers.register_handler(dp)

"""starting bot"""
try:
    if __name__ == '__main__':
        executor.start_polling(dp, skip_updates=True, on_startup=set_default_commands)
except NetworkError as error:
    print('Похоже вы не подключены к сети интернет, проверьте соединение')
