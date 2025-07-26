import httpx
from core.config import Config

async def export_to_1c():
    async with httpx.AsyncClient() as client:
        await client.post(
            f"{Config.API_1C_URL}/import",
            headers={"Authorization": Config.API_1C_KEY}
        )
