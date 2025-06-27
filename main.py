import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def on_start(message: Message):
    await message.answer("Привет! Бот работает на Python 3.13.4 и Aiogram 3.5.0")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
