from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from environs import Env

env = Env()
env.read_env()
TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
dp = Dispatcher(storage=MemoryStorage())
