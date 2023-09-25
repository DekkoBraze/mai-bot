from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="🖼 Изображение", callback_data="get_image"),
    InlineKeyboardButton(text="🎼 Аудио", callback_data="get_audio")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)