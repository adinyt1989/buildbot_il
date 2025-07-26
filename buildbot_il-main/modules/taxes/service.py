from core.databases import async_session
from core.models import Order

async def calculate_tax(user_id: str) -> float:
    async with async_session() as session:
        result = await session.execute(
            select(func.sum(Order.amount))
            .where(Order.customer_id == user_id)
        )
        total = result.scalar() or 0
        return total * 0.1  # 10% налог
