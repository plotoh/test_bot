from aiogram.fsm.state import StatesGroup, State


class MySG(StatesGroup):
    category_selection = State()
    select_operation_type = State()
    expenses = State()
    incomes = State()
    investments = State()
    table = State()
    settings = State()
    enter_amount = State()
    set_operation = State()
    edit_amount = State()  # упростить так, чтобы код не дублировался. и окна ввода суммы или категории можно было использовать повторно
    edit_category = State()  #
    enter_comment = State()
    edit_date = State()
    set_regular = State()
    cancel_operation = State()