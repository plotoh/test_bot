from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram_dialog import Dialog, DialogManager, DialogRegistry, Window
from aiogram_dialog.widgets.kbd import Calendar, Cancel
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.input.calendar import CalendarConfig
from datetime import date

# Импортируем необходимые компоненты
from aiogram_dialog import StartMode

# Создаем бота и диспетчер
bot = Bot(token="YOUR_BOT_TOKEN")
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Регистрируем диалог
registry = DialogRegistry(dp)

# Обработчик выбора даты
async def on_date_selected(callback: types.CallbackQuery, widget, manager: DialogManager, selected_date: date):
    await callback.message.answer(f"Вы выбрали дату: {selected_date}")
    await manager.done()

# Создаем диалог с календарем
calendar_dialog = Dialog(
    Window(
        Const("Выберите дату:"),
        Calendar(
            id="calendar",
            on_click=on_date_selected,
            config=CalendarConfig(
                firstweekday=0,  # Первый день недели (0 - понедельник, 6 - воскресенье)
            ),
        ),
        Cancel(Const("Отмена")),
        state="calendar_state",
    )
)

# Регистрируем диалог
registry.register(calendar_dialog)

# Команда для запуска диалога
@dp.message_handler(commands=["start"])
async def start_calendar(message: types.Message, dialog_manager: DialogManager):
    await dialog_manager.start("calendar_state", mode=StartMode.RESET_STACK)

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)