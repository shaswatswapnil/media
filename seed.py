
import asyncio
from core.db import get_db
from models.admins import Admin
from core.security import get_password_hash

async def main():
    db = await anext(get_db())
    admin = Admin(
        name="Admin",
        email="admin@example.com",
        password_hash=get_password_hash("password"),
    )
    db.add(admin)
    await db.commit()

if __name__ == "__main__":
    asyncio.run(main())
