import logging
from typing import Any

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Select, Button

from v2.states import FinanceStates

# Настройка логгирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def on_chosen_operation_type(*args):  # c: CallbackQuery, widget: Any, button: Button, manager: DialogManager, item_id: str):  #
    # start_data - если на старте переданы какие-то данные
    print(args) # *args):  #
    # logger.info(f'Выбрана операция с item_id: {int(item_id)}')  # Логгирование выбора операции
    # ctx = manager.current_context()
    # ctx.dialog_data.update(op_type_id=int(item_id))
    # await manager.switch_to(FinanceStates.select_categories)


async def on_chosen_category(*args):  # c: CallbackQuery, widget: Any,  button: Button, manager: DialogManager, item_id: str):
    # logger.info(f'Выбрана категория с item_id: {item_id}')  # Логгирование выбора категории
    # ctx = manager.current_context()
    # ctx.dialog_data.update(category_id=item_id)
    # await manager.done()   # switch_to(FinanceStates.select_op_types)
    print(args)

