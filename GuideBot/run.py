import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from app.demonstration import router # import router from demonstration
from dotenv import load_dotenv

load_dotenv()

bot = Bot(os.getenv('BOT_TOKEN'))
dp = Dispatcher()


async def main():
    dp.include_router(router) # Add router from app.demonstration
    await dp.start_polling(bot)



if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')