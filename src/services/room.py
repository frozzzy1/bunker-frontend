from repositories.room import RoomRepository
from exceptions.incorrect_capacity import IncorrectCapacityError


class RoomService:
    def __init__(self) -> None:
        self.room_repo = RoomRepository()

    async def create_room(self, capacity: str) -> str:
        try:
            if int(capacity) < 4:
                return IncorrectCapacityError.text
        except ValueError:
            return IncorrectCapacityError.text

        room_dict = {
            'capacity': int(capacity),
            'state': 0,
        }
        room = await self.room_repo.add_room(room_dict)
        return room['code']

    async def connect_to_room(self, code: str) -> None:
        ...