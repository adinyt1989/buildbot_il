from aiogram import Bot, Dispatcher
from core.config import Config

bot = Bot(token=Config.BOT_TOKEN)
dp = Dispatcher(bot)

from bot import register_handlers
register_handlers(dp)

async def main():
    await dp.start_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
