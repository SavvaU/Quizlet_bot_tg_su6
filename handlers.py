from aiogram import F, Router, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from sqlalchemy import select, func

import kb
import text
from db import db
from models import Word
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
                           reply_markup=kb.game)


@router.callback_query(F.data == "Rus_English")
async def game_1(query: CallbackQuery, state: FSMContext, bot: Bot):
    await state.set_state(Gen.Rus_English)
    word = db.sql_query(query=select(Word).limit(1).order_by(func.random()))
    words = db.sql_query(
        query=select(Word).limit(3).order_by(func.random()).where(Word.id != word.id), single=False)
    keyboard = kb.get_words(word=word, choices_words=words, en_ru=False)
    await bot.send_message(chat_id=query.from_user.id, text=word.ru_name, reply_markup=keyboard)


@router.callback_query(F.data == "English_Rus")
async def game_1(query: CallbackQuery, state: FSMContext, bot: Bot):
    await state.set_state(Gen.English_Rus)
    word = db.sql_query(query=select(Word).limit(1).order_by(func.random()))
    words = db.sql_query(
        query=select(Word).limit(3).order_by(func.random()).where(Word.id != word.id), single=False)
    keyboard = kb.get_words(word=word, choices_words=words, en_ru=True)
    await bot.send_message(chat_id=query.from_user.id, text=word.eng_name, reply_markup=keyboard)


@router.callback_query(Gen.Rus_English, F.data == "true")
async def game_1(query: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(chat_id=query.from_user.id, text="Ты ответил верно!")
    word = db.sql_query(query=select(Word).limit(1).order_by(func.random()))
    words = db.sql_query(
        query=select(Word).limit(3).order_by(func.random()).where(Word.id != word.id), single=False)
    keyboard = kb.get_words(word=word, choices_words=words, en_ru=False)
    await bot.send_message(chat_id=query.from_user.id, text=word.ru_name, reply_markup=keyboard)


@router.callback_query(Gen.Rus_English, F.data == "false")
async def game_1(query: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(chat_id=query.from_user.id, text="Ты ответил неверно!")
    word = db.sql_query(query=select(Word).limit(1).order_by(func.random()))
    words = db.sql_query(
        query=select(Word).limit(3).order_by(func.random()).where(Word.id != word.id), single=False)
    keyboard = kb.get_words(word=word, choices_words=words, en_ru=False)
    await bot.send_message(chat_id=query.from_user.id, text=word.ru_name, reply_markup=keyboard)


@router.callback_query(Gen.English_Rus, F.data == "true")
async def game_1(query: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(chat_id=query.from_user.id, text="Ты ответил верно!")
    word = db.sql_query(query=select(Word).limit(1).order_by(func.random()))
    words = db.sql_query(
        query=select(Word).limit(3).order_by(func.random()).where(Word.id != word.id), single=False)
    keyboard = kb.get_words(word=word, choices_words=words, en_ru=True)
    await bot.send_message(chat_id=query.from_user.id, text=word.eng_name, reply_markup=keyboard)


@router.callback_query(Gen.English_Rus, F.data == "false")
async def game_1(query: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(chat_id=query.from_user.id, text="Ты ответил неверно!")
    word = db.sql_query(query=select(Word).limit(1).order_by(func.random()))
    words = db.sql_query(
        query=select(Word).limit(3).order_by(func.random()).where(Word.id != word.id), single=False)
    keyboard = kb.get_words(word=word, choices_words=words, en_ru=True)
    await bot.send_message(chat_id=query.from_user.id, text=word.eng_name, reply_markup=keyboard)
