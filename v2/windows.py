from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Group, Url, CalendarConfig, Cancel, Back
from aiogram_dialog.widgets.kbd import Calendar
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const, Format

from v2 import getters
from v2 import keyboards
from v2 import selected
from v2.states import FinanceStates


def operation_type_window():
    return Window(
        Const('Выбери тип операции'),
        keyboards.finance_menu(selected.on_chosen_operation_type),  # функция коллбэка при нажатии на кнопку
        Cancel(Const('Закрыть')),
        state=FinanceStates.select_op_types,
        getter=getters.get_finance_menu,
    )


def category_window():
    return Window(
        Format('Выбери категорию'),
        keyboards.categories(selected.on_chosen_category),  # функция коллбэка при нажатии на кнопку
        Back(Const('Вернуться к выбору типа')),
        state=FinanceStates.select_categories,
        getter=getters.get_categories,
    )


finance_dialog = Dialog(
    operation_type_window(),
    category_window(),
)
