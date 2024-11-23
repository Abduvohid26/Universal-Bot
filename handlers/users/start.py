from aiogram.filters import CommandStart
from loader import dp
from aiogram import types, html, F
from keyboards.default.buttons import start_button, file_button, music_button, video_button, \
create_post_button


@dp.message(CommandStart())
async def start_bot(message:types.Message):
    greeting_text = (
        f"👋 Assalomu alaykum, {html.link(value=message.from_user.full_name, link=f'tg://user?id={message.from_user.id}')}\n\n"
        "🤖 Men sizga fayllar, musiqa va videolar bilan ishlash, "
        "yoki postlar yaratishda yordam beradigan botman.\n\n"
        "🎯 Quyidagi tugmalardan birini tanlang yoki o'zingizga kerakli xizmatni boshlang!"
    )
    await message.answer(text=html.bold(greeting_text), reply_markup=start_button())


@dp.message(F.text == '🗂 File')
async def file_start(message: types.Message):
    text = "🎛 Kerakli Bo'limni tanlang"
    await message.answer(text=text, reply_markup=file_button)



@dp.message(F.text == '🎵 Music')
async def music_start(message: types.Message):
    text = "🎛 Kerakli Bo'limni tanlang"
    await message.answer(text=text, reply_markup=music_button())


@dp.message(F.text == '📹 Video')
async def music_start(message: types.Message):
    text = "🎛 Kerakli Bo'limni tanlang"
    await message.answer(text=text, reply_markup=video_button())


@dp.message(F.text == '👁‍🗨 Post yaratish')
async def music_start(message: types.Message):
    text = "🎛 Kerakli Bo'limni tanlang"
    await message.answer(text=text, reply_markup=create_post_button())

@dp.message(F.text == '🔙 Orqaga')
async def back_handler(message: types.Message):
    text = "🎛 Kerakli Bo'limni tanlang"
    await message.answer(text=text, reply_markup=start_button())