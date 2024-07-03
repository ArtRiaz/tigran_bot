from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


# Keyboards


# Old user

def start_keyboard_user():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 Play",
                              web_app=WebAppInfo(url="https://tg.taptap.ac"))], [
            InlineKeyboardButton(text="👯 Community", callback_data="community")
        ],
        [InlineKeyboardButton(text="📋 Rules", callback_data="rules")]
    ]
    )
    return ikb