from loader import dp
from aiogram import types,F, html
@dp.message(F.text)
async def echo_bot(message:types.Message):
    greeting_text = (
        f"👋 Assalomu alaykum, {html.link(value=message.from_user.full_name, link=f'tg://user?id={message.from_user.id}')}\n\n"
        "🤖 Men sizga fayllar, musiqa va videolar bilan ishlash, "
        "yoki postlar yaratishda yordam beradigan botman.\n\n"
        "🎯 Quyidagi tugmalardan birini tanlang yoki o'zingizga kerakli xizmatni boshlang!"
    )
    await message.answer(greeting_text)
