актуальный код в папке v2
в файле seleected функция on_chosen_operation_type не получает item_id, хотя он передается, и если выводить через args  - он есть...

если выводить все что принимает функция - (CallbackQuery(*тут весь коллбэк*), <aiogram_dialog.widgets.kbd.select.Select object at 0x0000023DB68037A0>, <aiogram_dialog.manager.manager.ManagerImpl object at 0x0000023DB83D92B0>, *_'2'_*)

ошибка ---  TypeError: on_chosen_operation_type() missing 1 required positional argument: 'item_id'


полный текст ошибки -



F:\PythonProjects\test_bot\.venv\Scripts\python.exe F:\PythonProjects\test_bot\bot.py 
INFO:v2.keyboards:Создание меню финансов
INFO:v2.keyboards:Создание меню категорий
INFO:aiogram.dispatcher:Start polling
INFO:aiogram.dispatcher:Run polling for bot @ploho_dialog_bot id=7502465507 - 'ploho_dialog_bot'
INFO:aiogram.event:Update id=863509113 is handled. Duration 313 ms by bot id=7502465507
INFO:aiogram.event:Update id=863509114 is not handled. Duration 0 ms by bot id=7502465507
ERROR:aiogram.event:Cause exception while process update id=863509114 by bot id=7502465507
TypeError: on_chosen_operation_type() missing 1 required positional argument: 'item_id'
Traceback (most recent call last):
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram\dispatcher\dispatcher.py", line 309, in _process_update
    response = await self.feed_update(bot, update, **kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram\dispatcher\dispatcher.py", line 158, in feed_update
    response = await self.update.wrap_outer_middleware(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram\dispatcher\middlewares\error.py", line 25, in __call__
    return await handler(event, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram\dispatcher\middlewares\user_context.py", line 56, in __call__
    return await handler(event, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram\fsm\middleware.py", line 42, in __call__
    return await handler(event, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram_dialog\manager\manager_middleware.py", line 80, in __call__
    return await handler(event, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram\dispatcher\event\telegram.py", line 121, in trigger
    return await wrapped_inner(event, kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram\dispatcher\event\handler.py", line 43, in call
    return await wrapped()
           ^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram\dispatcher\dispatcher.py", line 276, in _listen_update
    return await self.propagate_event(update_type=update_type, event=event, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram\dispatcher\router.py", line 146, in propagate_event
    return await observer.wrap_outer_middleware(_wrapped, event=event, data=kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram_dialog\context\intent_middleware.py", line 409, in process_callback_query
    result = await handler(event, data)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram_dialog\context\intent_middleware.py", line 437, in context_unlocker_middleware
    result = await handler(event, data)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram_dialog\manager\manager_middleware.py", line 80, in __call__
    return await handler(event, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram\dispatcher\router.py", line 141, in _wrapped
    return await self._propagate_event(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram\dispatcher\router.py", line 174, in _propagate_event
    response = await router.propagate_event(update_type=update_type, event=event, **kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram\dispatcher\router.py", line 146, in propagate_event
    return await observer.wrap_outer_middleware(_wrapped, event=event, data=kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram\dispatcher\router.py", line 141, in _wrapped
    return await self._propagate_event(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram\dispatcher\router.py", line 166, in _propagate_event
    response = await observer.trigger(event, **kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram\dispatcher\event\telegram.py", line 121, in trigger
    return await wrapped_inner(event, kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram_dialog\manager\manager_middleware.py", line 55, in __call__
    return await handler(event, data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram_dialog\context\intent_middleware.py", line 426, in context_saver_middleware
    result = await handler(event, data)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram\dispatcher\event\handler.py", line 43, in call
    return await wrapped()
           ^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram_dialog\dialog.py", line 149, in _callback_handler
    processed = await window.process_callback(
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram_dialog\window.py", line 135, in process_callback
    return await self.keyboard.process_callback(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram_dialog\widgets\kbd\base.py", line 81, in process_callback
    return await self._process_other_callback(callback, dialog, manager)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram_dialog\widgets\kbd\group.py", line 76, in _process_other_callback
    if await b.process_callback(callback, dialog, manager):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram_dialog\widgets\kbd\base.py", line 81, in process_callback
    return await self._process_other_callback(callback, dialog, manager)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram_dialog\widgets\kbd\group.py", line 76, in _process_other_callback
    if await b.process_callback(callback, dialog, manager):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram_dialog\widgets\kbd\base.py", line 75, in process_callback
    return await self._process_item_callback(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram_dialog\widgets\kbd\select.py", line 122, in _process_item_callback
    await self.on_click.process_event(
  File "F:\PythonProjects\test_bot\.venv\Lib\site-packages\aiogram_dialog\widgets\widget_event.py", line 35, in process_event
    await self.callback(event, source, manager, *args, **kwargs)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: on_chosen_operation_type() missing 1 required positional argument: 'item_id'
