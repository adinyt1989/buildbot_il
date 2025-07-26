from datetime import datetime, timedelta
from core.databases import async_session
from core.models import User

async def activate_trial(user_id: str):
    async with async_session() as session:
        user = await session.get(User, user_id)
        user.trial_expires = datetime.now() + timedelta(days=7)
        await session.commit()
