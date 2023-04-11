from aiogram import types
from loader import dp


@dp.message_handler(commands=['about'])
async def bot_help(message: types.Message):
    text = ("Javohir Ergashev")
    await message.answer(text)