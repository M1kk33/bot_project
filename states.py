from aiogram.fsm.state import StatesGroup, State

class Gen(StatesGroup):
    adding_en_meaning = State()
    adding_ru_meaning = State()
    finish_adding = State()