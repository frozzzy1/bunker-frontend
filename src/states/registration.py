from aiogram.fsm.state import StatesGroup, State


class RegistrationState(StatesGroup):
    start = State()
    assignment_name = State()

    available_start_text = ['Перейти к регистрации']
