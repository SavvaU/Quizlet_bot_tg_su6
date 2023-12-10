from aiogram.fsm.state import StatesGroup, State

class Gen(StatesGroup):
    translate = State()
    img_prompt = State()