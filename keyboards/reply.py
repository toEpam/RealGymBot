from itertools import chain

from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from utils.texts import Start, Settings, Prices


def start_keyboard():
    keyboard = ReplyKeyboardBuilder()
    buttons = [
        [Start.training, Start.nutrition],
        [Start.settings, Start.help]
    ]
    keyboard.row(*[KeyboardButton(text=i) for i in chain(*buttons)], width=2)
    return keyboard.as_markup(resize_keyboard=True)


def settings_keyboard():
    keyboard = ReplyKeyboardBuilder()
    buttons = [
        [Settings.nutrition, ''],
        [Settings.profile, Settings.subscription],
        [Settings.back, Settings.help]
    ]
    keyboard.row(*[KeyboardButton(text=i) for i in chain(*buttons)], width=2)
    return keyboard.as_markup(resize_keyboard=True)


def prices_keyboard():
    keyboard = ReplyKeyboardBuilder()
    buttons = [
        [Prices.one, Prices.three, Prices.six],
        [Prices.twelve, '', ''],
        [Settings.back]
    ]
    keyboard.row(*[KeyboardButton(text=i) for i in chain(*buttons)], width=3)
    return keyboard.as_markup(resize_keyboard=True)