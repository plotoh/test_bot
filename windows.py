from datetime import date

from aiogram_dialog.widgets.input import MessageInput, TextInput
from aiogram_dialog.widgets.kbd import Button, ListGroup, Group, ScrollingGroup, Url, Next, CalendarConfig
from aiogram_dialog.widgets.kbd import Calendar
from aiogram_dialog import Window, Dialog, DialogManager
from aiogram_dialog.widgets.kbd import Button, Back
from aiogram_dialog.widgets.text import Const, Format

import getters
import selected as s
from handlers import error
from states import MySG

expenses_dct = {'products': '🛒 Продукты и хозтовары', 'snacks': '🍕 Вкусняшки', 'bus': '🚇Автобусы', 'taxi': '🚕 Такси ',
                'clothes': '👕Одежда', 'gifts': '🎁 Подарки', 'leisure': '🎳 Досуг', 'emergency': '🚧 Непредвиденное',
                'care': '🦷 Уход за собой', 'fast_food': '🍔 Еда вне дома', 'partner': '❤️ Партнер',
                'education': '📚 Образование', 'communication': '🚰 К \\ У, связь', 'parents': 'Помощь родителям',
                'housee': '🏡 Дом, ремонт', 'other': '🌎 Прочие'}  # , 'cancel': 'Отмена'
incomes_dct = {'salary': '💵 Зарплата', 'underworking': '🛠️ Подработка', 'selling': '💲 Продажа вещей',
               'cashback': '🪙Кэшбек', 'freelance': '💻 Фриланс', 'deal': '🤝 Услуги', }
investments_dct = {'deposits': '🏦 Вклады', 'stock': '📈 Акции', 'dividends': '💰 Дивиденды', 'crypto': '🎰 Крипта', }

operation_type_window = Window(
    Format("здарова, {name}!"),
    Group(
        Button(Const("Расходы"), id="expenses", on_click=s.select_operation_type),
        Button(Const("Доходы"), id="incomes", on_click=s.select_operation_type),
        Button(Const("Инвестиции"), id="investments", on_click=s.select_operation_type),
        Button(Const("Таблица"), id="table", on_click=s.select_operation_type),
        Button(Const("Настройки"), id="settings", on_click=s.select_operation_type),
        width=3,
    ),
    state=MySG.select_operation_type, )
# getter=window1_get_data,  # here we specify data getter for window1


expenses_categories_window = Window(
    Format("{dialog_data[operation_type]} --- Категории"),
    Button(Const("Назад"), id="back", on_click=s.back_to_operation_type),
    ScrollingGroup(
        *[Button(Const(v), id=k, on_click=s.select_category) for k, v in expenses_dct.items()],
        id="expenses",
        width=2,
        height=5,
    ),
    state=MySG.expenses,
)

incomes_categories_window = Window(
    Format("{dialog_data[operation_type]} --- Категории"),
    Button(Const("Назад"), id="back", on_click=s.back_to_operation_type),
    Group(
        *[Button(Const(v), id=k, on_click=s.select_category) for k, v in incomes_dct.items()],
        id="incomes",
        width=2,
    ),
    state=MySG.incomes,
)

investments_categories_window = Window(
    Format("{dialog_data[operation_type]} --- Категории"),
    Button(Const("Назад"), id="back", on_click=s.back_to_operation_type),
    Group(
        *[Button(Const(v), id=k, on_click=s.select_category) for k, v in investments_dct.items()],
        id="investments",
        width=2,
    ),
    state=MySG.investments,
)

table_window = Window(
    Format(
        "Ссылка на таблицу\n\n Сделать в виде кнопки, а текстом данные о таблице\n\nдолжно выводиться как диалоговое окно, а не как простое сообщение"),
    Url(
        Const("Google таблица\n\nПока что ссылка на создателя aiogram"),
        Const('https://github.com/Tishka17/aiogram_dialog/'),
    ),
    Button(Const("Назад"), id="back", on_click=s.back_to_operation_type),
    state=MySG.table, )

settings_window = Window(
    Format(
        "Меню настроек\n\n Сделать в виде кнопок, вероятно checkbox\n\nдолжно выводиться как диалоговое окно, а не как простое сообщение"),
    Group(
        Button(Const("1"), id="1", ),  # on_click=select_operation_type
        Button(Const("2"), id="2"),
        Button(Const("3"), id="3"),
        Button(Const("4"), id="4"),
        Button(Const("5"), id="5"),
        width=1,
    ),
    Button(Const("Назад"), id="back", on_click=s.back_to_operation_type),
    state=MySG.settings, )

amount_input_window = Window(
    Const("Введи сумму"),
    TextInput(
        id="amount",
        on_error=error,
        on_success=s.on_entered_amount,
        type_factory=int,
    ),
    state=MySG.enter_amount,
)

set_operation_window = Window(
    Format(
        '{dialog_data[operation_type]} | Категория - {dialog_data[category]}\nСумма - {dialog_data[amount]}\nДата - {dialog_data[date]}\n\nсделать красиво, вывести сумму за день, добавить эмодзи, дату сделать по часам и красивую и т.д.'),
    Group(
        Button(Const("Категория"), id="edit_category", on_click=s.select_edit_option),
        Button(Const("Дата"), id="edit_date", on_click=s.on_date_selected),
        Button(Const("Сумма"), id="edit_amount", on_click=s.select_edit_option),
        Button(Const("Коммент"), id="enter_comment", on_click=s.select_edit_option),
        Button(Const("Отменить"), id="cancel_op", on_click=s.select_edit_option),
        Button(Const("Регулярный"), id="regular_op", on_click=s.select_edit_option),
        width=3,
    ),
    state=MySG.set_operation,
)

comment_input_window = Window(
    Const("Напиши комментарий"),
    TextInput(
        id="amount",
        on_error=error,
        on_success=s.on_entered_comment,
        type_factory=str,
    ),
    state=MySG.enter_comment,
)
calendar = Calendar(
    id="calendar",
    on_click=s.on_date_selected,
    config=CalendarConfig(
        firstweekday=0,  # Первый день недели (0 - понедельник, 6 - воскресенье)
       ),
)

edit_date_window = Window(
    Const("Выбери дату"),
    Button(Const("Назад"), id="back", on_click=s.select_edit_option),
    calendar,
    state=MySG.edit_date,
)

finance_dialog = Dialog(
    operation_type_window,
    expenses_categories_window,
    incomes_categories_window,
    investments_categories_window,
    table_window,
    settings_window,
    amount_input_window,
    set_operation_window,
    comment_input_window,
    # edit_date_window,
    getter=getters.dialog_get_data  # здесь мы указываем метод получения данных для диалога
)

# переписать логику кнопки назад
# выводить календарь
# переписать логику календаря
