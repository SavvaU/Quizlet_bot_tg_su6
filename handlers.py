from aiogram import F, Router, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

import kb
import text
from states import Gen
from utils import translate_text

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


@router.callback_query(F.data == "play")
async def game_1(query: CallbackQuery, state: FSMContext, bot: Bot):
    await state.set_state(Gen.play)
    await bot.send_message(chat_id=query.from_user.id, text=text.Game_rules,
                           reply_markup=kb.game_choose)


@router.callback_query(F.data == "Rus_English")
async def game_1(query: CallbackQuery, state: FSMContext, bot: Bot):
    await state.set_state(Gen.Rus_English)
    await bot.send_message(chat_id=query.from_user.id, text="Первое слово игры")


@router.callback_query(F.data == "English_Rus")
async def game_1(query: CallbackQuery, state: FSMContext, bot: Bot):
    await state.set_state(Gen.English_Rus)
    await bot.send_message(chat_id=query.from_user.id, text="Первое слово игры")
