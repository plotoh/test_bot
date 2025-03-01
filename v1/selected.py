import operator
from datetime import datetime, date
from typing import Any

from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram_dialog import Window, Dialog, DialogManager
from aiogram_dialog.widgets.kbd import Button, Back, ScrollingGroup, Select
from aiogram_dialog.widgets.text import Const, Format

from states import MySG

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def back_to_operation_type(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.switch_to(state=MySG.select_operation_type)


async def on_chosen_category(c: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    ctx = manager.current_context()
    ctx.dialog_data.update(category_id=item_id)
    await manager.switch_to(state=MySG.category_selection)


async def select_operation_type(c: CallbackQuery, button: Button, manager: DialogManager):
    finances = {
        'expenses': 'Расходы',
        'incomes': 'Доходы',
        'investments': 'Инвестиции',
    }
    expenses_dct = {'products': '🛒 Продукты и хозтовары', 'snacks': '🍕 Вкусняшки', 'bus': '🚇Автобусы',
                    'taxi': '🚕 Такси ',
                    'clothes': '👕Одежда', 'gifts': '🎁 Подарки', 'leisure': '🎳 Досуг', 'emergency': '🚧 Непредвиденное',
                    'care': '🦷 Уход за собой', 'fast_food': '🍔 Еда вне дома', 'partner': '❤️ Партнер',
                    'education': '📚 Образование', 'communication': '🚰 К \\ У, связь', 'parents': 'Помощь родителям',
                    'housee': '🏡 Дом, ремонт', 'other': '🌎 Прочие'}  # , 'cancel': 'Отмена'
    incomes_dct = {'salary': '💵 Зарплата', 'underworking': '🛠️ Подработка', 'selling': '💲 Продажа вещей',
                   'cashback': '🪙Кэшбек', 'freelance': '💻 Фриланс', 'deal': '🤝 Услуги', }
    investments_dct = {'deposits': '🏦 Вклады', 'stock': '📈 Акции', 'dividends': '💰 Дивиденды', 'crypto': '🎰 Крипта', }

    manager.dialog_data['comment'] = '-'

    if c.data == 'expenses':
        manager.dialog_data['operation_type'] = finances[c.data]
        category_keyboard = [Button(Const(v), id=k, on_click=select_category) for k, v in expenses_dct.items()]
        return category_keyboard
        # await manager.switch_to(state=MySG.expenses)
    elif c.data == 'incomes':
        manager.dialog_data['operation_type'] = finances[c.data]
        category_keyboard = [Button(Const(v), id=k, on_click=select_category) for k, v in incomes_dct.items()]
        return category_keyboard
        # await manager.switch_to(state=MySG.incomes)
    elif c.data == 'investments':
        manager.dialog_data['operation_type'] = finances[c.data]
        category_keyboard = [Button(Const(v), id=k, on_click=select_category) for k, v in investments_dct.items()]
        return category_keyboard
        # await manager.switch_to(state=MySG.investments)

    elif c.data == 'table':
        await manager.switch_to(state=MySG.table)
        # await callback.message.answer(
        #     'Ссылка на таблицу\n\n Сделать в виде кнопки, а текстом данные о таблице\n\nдолжно выводиться как '
        #     'диалоговое окно, а не как простое сообщение')
    elif c.data == 'settings':
        await manager.switch_to(state=MySG.settings)
        # await callback.message.answer('Меню настроек\n\n Сделать в виде кнопок, вероятно checkbox\n\nдолжно'
        #                               ' выводиться как диалоговое окно, а не как простое сообщение')


async def select_category(c: CallbackQuery, button: Button, manager: DialogManager):
    all_categories = {'products': '🛒 Продукты и хозтовары', 'snacks': '🍕 Вкусняшки', 'bus': '🚇Автобусы',
                      'taxi': '🚕 Такси ', 'clothes': '👕Одежда', 'gifts': '🎁 Подарки', 'leisure': '🎳 Досуг',
                      'emergency': '🚧 Непредвиденное',
                      'care': '🦷 Уход за собой', 'fast_food': '🍔 Еда вне дома', 'partner': '❤️ Партнер',
                      'education': '📚 Образование', 'communication': '🚰 К \\ У, связь', 'parents': 'Помощь родителям',
                      'housee': '🏡 Дом, ремонт', 'other': '🌎 Прочие', 'salary': '💵 Зарплата',
                      'underworking': '🛠️ Подработка', 'selling': '💲 Продажа вещей',
                      'cashback': '🪙Кэшбек', 'freelance': '💻 Фриланс', 'deal': '🤝 Услуги', 'deposits': '🏦 Вклады',
                      'stock': '📈 Акции', 'dividends': '💰 Дивиденды', 'crypto': '🎰 Крипта', }
    manager.dialog_data['category'] = all_categories[c.data]
    await manager.switch_to(state=MySG.enter_amount)


async def on_entered_amount(m: Message, button: Button, manager: DialogManager, kwargs):
    print(kwargs)
    manager.dialog_data['amount'] = int(m.text)
    manager.dialog_data['date'] = datetime.now().strftime("%d-%m-%Y")
    await manager.switch_to(state=MySG.set_operation)


async def select_edit_option(c: CallbackQuery, button: Button, manager: DialogManager):
    if c.data == 'edit_category':
        pass
    elif c.data == 'edit_date':
        pass
    elif c.data == 'edit_amount':
        pass
    elif c.data == 'enter_comment':
        pass
    elif c.data == 'cancel_op':
        pass
    elif c.data == 'regular_op':
        pass


async def on_entered_comment(m: Message, button: Button, manager: DialogManager, kwargs):
    print(kwargs)
    manager.dialog_data['comment'] = m.text
    await manager.switch_to(state=MySG.set_operation)


async def on_edit_date(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.switch_to(state=MySG.edit_date)
    await callback.answer("Выберите дату из календаря.")


async def on_date_selected(callback: CallbackQuery, widget, manager: DialogManager, selected_date: date):
    manager.dialog_data['date'] = selected_date.strftime("%d-%m-%Y")
    await callback.answer(f"Выбранная дата: {manager.dialog_data['date']}")
    await manager.switch_to(state=MySG.set_operation)


async def on_edit_category(callback: CallbackQuery, button: Button, manager: DialogManager):
    if manager.dialog_data['operation_type'] == 'expenses':
        await manager.switch_to(state=MySG.expenses)
    elif manager.dialog_data['operation_type'] == 'incomes':
        await manager.switch_to(state=MySG.incomes)
    elif manager.dialog_data['operation_type'] == 'investments':
        await manager.switch_to(state=MySG.investments)
    await manager.switch_to(state=MySG.edit_category)
    await callback.answer("Выберите категорию")


async def on_category_selected(callback: CallbackQuery, widget, manager: DialogManager, selected_date: date):
    manager.dialog_data['category'] = selected_date.strftime("%d-%m-%Y")
    await callback.answer(f"Выбранная дата: {manager.dialog_data['date']}")
    await manager.switch_to(state=MySG.set_operation)