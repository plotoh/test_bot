from aiogram.fsm.state import StatesGroup, State


class FinanceStates(StatesGroup):
    select_op_types = State()
    select_categories = State()
    enter_amount = State()
    set_operation = State()


class EditOperation(StatesGroup):
    enter_comment = State()
    edit_category = State()
    edit_amount = State()
    edit_date = State()
    cancel_operation = State()
    set_regular = State()