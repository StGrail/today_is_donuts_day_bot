import asyncio
import datetime
import random

from aiogram import types
from aiogram.utils.exceptions import BotKicked, ChatNotFound

from constants import stickers
from main import dp, bot
from settings import GROUP_CHAT_ID, CHAT_ID


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer('🍩 Привет, все мы любим пончики 🍩')


@dp.message_handler(commands=['kill_it'])
async def send_welcome(message: types.Message):
    await message.answer('🍩 Привет, все мы любим пончики. Но меня убили 🍩')
    raise SystemExit


@dp.message_handler(commands=['welcome_message'])
async def send_welcome_message(message: types.Message):
    try:
        await bot.send_message(
            chat_id=GROUP_CHAT_ID, text='🍩 Привет, я буду напоминать вам о пончиках в четверг 🍩'
        )
    except BotKicked:
        await bot.send_message(
            chat_id=CHAT_ID,
            text=f'Попытка отправить сообщение в чат с id: {GROUP_CHAT_ID}, но я был оттуда кикнут :(',
        )
    except ChatNotFound:
        await bot.send_message(
            chat_id=CHAT_ID,
            text=f'Попытка отправить сообщение в чат с id: {GROUP_CHAT_ID}, нет такого чата :(',
        )


@dp.message_handler(
    lambda message: message.text and '@today_is_donuts_day_bot' in message.text.lower()
)
async def echo_with_sticker(message: types.Message):
    await message.answer_sticker(sticker=random.choice(stickers.DONUTS), disable_notification=True)


async def today_is_donuts_day():  # Не стал заморачиваться с выносом в отдельный файл
    while True:
        if (
            datetime.datetime.today().weekday() == 3
            and datetime.datetime.now().strftime("%H:%M") == '10:30'
        ):
            await bot.send_message(chat_id=GROUP_CHAT_ID, text='🍩 Сегодня день пончиков! 🍩')
        await asyncio.sleep(60)
