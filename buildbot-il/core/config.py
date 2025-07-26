import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Telegram
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    MODERATOR_BOT_TOKEN = os.getenv("MODERATOR_BOT_TOKEN")

    # Database
    DATABASE_URL = os.getenv("DATABASE_URL")
    REDIS_URL = os.getenv("REDIS_URL")

    # Payments
    BIT_API_KEY = os.getenv("BIT_API_KEY")
    BIT_API_URL = os.getenv("BIT_API_URL")

    # 1C
    API_1C_URL = os.getenv("API_1C_URL")
    API_1C_KEY = os.getenv("API_1C_KEY")

    # S3
    AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET")
    AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
    AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

    # Currency
    BC_RATE = 1.0  # 1 BC = 1 ₪
