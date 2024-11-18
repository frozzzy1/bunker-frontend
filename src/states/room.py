from aiogram.fsm.state import StatesGroup, State


class RoomState(StatesGroup):
    create_room = State()
    connect_to_room = State()
    start_room = State()

    available_create_room_text = ['Создать комнату']
    available_connect_to_room_text = ['Подключиться к комнате']
    available_choice_room_text = ['Создать комнату', 'Подключиться к комнате']
