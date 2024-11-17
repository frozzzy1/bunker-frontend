from typing import Any

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from utils.logging import setup_logger
from states.registration import RegistrationState
from services.user import UserService

logger = setup_logger()
registration_router = Router()


@registration_router.message(
    RegistrationState.start,
    F.text.in_(RegistrationState.available_start_text),
)
async def start_registration_handler(msg: Message, state: FSMContext) -> Any:
    logger.info(f'{msg.from_user.username} started registration')

    await msg.answer(
        text=(
            'Введи имя, которое будет отображаться в дальнейших играх\n\n'
            'P.S. ты сможешь изменить его в любой момент :)'
        ),
    )
    await state.set_state(RegistrationState.assignment_name)

    logger.info(f'{msg.from_user.username} has completed registration')
    return


@registration_router.message(
    RegistrationState.assignment_name,
)
async def assignment_name_handler(msg: Message, state: FSMContext) -> Any:
    user_service = UserService()
    await user_service.create_user(msg.from_user.id, msg.text)
    await msg.answer(
        text='Отлично! Теперь тебе доступны основные функции бота',
    )
    return
