from aiogram.fsm.state import State,StatesGroup


class ProductState(StatesGroup):
    name = State()
    description = State()
    price = State()
    address = State()
    image = State()
