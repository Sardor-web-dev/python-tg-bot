import sys
from os import getenv
from dotenv import load_dotenv

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

load_dotenv()
TOKEN = getenv("BOT_TOKEN") or ""

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer("Привет бот это бот R")

async def main():
    bot = Bot(token = TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        stream=sys.stdout,
        format = "%(asctime)s - %(levelname)s - %(message)s",
        datefmt = "%Y-%M-%D %H:%M:%S"
    )
    logging.debug("сообщение типа инфо")
    print("Обычное сообщение")
    asyncio.run(main())

