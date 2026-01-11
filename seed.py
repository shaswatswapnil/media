
import asyncio
from core.db import get_db
from models.admins import Admin
from core.security import get_password_hash

async def main():
    db = await anext(get_db())
    admin = Admin(
        name="shaswat",
        email="shaswat785@gmail.com",
        password_hash=get_password_hash("311001"),
    )
    db.add(admin)
    await db.commit()

if __name__ == "__main__":
    asyncio.run(main())
