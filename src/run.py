import asyncio
from aiogram import Dispatcher, Bot

from core import config as cfg
from handlers.registration import registration_router


async def setup_handlers(dp: Dispatcher) -> None:
    dp.include_router(registration_router)


async def main() -> None:
    bot = Bot(
        token=cfg.BOT_TOKEN,
    )
    dp = Dispatcher()

    await setup_handlers(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
