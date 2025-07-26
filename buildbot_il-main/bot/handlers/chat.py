from aiogram import types
from aiogram.dispatcher import FSMContext
from modules.chat.service import ChatService

async def handle_message(message: types.Message):
    await ChatService.process_message(
        user_id=message.from_user.id,
        text=message.text
    )
    await message.answer("Сообщение сохранено")

def register_handlers(dp):
    dp.register_message_handler(handle_message)
