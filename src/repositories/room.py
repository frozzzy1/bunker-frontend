from utils.fetch import fetch_post
from core.config import SERVICE_BASE_URL


class RoomRepository:
    async def add_room(self, data: dict) -> None:
        return {'code': 'bqju'} # test string
        url = f'{SERVICE_BASE_URL}/rooms'
        return await fetch_post(url, data)
