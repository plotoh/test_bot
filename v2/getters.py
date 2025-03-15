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
    logger.info(f'Получен op_type_id: {ru.finances[op_type_id]}')  # Логирование op_type_id

    if op_type_id == 'expenses':
        category = ru.expenses  # category = ru.expenses.items()
    elif op_type_id == 'incomes':
        category = ru.incomes
    elif op_type_id == 'investments':
        category = ru.investments

    data = {
        'op_type': ru.finances[op_type_id],
        "categories": [
            (item['id'], item['title'])
            for item in category
        ]
    }
    return data


async def get_op_frequency(dialog_manager: DialogManager, **middleware_data):
    data = {
        "frequency": [
            (title, slug)
            for slug, title in ru.regular.items()
        ],
    }
    return data


async def get_executed_operation(dialog_manager: DialogManager, **middleware_data):
    ctx = dialog_manager.current_context().dialog_data
    op_type = ru.finances[ctx.get('op_type_id')]
    category = ctx.get('category')
    amount = ctx.get('amount')
    date = ctx.get('date')
    comment = ctx.get('comment')
    logger.info(f'Получены: {op_type, category, amount, comment, date}')

    return {
        'op_type': op_type,
        'category': category,
        'amount': amount,
        'date': date,
        'comment': comment,
        'options': [(title, slug) for slug, title in ru.edit_op_menu.items()],
    }
