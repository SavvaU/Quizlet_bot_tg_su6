import random

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, \
    ReplyKeyboardMarkup

from models import Word

menu = [
    [InlineKeyboardButton(text="📝 Преводчик", callback_data="translate_text")],
    [InlineKeyboardButton(text="🧩 Играть", callback_data="play")],
    [InlineKeyboardButton(text="🔎 Добавить игру", callback_data="Insert")]
]
game_choose = [
    [InlineKeyboardButton(text="Русский -> English", callback_data="Rus_English")],
    [InlineKeyboardButton(text="English -> Русский", callback_data="English_Rus")],
]

game = InlineKeyboardMarkup(inline_keyboard=game_choose)
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]],
                              resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])


def get_words(word: Word, choices_words: list[Word], en_ru=True) -> InlineKeyboardMarkup:
    choices = [[InlineKeyboardButton(text=choices_word.ru_name if en_ru else choices_word.eng_name,
                                     callback_data="false")] for choices_word in choices_words]
    choices.append(
        [InlineKeyboardButton(text=word.ru_name if en_ru else word.eng_name, callback_data="true")])
    random.shuffle(choices)
    print(choices)
    return InlineKeyboardMarkup(inline_keyboard=choices)
