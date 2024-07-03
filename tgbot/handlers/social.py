from aiogram import Router, F, types
from aiogram.types.callback_query import CallbackQuery

social_router = Router()


# CMD Social

@social_router.callback_query(F.data == "community")
async def community(query: CallbackQuery):
    await query.message.answer("Hello")
    await query.answer()


# CMD Rules
@social_router.callback_query(F.data == "rules")
async def rules(query: CallbackQuery):
    await query.message.answer("📋 Rules of the game\n\n"
                               f"🎮 Play\n\n"
                               f"Tap the screen, make me purrr, "
                               f"and get rewards.\n\n"
                               f"💸 Gain\n\n"
                               f"Get rewards for your actions and "
                               f"achievements.\n\n"
                               f"🚀 Boost\n\n"
                               f"Skyrocket your rewards with "
                               f"boosts.\n\n"
                               f"💌 Invite\n\n"
                               f"Invite friends and get rewards.\n\n"
                               f"🎁 Gifts\n\n"
                               f"Get gifts for your achievements.")
    await query.answer()