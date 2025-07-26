from apscheduler.schedulers.asyncio import AsyncIOScheduler
from modules.subscriptions.service import check_expired_subscriptions

scheduler = AsyncIOScheduler()
scheduler.add_job(check_expired_subscriptions, "interval", hours=24)
scheduler.start()
