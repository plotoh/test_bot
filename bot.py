import os

import dotenv
from aiogram_dialog import setup_dialogs
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram_dialog import (setup_dialogs)

# from v1 import handlers
# from v1.windows import finance_dialog
from v2 import handlers  # , setup_dialogs
from v2.windows import finance_dialog


dotenv.load_dotenv()
storage = MemoryStorage()
bot = Bot(token=os.getenv('BOT_TOKN'))
dp = Dispatcher(storage=storage)
dp.include_router(finance_dialog)
dp.include_router(handlers.router)
setup_dialogs(dp)

if __name__ == '__main__':
    (dp.run_polling(bot, skip_updates=True))
