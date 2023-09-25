from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types.callback_query import CallbackQuery

import kb
import text

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)

@router.message(F.text == "Ссылка")
async def menu(msg: Message):
    await msg.answer(text.link)

@router.callback_query(F.data == "get_image")
async def input_text_prompt(clbck: CallbackQuery):
    await clbck.bot.send_photo(clbck.message.chat.id, text.IMG_URL, caption=text.image_text)

@router.callback_query(F.data == "get_audio")
async def input_text_prompt(clbck: CallbackQuery):
    await clbck.bot.send_audio(clbck.message.chat.id, text.AUDIO_URL, caption=text.audio_text)