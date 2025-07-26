from aiogram import Dispatcher

def register_handlers(dp: Dispatcher):
    from bot.handlers import (
        chat, contracts, payments, 
        subscriptions, moderation
    )
    
    chat.register_handlers(dp)
    contracts.register_handlers(dp)
    payments.register_handlers(dp)
    subscriptions.register_handlers(dp)
    moderation.register_handlers(dp)
