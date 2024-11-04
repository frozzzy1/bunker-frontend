from repositories.user import UserRepository


class UserService:
    @staticmethod
    async def create_user(tg_id: int, name: str) -> None:
        user_dict = {
            'tg_id': tg_id,
            'name': name,
        }
        await UserRepository.add_user(user_dict)
