from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def start_button():
    btn = ReplyKeyboardBuilder()
    btn.button(text="🗂 File")
    btn.button(text="🎵 Music")
    btn.button(text="📹 Video")
    btn.button(text="👁‍🗨 Post yaratish")
    btn.adjust(2)
    return btn.as_markup(one_time_keyboard=True, resize_keyboard=True)


file_button = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [KeyboardButton(text="🗞 File compress"),
         KeyboardButton(text="📄 PDF to PPT")],
        [KeyboardButton(text="📊 PPT to PDF"),
         KeyboardButton(text="📑 Word to PDF")],
        [KeyboardButton(text="📄 PDF to Word"),
         KeyboardButton(text="📊 PPT to Word")],
        [KeyboardButton(text="📑 Word to PPT"),
         KeyboardButton(text="🔙 Orqaga")]
    ]
)


def music_button():
    """Music bo'limi uchun tugmalar"""
    btn = ReplyKeyboardBuilder()
    btn.button(text="✂️ Music kesish")
    btn.button(text="➕ Music qo'shish")
    btn.button(text="🔙 Orqaga")
    btn.adjust(2)
    return btn.as_markup(resize_keyboard=True, one_time_keyboard=True)

def video_button():
    """Video bo'limi uchun tugmalar"""
    btn = ReplyKeyboardBuilder()
    btn.button(text="➕ Video qo'shish 🎬")
    btn.button(text="✂️ Video kesish 🎞️")
    btn.button(text="🔊 Musiqasini olish 🎵")
    btn.button(text="📉 Video siqish 📦")
    btn.button(text="🔙 Orqaga")
    btn.adjust(2)
    return btn.as_markup(resize_keyboard=True, one_time_keyboard=True)


def create_post_button():
    """Post yaratish bo'limi uchun tugmalar"""
    btn = ReplyKeyboardBuilder()
    btn.button(text="🌐 Tashqi tugma")
    btn.button(text="✍️ Ichki tugma")
    btn.button(text="🔙 Orqaga")
    btn.adjust(2)
    return btn.as_markup(resize_keyboard=True, one_time_keyboard=True)