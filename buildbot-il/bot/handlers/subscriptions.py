from aiogram import types
from modules.subscriptions.service import SubscriptionService

async def cmd_subscribe(message: types.Message):
    await SubscriptionService.activate_trial(message.from_user.id)
    await message.answer("Пробный период активирован!")

def register_handlers(dp):
    dp.register_message_handler(cmd_subscribe, commands=["subscribe"])
