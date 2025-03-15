import logging
from datetime import datetime, date
from typing import Any

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Select, Button

from v2.states import FinanceStates
from v2 import lexicon as ru

# Настройка логгирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def on_chosen_operation_type(c: CallbackQuery, widget: Select, manager: DialogManager, item_id: str,
                                   **kwargs):  # button: Button,
    # start_data - если на старте переданы какие-то данные
    # print(*args, sep='\n\n')  # *args):  #
    # callback, widget, manager, item_id = [x for x in args]  # button,
    # logger.info(f'Выбрана операция с item_id: {args[0]}')  # Логгирование выбора операции
    # ctx = manager.current_context()
    # ctx.dialog_data.update(op_type_id=item)
    # await manager.switch_to(FinanceStates.select_categories)
    # logger.info(f'{c.data, widget, manager, item_id, kwargs}') #  c.data
    logger.info(f'Выбран тип item_id: {item_id}')  # Логгирование выбора операции
    ctx = manager.current_context()

    if item_id in ['expenses', 'incomes', 'investments']:
        ctx.dialog_data.update(op_type_id=item_id)
        await manager.switch_to(state=FinanceStates.select_category)

#     if item_id == 'table':
#         await manager.switch_to(state=FinanceStates.table)
#     elif item_id == 'settings':
#         await manager.switch_to(state=FinanceStates.settings)
#
#
# async def back_to_select_op_type(callback: CallbackQuery, button: Button, manager: DialogManager):
#     await manager.switch_to(state=FinanceStates.select_op_type)


async def on_chosen_category(c: CallbackQuery, widget: Select, manager: DialogManager, item_id: str):  # button: Button,
    ctx = manager.current_context()
    op_type = ru.finances[ctx.dialog_data.get('op_type_id')]

    if op_type == 'Расходы':
        category = ru.expenses[int(item_id)]['title']
    elif op_type == 'Доходы':
        category = ru.incomes[int(item_id)]['title']
    elif op_type =='Инвестиции':
        category = ru.investments[int(item_id)]['title']

    logger.info(f'Выбрана категория: {category}')  # Логирование выбора категории
    ctx.dialog_data.update(category=category)
    if not ctx.dialog_data.get('edit_category'):
        await manager.switch_to(state=FinanceStates.enter_amount)
    else:
        ctx.dialog_data.update(edit_category=False)
        await manager.switch_to(state=FinanceStates.set_operation)


async def on_entered_amount(m: Message, widget: Button, manager: DialogManager, amount: int):
    ctx = manager.current_context()
    logger.info(f'Введена сумма: {amount}')
    ctx.dialog_data.update(amount=amount)

    if not ctx.dialog_data.get('edit_amount'):
        ctx.dialog_data.update(date=datetime.now().strftime("%d-%m-%Y"))
        ctx.dialog_data.update(comment='-')
    else:
        ctx.dialog_data.update(edit_amount=False)

    await manager.switch_to(state=FinanceStates.set_operation)


async def on_execute_operation(c: CallbackQuery, widget: Select, manager: DialogManager, option):
    ctx = manager.current_context()
    logger.info(f'Выбрана опция {option}')

    # Изменение данных
    if option == 'edit_category':
        ctx.dialog_data.update(edit_category=True)
        state = FinanceStates.select_category
    elif option == 'edit_amount':
        ctx.dialog_data.update(edit_amount=True)
        state = FinanceStates.enter_amount
    elif option == 'edit_comment':
        state = FinanceStates.enter_comment
    elif option == 'edit_date':
        state = FinanceStates.edit_date

    # Отмена операции
    elif option == 'cancel_operation':
        state = FinanceStates.cancel_operation
    # Сделать платеж регулярным
    elif option == 'set_regular':
        state = FinanceStates.set_regular
    # перейти к следующей операции
    elif option == 'set_another_op':
        state = FinanceStates.select_op_type

    await manager.switch_to(state=state)


async def on_entered_comment(m: Message, widget: Button, manager: DialogManager, comment: int | str):
    ctx = manager.current_context()
    logger.info(f'Введен комментарий: {comment}')
    ctx.dialog_data.update(comment=comment)
    await manager.switch_to(state=FinanceStates.set_operation)


async def on_date_option(callback: CallbackQuery, widget, manager: DialogManager, selected_date: date):
    ctx = manager.current_context()
    chosen_date = selected_date.strftime("%d-%m-%Y")
    logger.info(f'Введена дата: {chosen_date}')
    ctx.dialog_data.update(date=chosen_date)
    await manager.switch_to(state=FinanceStates.set_operation)


async def on_chosen_frequency(user_input: CallbackQuery | Message, widget: Select, manager: DialogManager, frequency: str = None):  # button: Button,
    if isinstance(user_input, Message):
        frequency = user_input.text

    print(frequency)
    logger.info(f'Выбрана категория с item_id: {frequency}')  # Логирование выбора категории
    ctx = manager.current_context()
    ctx.dialog_data.update(op_frequency=frequency)

    await user_input.answer(text=frequency)

    if frequency == 'month':
        pass
    elif frequency == 'year':
        pass
    await manager.switch_to(state=FinanceStates.set_operation)