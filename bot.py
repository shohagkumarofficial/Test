import asyncio
import os
import platform
import socket
import time

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise SystemExit("BOT_TOKEN সেট করা নেই! .env ফাইলে বা environment এ দাও।")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
START_TIME = time.time()


def uptime() -> str:
    s = int(time.time() - START_TIME)
    h, s = divmod(s, 3600)
    m, s = divmod(s, 60)
    return f"{h}h {m}m {s}s"


@dp.message(Command("start"))
async def start(msg: types.Message):
    await msg.answer("✅ Test VPS Bot চালু আছে!\n/ping /status /id")


@dp.message(Command("ping"))
async def ping(msg: types.Message):
    await msg.answer("🏓 pong!")


@dp.message(Command("status"))
async def status(msg: types.Message):
    await msg.answer(
        f"🖥 VPS Status\n"
        f"Host: {socket.gethostname()}\n"
        f"OS: {platform.system()} {platform.release()}\n"
        f"Python: {platform.python_version()}\n"
        f"Uptime: {uptime()}"
    )


@dp.message(Command("id"))
async def my_id(msg: types.Message):
    await msg.answer(f"Your ID: {msg.from_user.id}")


async def main():
    print("Bot started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
