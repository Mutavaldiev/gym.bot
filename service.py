from connection import *


async def get_user_by_id(telegram_id):
    conn = await connection_db()
    try:
        return await conn.fetchrow(
            "SELECT * FROM users WHERE telegram_id = $1",str(telegram_id))
    finally:
        await conn.close()


async def create_user(username, full_name, telegram_id):
    conn = await connection_db()

    try:
        await conn.execute("""
            INSERT INTO users (username, full_name, telegram_id)
            VALUES ($1, $2, $3)
        """, username, full_name, str(telegram_id))
    finally:
        await conn.close()



