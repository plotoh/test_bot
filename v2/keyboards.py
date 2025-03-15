import operator

from aiogram_dialog.widgets.kbd import Group, Select, ListGroup, ScrollingGroup, Button, Calendar, CalendarConfig
from aiogram_dialog.widgets.text import Format, Const

import logging

from v2 import selected

# Настройка логгирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def finance_menu(on_click):
    logger.info('Создание меню финансов')  # Логгирование создания меню
    return Group(
        Select(
            Format('{item[0]}'),
            id='s_finance_menu',
            item_id_getter=operator.itemgetter(1),  # lambda item: item,  #
            items='op_types',  # Убедитесь, что это правильный источник данных
            on_click=on_click,
        ),
        id='finance_menu_group',
        width=3,
    )


def categories(on_click):
    logger.info('Создание меню категорий')  # Логирование создания меню категорий
    return Group(
        Select(
            Format('{item[1]}'),  # Format('{item[0]}'),
            id='categories_by_type',
            item_id_getter=operator.itemgetter(0),
            items='categories',  # Убедитесь, что это правильный источник данных
            on_click=on_click,
        ),
        id='categories_ids',
        width=2,
    )


def frequency(on_click):
    logger.info('Выбор частоты')  # Логирование создания меню категорий
    return Group(
        Select(
            Format('{item[0]}'),
            id='op_frequency',
            item_id_getter=operator.itemgetter(1),
            items='frequency',  # Убедитесь, что это правильный источник данных
            on_click=on_click,
        ),
        id='frequency_options',
        width=5,
    )


def execute_operation_option(on_click):
    logger.info('Открыто меню изменения операции')  # Логгирование создания меню категорий
    return Group(
        Select(
            Format('{item[0]}'),
            id='operation',
            item_id_getter=operator.itemgetter(1),
            items='options',  # Убедитесь, что это правильный источник данных
            on_click=on_click,
        ),
        id='operation_options_ids',
        width=3,
    )


calendar = Calendar(
    id="calendar",
    on_click=selected.on_date_option,
    config=CalendarConfig(
        firstweekday=0,
    ),
)