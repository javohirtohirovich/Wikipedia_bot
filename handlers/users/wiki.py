from aiogram import types
import wikipedia
from loader import dp

wikipedia.set_lang('uz')

@dp.message_handler(state=None)
async def echo(message: types.Message):
    try:
        resend=wikipedia.summary(message.text)
        await message.answer(resend)
    except:
        await message.answer("Bu mavzuga oid ma'lumot topilmadi".upper())
