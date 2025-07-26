from core.config import Config
import httpx

async def create_payment(user_id: str, amount: int) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{Config.BIT_API_URL}/create",
            json={"user_id": user_id, "amount": amount},
            headers={"Authorization": f"Bearer {Config.BIT_API_KEY}"}
        )
        return response.json()["payment_url"]
