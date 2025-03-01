from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import (setup_dialogs)

# from v1 import handlers
# from v1.windows import finance_dialog
from v2 import handlers
from v2.windows import finance_dialog

storage = MemoryStorage()
load_dotenv()
bot_token = '7474830634:AAGl5h_4A5HRfD73obiIBvpySVkrwAvwnmc'
bot = Bot(token=bot_token)
dp = Dispatcher(storage=storage)
dp.include_router(finance_dialog)
dp.include_router(handlers.router)
setup_dialogs(dp)

if __name__ == '__main__':
    (dp.run_polling(bot, skip_updates=True))
