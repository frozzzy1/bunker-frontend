from utils.fetch import fetch_post
from core.config import SERVICE_BASE_URL


class UserRepository:
    @staticmethod
    async def add_user(data: dict) -> None:
        url = f'{SERVICE_BASE_URL}/users'
        await fetch_post(url, data)
