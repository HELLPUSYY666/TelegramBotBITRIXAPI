from app.database.models import async_session
from app.database.models import User, Products, Webinars, UserAction, WebinarRegistration
from sqlalchemy import select, update, delete


async def save_user_data(user_data: dict, tg_id: int) -> User:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            user = User(
                tg_id=tg_id,
                full_name=user_data['full_name'],
                phone=user_data['phone'],
                email=user_data['email'],
                region=user_data['region'],
                specialty=user_data['specialty']
            )
            session.add(user)
            await session.commit()
        else:
            user.full_name = user_data['full_name']
            user.phone = user_data['phone']
            user.email = user_data['email']
            user.region = user_data['region']
            user.specialty = user_data['specialty']
            await session.commit()

        return user
