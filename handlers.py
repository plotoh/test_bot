from typing import Any

from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message

from aiogram_dialog import (
    Dialog, DialogManager, setup_dialogs, StartMode, Window, ShowMode,
)
from aiogram_dialog.widgets.input import MessageInput, TextInput
from aiogram_dialog.widgets.kbd import Button, ListGroup, Group, ScrollingGroup, Url, Next
from aiogram_dialog.widgets.text import Const, Format

from aiogram.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery

from aiogram_dialog import Window, Dialog, DialogManager
from aiogram_dialog.widgets.kbd import Button, Back
from aiogram_dialog.widgets.text import Const, Format

from states import MySG

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
