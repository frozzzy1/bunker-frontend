from typing import Any

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


registration_router = Router()


@registration_router.message(Command('start'))
async def registration_handler(message: Message) -> Any:
    await message.answer('Hello user')
