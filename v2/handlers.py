from typing import Any

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from aiogram_dialog import Dialog, DialogManager, setup_dialogs, StartMode, Window, ShowMode
from aiogram_dialog import Window, Dialog, DialogManager

from v2.states import FinanceStates

router: Router = Router()


@router.message(Command("finance"))
async def start(message: Message, dialog_manager: DialogManager):
    user_name = message.from_user.full_name
    await dialog_manager.start(FinanceStates.select_op_types, mode=StartMode.RESET_STACK, data=user_name)  # show_mode=ShowMode.EDIT
