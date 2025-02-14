import asyncio

from aiogram import Bot, Dispatcher

from config import TOKEN

import logging

from app.handlers import handlers
from app.handlers import handler_webenar

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(handlers.router)
    dp.include_router(handler_webenar.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
