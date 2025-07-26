from aiogram import types
from modules.contracts.service import generate_contract

async def cmd_contract(message: types.Message):
    pdf = await generate_contract(message.from_user.id)
    await message.answer_document(
        document=pdf,
        caption="Ваш договор"
    )

def register_handlers(dp):
    dp.register_message_handler(cmd_contract, commands=["contract"])
