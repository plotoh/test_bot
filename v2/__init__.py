# from aiogram import Dispatcher
#
# from aiogram_dialog import DialogRegistry
# from aiogram_dialog import Dialog
#
# from v2 import windows as w
#
#
# def bot_menu_dialogs():
#     return [
#         Dialog(
#             w.operation_type_window(),
#             w.category_window(),
#             # w.amount_window(),
#             # w.set_operation_window(),
#             # on_process_result=w.on_process_result(),
#         ),
#     ]
#
#
# def setup_dialogs(dp: Dispatcher):
#     registry = DialogRegistry(dp)
#     for dialog in [*bot_menu_dialogs()]:
#         registry.register(dialog)
#
#
#
