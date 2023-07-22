from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import *


async def start_btn():
    btn = InlineKeyboardMarkup(row_width=1)
    btn.add(
        InlineKeyboardButton('KIBER XAVFSIZLIK ✅', url="https://t.me/KiberxavfsizlikBot")
    )
    
    return btn

async def start_btn1():
    btn = InlineKeyboardMarkup(row_width=1)
    btn.add(
        InlineKeyboardButton("✅ A'zo bo'lish", url="https://t.me/shk_uz"),
        InlineKeyboardButton('✅ Tekshirish', callback_data='check')
    )
    
    return btn


async def reply_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.row("Foydali loyihalar ✅")
    btn.add(
        KeyboardButton("Boshlang'ich tushuncha"),
        KeyboardButton("Video darslar"),
        KeyboardButton("💡 G'oya/idea"),
        KeyboardButton("Android uchun montaj dastur"),
        KeyboardButton("Master class"),
        KeyboardButton("Intervyu"),
        KeyboardButton("Videomontaj uchun musiqa"),
        KeyboardButton("After effect darsi"),
        KeyboardButton("Vakansiyalar"),
        KeyboardButton("Trenddagi musiqalar"),
    )
    btn.row("🗯️ Fikr bildirish")

    return btn


async def video_lessons():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.add(
        KeyboardButton("📲 Nazariy"),
        KeyboardButton("💎Amaliy"),
        KeyboardButton("🔙 Orqaga"),
        KeyboardButton("🔝 Asosiy Menyu"),
    )

    return btn


async def idea():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.row("🚗 Avtomobil uchun💡")
    btn.row("🖼️ 🌎Landshaft uchun💡")
    btn.add(
        KeyboardButton("🔙 Orqaga"),
        KeyboardButton("🔝 Asosiy Menyu"),
    )

    return btn


# async def ():
#     btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     btn.add(
#         KeyboardButton(""),
#         KeyboardButton(""),
#         KeyboardButton(""),
#         KeyboardButton(""),
#     )

#     return btn


async def android():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.add(
        KeyboardButton("CapCut"),
        KeyboardButton("VN"),
    )

    btn.row("Inshot")

    btn.add(
        KeyboardButton("🔙 Orqaga"),
        KeyboardButton("🔝 Asosiy Menyu"),
    )

    return btn


async def master_class():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.row("🔝 TOP 5")
    btn.add(
        KeyboardButton("🔝 TOP 6 -> 8"),
        KeyboardButton("🔝 TOP 8 -> 10"),
        KeyboardButton("🔙 Orqaga"),
        KeyboardButton("🔝 Asosiy Menyu"),
    )

    return btn


async def interview():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.add(
        KeyboardButton("1️⃣"),
        KeyboardButton("2️⃣"),
        KeyboardButton("3️⃣"),
        KeyboardButton("4️⃣"),
        KeyboardButton("5️⃣"),
        KeyboardButton("6️⃣"),
        KeyboardButton("🔙 Orqaga"),
        KeyboardButton("🔝 Asosiy Menyu"),
    )

    return btn


async def videomontaj():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.row("Tasodifiy musiqa 🔀")
    btn.row("🔥Musiqalar jamlanmasi")
    btn.add(
        KeyboardButton("🔙 Orqaga"),
        KeyboardButton("🔝 Asosiy Menyu"),
    )

    return btn


async def vacanse():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.add(
        KeyboardButton("Ish qidirish"),
        KeyboardButton("Vakansiya qo'shish"),
        KeyboardButton("🔙 Orqaga"),
        KeyboardButton("🔝 Asosiy Menyu"),
    )

    return btn


async def trend_musics():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.add(
        KeyboardButton("1-musiqa"),
        KeyboardButton("2-musiqa"),
        KeyboardButton("3-musiqa"),
        KeyboardButton("4-musiqa"),
        KeyboardButton("5-musiqa"),
        KeyboardButton("6-musiqa"),
        KeyboardButton("7-musiqa"),
        KeyboardButton("8-musiqa"),
        KeyboardButton("9-musiqa"),
        KeyboardButton("10-musiqa"),
        KeyboardButton("11-musiqa"),
        KeyboardButton("12-musiqa"),
        KeyboardButton("13-musiqa"),
        KeyboardButton("14-musiqa"),
        KeyboardButton("15-musiqa"),
        KeyboardButton("16-musiqa"),
        KeyboardButton("17-musiqa"),
        KeyboardButton("18-musiqa"),
        KeyboardButton("19-musiqa"),
        KeyboardButton("20-musiqa"),
        KeyboardButton("21-musiqa"),
        KeyboardButton("22-musiqa"),
        KeyboardButton("23-musiqa"),
        KeyboardButton("24-musiqa"),
        KeyboardButton("🔙 Orqaga"),
        KeyboardButton("🔝 Asosiy Menyu"),
    )

    return btn


async def fikr_bildirish():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row("🚫 Bekor qilish")
