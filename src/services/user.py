from repositories.user import UserRepository


class UserService:
    def __init__(self) -> None:
        self.user_repo = UserRepository()

    async def create_user(self, tg_id: int, name: str) -> None:
        user_dict = {
            'tg_id': tg_id,
            'name': name,
        }
        await self.user_repo.add_user(user_dict)
