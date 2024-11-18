from utils.fetch import fetch_post
from core.config import SERVICE_BASE_URL


class UserRepository:
    async def add_user(self, data: dict) -> None:
        return # test string
        url = f'{SERVICE_BASE_URL}/users'
        await fetch_post(url, data)
