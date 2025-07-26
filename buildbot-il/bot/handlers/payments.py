from aiogram import types
from modules.payments.service import create_payment

async def cmd_pay(message: types.Message):
    payment_url = await create_payment(message.from_user.id, 1000)  # 1000 BC
    await message.answer(f"Оплатите: {payment_url}")

def register_handlers(dp):
    dp.register_message_handler(cmd_pay, commands=["pay"])
