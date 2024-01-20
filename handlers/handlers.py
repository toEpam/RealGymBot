from aiogram.types import Message
from aiogram import F

from dispatcher import dp
from keyboards.inline import *
from keyboards.reply import *
from utils.texts import Start, Settings


@dp.message(F.text == Start.help)
async def region_handler(message: Message):
    await message.answer("""
        Чтобы найти ответ на интересующий вас вопрос, загляните в мою базу знаний.
    Так же любые вопросы о моей работе вы можете задать в боте техподдержки 👇
    """,
    reply_markup=help_keyboard())


@dp.message(F.text == Start.settings)
async def region_handler(message: Message):
    await message.answer("""
        Выберите действие:
1. Настроить питание
2. Изменить свой профиль
3. Настроить подписку
4. Главное меню
5. Помощь
    """,
    reply_markup=settings_keyboard())


@dp.message(F.text == Settings.subscription)
async def region_handler(message: Message):
    await message.answer("Ваша подписка активна до 31.01.2024")
    await message.answer("""
    У меня есть несколько вариантов подписки:
+ 1 месяц за 190руб. 
+ 3 месяца за 490руб. 
+ 6 месяцев за 890руб. 
+ 1 год за 1190руб.
    """,
    reply_markup=prices_keyboard())

@dp.message(F.text.in_({Prices.one, Prices.three, Prices.six, Prices.twelve}))
async def command_start_handler(message: Message) -> None:
    await message.answer(
        """Для выбора способа оплаты перейдите по ссылке ниже 👇""",
        reply_markup=payment_keyboard()
    )



# @dp.message(F.text == Settings.back)
# async def command_start_handler(message: Message) -> None:
#     await message.answer("""
#     Чем могу помочь?
# 1. Начать тренировку
# 2. Питание
# 3. Изменить настройки
# 4. Помощь
#     """,
#     reply_markup=start_keyboard())