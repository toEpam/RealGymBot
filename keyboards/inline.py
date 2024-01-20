from itertools import chain

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.texts import Pay


def help_keyboard():
    keyboard = InlineKeyboardBuilder()
    buttons = [
        ['A', 'https://blog.gymbossbot.com/static/index/index.html'],
        ['B', 'https://t.me/gymboss_team_bot']
    ]
    keyboard.row(*[InlineKeyboardButton(text=i[0], callback_data=i[0], url=i[1]) for i in chain(buttons)], width=1)
    return keyboard.as_markup()

def payment_keyboard():
    keyboard = InlineKeyboardBuilder()
    buttons = [
        [Pay.payment, 'https://l.ptbt.site/8c3e1']
    ]
    keyboard.row(*[InlineKeyboardButton(text=i[0], callback_data=i[0], url=i[1]) for i in chain(buttons)])
    return keyboard.as_markup()