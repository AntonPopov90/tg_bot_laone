import os
from pathlib import Path
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

"""get token from .env and initialize necessary aiogram classes"""

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)
API_TOKEN: str = os.getenv('TOKEN')
bot = Bot(API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
