from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram import F
from dotenv import load_dotenv 
from service import *
from connection import *
import asyncio
import os

load_dotenv()

token = os.getenv("BOT_TOKEN")

bot = Bot(token=token)
dp = Dispatcher()



main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📝 Мои записи")],
        [KeyboardButton(text="🏋️ Расписание")],
        [KeyboardButton(text="🆘 Помощь")],
        [KeyboardButton(text="👤 Профиль")],
    ],
    resize_keyboard=True,
)



@dp.message(CommandStart())
async def start_bot(message: Message):
    user = message.from_user

    if not await get_user_by_id(user.id):
        await create_user(user.username, user.full_name, user.id)

    await message.answer(f"""
👋 Hello, {user.full_name}!
🤖 Welcome to Gym Class Booking!
📚 Send /help to see commands
""", reply_markup=main_kb)


@dp.message(F.text == "🆘 Помощь")
@dp.message(Command("help"))
async def help_handler(message: Message):
    await message.answer("""
💰 MY FINANCE — PERSONAL FINANCE BOT

🚀 /start - Start bot
📚 /help - Show commands
👤 /show_profile - Show my profile

""")




@dp.message(F.text == "👤 Profile")
@dp.message(Command("show_profile"))
async def show_profile(message: Message):
    user = await get_user_by_id(message.from_user.id)

    if not user:
        await message.answer("❌ User not found!")
        return

    await message.answer(f"""
👤 MY FINANCE — YOUR PROFILE

🆔 Telegram ID: {message.from_user.id}
📛 Full Name: {user['full_name']}
🔗 Username: @{user['username']}
📅 Joined: {user['created_at']}
""")




@dp.message(Command("add_class"))
async def add_class(message: Message):
    user = await get_user_by_id(message.from_user.id)

    if not user:
        await message.answer("❌ User not found!")
        return

    await message.answer(f"""

""")







async def main():
    await create_table_db()
    print("Bot started")
    await dp.start_polling(bot)
    
    
    
if __name__ == "__main__":
    asyncio.run(main())