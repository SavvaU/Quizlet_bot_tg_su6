from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="📝 Преводчик", callback_data="translate_text")],
    [InlineKeyboardButton(text="🧩 Играть", callback_data="play")],
    [InlineKeyboardButton(text="🔎 Добавить игру", callback_data="Insert")]
]
game_choose = [
    [InlineKeyboardButton(text="Русский -> English", callback_data="Rus_English")],
    [InlineKeyboardButton(text="English -> Русский", callback_data="English_Rus")],
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])