from typing import Any

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from utils.logging import setup_logger
from utils.abstract_row_keyboard import make_row_keyboard
from states.registration import RegistrationState

logger = setup_logger()
start_router = Router()


@start_router.message(Command('start'))
async def start_handler(msg: Message, state: FSMContext) -> Any:
    logger.info(f'{msg.from_user.username} started bot')

    await msg.answer(
        text=(
            f'Привет, {msg.from_user.username}!\n'
            'Это аналог настольной игры "Бункер" со всеми '
            'фишками реальной игры с полным погружением.\n\n'
            'Хочешь перейти к регистрации и начать играть?'
        ),
        reply_markup=make_row_keyboard(RegistrationState.available_start_text),
    )
    await state.set_state(RegistrationState.start)

    logger.info(f'{msg.from_user.username} has completed start handler')
    return
