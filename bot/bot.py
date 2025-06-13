from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
import os
import django
from dotenv import load_dotenv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(f"Hello {message.from_user.full_name}")

def run_bot():
    dp.start_polling(bot)
