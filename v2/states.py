from aiogram.fsm.state import StatesGroup, State


class FinanceStates(StatesGroup):
    select_op_type = State()
    select_category = State()  #  добавить возможность редактирования, а не только ввода
    enter_amount = State()  #  добавить возможность редактирования, а не только ввода

    set_operation = State()

    enter_comment = State()
    edit_date = State()

    cancel_operation = State()
    set_regular = State()
