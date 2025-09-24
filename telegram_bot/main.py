import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.handlers import router

# Bot token can be obtained via https://t.me/BotFather

TOKEN = "8426215881:AAHdIktevPaMiTcnfVaSErElKNgahob08jc"
# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # Добавить диспетчеру роутер
    dp.include_router(router)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())