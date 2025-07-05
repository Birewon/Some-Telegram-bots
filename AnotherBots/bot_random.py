import asyncio
import os
import logging

from random import choice
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

load_dotenv()
bot = Bot(os.getenv('BOT_TOKEN'))
dp = Dispatcher()

data = ['👻 The spirits say yess...',
        '🌃 The stars are whispering yes',
        '✅ Yes',
        '♾️ Maybe',
        '🔭 Is unknown',
        '⏰ Please, ask latter',
        '❌ No',
        '🤦 Of course no.',
        '🤷 Rather no, then yes']

@dp.message(Command('start', 'help'))
async def start_handler(message: Message):
    await message.answer('Hi, Im RandomBot! 👋\nYou can send me any question ✍️, and I will tell you what your chances are. 🔮')

@dp.message()
async def any_question(message: Message):
    response = choice(data)
    await message.reply(response)

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')