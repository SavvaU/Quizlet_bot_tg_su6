from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message

from aiogram import flags
from aiogram.fsm.context import FSMContext
import utils
from states import Gen
from utils import translate_text

import kb
import text

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)


@router.message(F.text == "Меню" or F.text == "Выйти в меню" or F.text == "меню")
async def menu(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer(text.menu, reply_markup=kb.menu)


@router.callback_query(F.data == "translate_text")
async def translate_1(msg: Message, state: FSMContext):
    await state.set_state(Gen.translate)


@router.message(Gen.translate)
async def translate_2(msg: Message, state: FSMContext):
    await msg.answer(translate_text(msg.text))


