from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from tgbot.keyboards.inline import start_keyboard_user

user_router = Router()


# Асинхронная функция для обработки команды /start
@user_router.message(CommandStart())
async def user_start(message: Message):
    await message.answer("Hello Tigran", reply_markup=start_keyboard_user())