from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Group, Url, CalendarConfig, Cancel, Back
from aiogram_dialog.widgets.kbd import Calendar
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const, Format

from v2 import getters, keyboards, selected, handlers as h, lexicon as l
from v2.states import FinanceStates


def operation_type_window():
    return Window(
        Const('Выбери тип операции'),
        keyboards.finance_menu(selected.on_chosen_operation_type),  # функция коллбэка при нажатии на кнопку
        Url(
            Const("Google таблица\n\nПока что ссылка на создателя aiogram"),
            Const('https://github.com/Tishka17/aiogram_dialog/'),
        ),
        Cancel(Const('Закрыть')),
        state=FinanceStates.select_op_type,
        getter=getters.get_finance_menu,
    )


def category_window():
    return Window(
        Format('{op_type} | Выбери категорию'),
        keyboards.categories(selected.on_chosen_category),  # функция коллбэка при нажатии на кнопку
        Back(Const('Вернуться к выбору типа')),
        state=FinanceStates.select_category,
        getter=getters.get_categories,
    )


def enter_amount_window():
    return Window(
        Format("{op_type} | {category}\nВведи сумму"),
        TextInput(
            id="amount",
            on_error=h.amount_error,
            on_success=selected.on_entered_amount,
            type_factory=int,
        ),
        Back(Const('Вернуться к выбору категории')),
        Cancel(Const('Прекратить')),
        state=FinanceStates.enter_amount,
        getter=getters.get_executed_operation
    )


def execute_operation_window():
    return Window(
        Format('{op_type} -- {category}\nСумма: {amount}\nДата: {date}\nКомментарий: {comment}'),
        # Format('Тип операции -- Категория\nСумма - \nДата - \nКомментарий - \n - \n'),
        keyboards.execute_operation_option(selected.on_execute_operation),  # функция коллбэка при нажатии на кнопку
        state=FinanceStates.set_operation,
        getter=getters.get_executed_operation,
    )


def edit_comment_window():
    return Window(
        Format('{op_type} -- {category}\nСумма: {amount}\n\nВведи комментарий'),
        TextInput(
            id="comment",
            on_error=h.comment_error,
            on_success=selected.on_entered_comment,
            type_factory=str,
        ),
        Back(Const('Вернуться к операции')),
        state=FinanceStates.enter_comment,
        getter=getters.get_executed_operation
    )


def edit_date_window():
    return Window(
        Format("{op_type} -- {category}\nСумма: {amount}\nКомментарий: {comment}\nДата: {date}\n\nВыбери дату"),
        keyboards.calendar,
        state=FinanceStates.edit_date,
        getter=getters.get_executed_operation
    )


def cancel_operation_window():
    return Window(
        Const('Операция отменена.\nВыбери тип операции'),
        keyboards.finance_menu(selected.on_chosen_operation_type),  # функция коллбэка при нажатии на кнопку
        Cancel(Const('Закрыть')),
        state=FinanceStates.cancel_operation,
        getter=getters.get_finance_menu,
    )


def set_regular_window():
    return Window(
        Const(
            'Сделать операцию регулярной. Введи частоту в днях (до 365 дней)\nЛибо выбери из предложенных вариантов.'),
        keyboards.frequency(selected.on_chosen_frequency),
        Back(Const('Назад')),
        TextInput(id="frequency", on_success=selected.on_chosen_frequency),
        state=FinanceStates.set_regular,
        getter=getters.get_op_frequency,
    )


finance_dialog = Dialog(
    operation_type_window(),
    category_window(),
    enter_amount_window(),
    execute_operation_window(),
    edit_comment_window(),
    edit_date_window(),
    cancel_operation_window(),
    set_regular_window(),
)
