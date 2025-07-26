from aiogram import types
from modules.moderation.service import ModerationService

async def cmd_ban(message: types.Message):
    if await ModerationService.check_moderator(message.from_user.id):
        await ModerationService.ban_user(message.get_args())
        await message.answer("Пользователь заблокирован")

def register_handlers(dp):
    dp.register_message_handler(cmd_ban, commands=["ban"])
