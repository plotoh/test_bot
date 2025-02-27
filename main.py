from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import (setup_dialogs)

import handlers
from windows import finance_dialog
from handlers import router

storage = MemoryStorage()
bot = Bot(token='7474830634:AAGl5h_4A5HRfD73obiIBvpySVkrwAvwnmc')
dp = Dispatcher(storage=storage)
dp.include_router(finance_dialog)
dp.include_router(handlers.router)
setup_dialogs(dp)


if __name__ == '__main__':
    (dp.run_polling(bot, skip_updates=True))