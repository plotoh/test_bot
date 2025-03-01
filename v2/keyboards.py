import operator

from aiogram_dialog.widgets.kbd import Group, Select, ListGroup, ScrollingGroup
from aiogram_dialog.widgets.text import Format

import logging

# Настройка логгирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEFAULT_HEIGHT = 5


def finance_menu(on_click):
    logger.info('Создание меню финансов')  # Логгирование создания меню
    return Group(
        Select(
            Format('{item[0]}'),
            id='finance_menu',
            item_id_getter=operator.itemgetter(1),
            items='op_types',  # Убедитесь, что это правильный источник данных
            on_click=on_click,
        ),
        id='finance_menu_id',
        width=3,
    )


def categories(on_click):
    logger.info('Создание меню категорий')  # Логгирование создания меню категорий
    return ScrollingGroup(
        Select(
            Format('{item[0]}'),
            id='categories_by_type',
            item_id_getter=operator.itemgetter(1),
            items='categories',  # Убедитесь, что это правильный источник данных
            on_click=on_click,
        ),
        id='categories_ids',
        width=2,
        height=DEFAULT_HEIGHT
    )
