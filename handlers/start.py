from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from dispatcher import dp
from keyboards.reply import start_keyboard
from utils.texts import Settings


@dp.message(F.text.in_({'/start', Settings.back}))
async def command_start_handler(message: Message) -> None:
    await message.answer("""
    Чем могу помочь?
1. Начать тренировку
2. Питание
3. Изменить настройки
4. Помощь
    """,
    reply_markup=start_keyboard())