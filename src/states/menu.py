from aiogram.fsm.state import StatesGroup, State


class MenuState(StatesGroup):
    choice_action_in_menu = State()

    available_actions_text = ['Создать комнату', 'Подключиться к комнате', 'Настройки']
