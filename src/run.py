import asyncio
from aiogram import Dispatcher, Bot

from core import config as cfg
from utils.logging import setup_logger
from handlers.start import start_router
from handlers.registration import registration_router
from handlers.room import room_router

logger = setup_logger()


async def setup_handlers(dp: Dispatcher) -> None:
    logger.info('Start setup handlers')

    routers = (
        start_router,
        registration_router,
        room_router,
    )
    for router in routers:
        dp.include_router(router)

    logger.info('End setup handlers')


async def main() -> None:
    logger.info('Init bot')
    bot = Bot(
        token=cfg.BOT_TOKEN,
    )
    dp = Dispatcher()

    await setup_handlers(dp)
    logger.info('Bot start polling')
    await dp.start_polling(bot)
    logger.info('Bot shutdown polling')


if __name__ == '__main__':
    asyncio.run(main())
