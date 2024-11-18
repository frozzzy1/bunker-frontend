from typing import Any

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from utils.abstract_row_keyboard import make_row_keyboard
from utils.logging import setup_logger
from states.room import RoomState
from states.menu import MenuState
from services.room import RoomService

logger = setup_logger()
room_router = Router()


@room_router.message(
    MenuState.choice_action_in_menu,
    F.text.in_(RoomState.available_create_room_text),
)
async def create_room_handler(msg: Message, state: FSMContext) -> Any:
    await msg.answer(
        text='Сколько игроков будет в комнате?',
    )
    await state.set_state(RoomState.create_room)
    return

@room_router.message(RoomState.create_room)
async def input_capacity_room_handler(msg: Message, state: FSMContext) -> Any:
    room_service = RoomService()
    answer = await room_service.create_room(msg.text)
    if len(answer) != 4:
        await msg.answer(
            text=answer,
        )
        return
    await msg.answer(
        text=('Комната создана. Подключиться к ней можно по коду:\n'
              f'{answer}'),
        reply_markup=make_row_keyboard(MenuState.available_actions_text),
    )
    await state.set_state(MenuState.choice_action_in_menu)
    return