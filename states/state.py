from aiogram.filters.state import State, StatesGroup

class FileCompressState(StatesGroup):
    start = State()
    final = State()