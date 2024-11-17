from utils.fetch import fetch_post
from core.config import SERVICE_BASE_URL


class UserRepository:
    async def add_user(self, data: dict) -> None:
        return
        url = f'{SERVICE_BASE_URL}/users'
        await fetch_post(url, data)
