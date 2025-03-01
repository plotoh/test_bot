from aiogram_dialog import DialogManager


async def window1_get_data(**kwargs):
    return {
        "something": "data from Window1 getter",
    }


async def window2_get_data(**kwargs):
    return {
        "something": "data from Window2 getter",
    }


async def dialog_get_data(**kwargs):
    return {
        "name": "платон",
    }


async def get_categories(dialog_manager: DialogManager, **middleware_data):
    expenses_dct = {'products': '🛒 Продукты и хозтовары', 'snacks': '🍕 Вкусняшки', 'bus': '🚇Автобусы',
                    'taxi': '🚕 Такси ',
                    'clothes': '👕Одежда', 'gifts': '🎁 Подарки', 'leisure': '🎳 Досуг', 'emergency': '🚧 Непредвиденное',
                    'care': '🦷 Уход за собой', 'fast_food': '🍔 Еда вне дома', 'partner': '❤️ Партнер',
                    'education': '📚 Образование', 'communication': '🚰 К \\ У, связь', 'parents': 'Помощь родителям',
                    'housee': '🏡 Дом, ремонт', 'other': '🌎 Прочие'}  # , 'cancel': 'Отмена'
    incomes_dct = {'salary': '💵 Зарплата', 'underworking': '🛠️ Подработка', 'selling': '💲 Продажа вещей',
                   'cashback': '🪙Кэшбек', 'freelance': '💻 Фриланс', 'deal': '🤝 Услуги', }
    investments_dct = {'deposits': '🏦 Вклады', 'stock': '📈 Акции', 'dividends': '💰 Дивиденды', 'crypto': '🎰 Крипта', }

    if dialog_manager.current_context().dialog_data['operation_type'] == 'expenses':
        data = {
            'categories': [
                (v, k)
                for k, v in expenses_dct.items()
            ],
        }
    elif dialog_manager.current_context().dialog_data['operation_type'] == 'incomes':
        data = {
            'categories': [
                (v, k)
                for k, v in incomes_dct.items()
            ],
        }
    elif dialog_manager.current_context().dialog_data['operation_type'] == 'investments':
        data = {
            'categories': [
                (v, k)
                for k, v in investments_dct.items()
            ],
        }
    return data
