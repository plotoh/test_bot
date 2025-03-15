from typing import Any

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from aiogram_dialog import Dialog, DialogManager, setup_dialogs, StartMode, Window, ShowMode
from aiogram_dialog import Window, Dialog, DialogManager

from v2.states import FinanceStates

router: Router = Router()


@router.message(Command("start"))
async def start(message: Message, dialog_manager: DialogManager):
    user_name = message.from_user.full_name
    await dialog_manager.start(FinanceStates.select_op_type, mode=StartMode.RESET_STACK,
                               data=user_name)  # show_mode=ShowMode.EDIT


async def amount_error(
        message: Message,
        dialog_: Any,
        manager: DialogManager,
        error_: ValueError
):
    await message.answer("Сумма должна быть числом!")


async def comment_error(
        message: Message,
        dialog_: Any,
        manager: DialogManager,
        error_: ValueError
):
    await message.answer("Я не знаю что могло пойти не так, но что-то пошло не так :/")


