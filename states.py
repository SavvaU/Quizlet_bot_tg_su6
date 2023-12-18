from aiogram.fsm.state import StatesGroup, State

class Gen(StatesGroup):
    translate = State()
    img_prompt = State()
    ChoiceState = State()
    play = State()
    Rus_English = State()
    English_Rus = State()
