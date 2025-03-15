from typing import Any

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from aiogram_dialog import StartMode

from aiogram_dialog import Window, Dialog, DialogManager

from v1.states import MySG

router = Router()


async def error(
        message: Message,
        dialog_: Any,
        manager: DialogManager,
        error_: ValueError
):
    await message.answer("Сумма должна быть числом!")


@router.message(Command("start"))
async def start(message: Message, dialog_manager: DialogManager):
    user_name = message.from_user.first_name  # Получаем имя пользователя
    # Обновляем текст окна диалога с именем пользователя
    await dialog_manager.start(MySG.select_operation_type, mode=StartMode.RESET_STACK, )  # show_mode=ShowMode.EDIT
