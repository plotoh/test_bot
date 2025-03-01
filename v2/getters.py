import logging

from aiogram_dialog import DialogManager

from v2.states import FinanceStates
from v2 import lexicon as ru


# Настройка логгирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def get_finance_menu(dialog_manager: DialogManager, **middleware_data):
    data = {
        "op_types": [
            (title, slug)
            for slug, title in ru.finances.items()
                ]
    }
    return data


async def get_categories(dialog_manager: DialogManager, **middleware_data):
    ctx = dialog_manager.current_context()
    op_type_id = ctx.dialog_data.get('op_type_id')
    logger.info(f'Получен op_type_id: {op_type_id}')  # Логгирование op_type_id

    if not op_type_id:
        await dialog_manager.event.answer('Plz go duck yourself')
        await dialog_manager.switch_to(FinanceStates.select_op_types)
        return

    # op_type = ru.finances[op_type_id]  # Исправлено
    # logger.info(f'Получен op_type: {op_type}')  # Логгирование op_type
    # if c.data == 'expenses':
    # elif c.data == 'incomes':
    # elif c.data == 'investments':
    #
    # elif c.data == 'table':
    # elif c.data == 'settings':
    data = {
        "categories": [
            (item['id'], item['title'])
            for item in ru.expenses
                ]
    }
    return data

    print(op_type_id, op_type)