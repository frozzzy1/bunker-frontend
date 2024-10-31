from typing import Any

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from utils.logging import setup_logger

logger = setup_logger()
registration_router = Router()


@registration_router.message(Command('start'))
async def registration_handler(message: Message) -> Any:
    logger.info(f'{message.from_user.username} started registration')
    await message.answer('Hello user')
    logger.info(f'{message.from_user.username} has completed registration')
