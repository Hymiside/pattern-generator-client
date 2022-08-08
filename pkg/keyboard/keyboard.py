from aiogram import types


def main_keyboard() -> types.InlineKeyboardMarkup:
    buttons = [
        types.InlineKeyboardButton(text="Создать паттерн", callback_data="generate_pattern"),
        types.InlineKeyboardButton(text="Пополнить счёт", callback_data="update_cash"),
        types.InlineKeyboardButton(text="Инструкция", callback_data="tutorial"),
        types.InlineKeyboardButton(text="Профиль", callback_data="profile")
    ]
    inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
    inline_keyboard.add(*buttons)
    return inline_keyboard


def cash_keyboard() -> types.InlineKeyboardMarkup:
    buttons = [
        types.InlineKeyboardButton(text="50 рублей", callback_data="rub50"),
        types.InlineKeyboardButton(text="150 рублей", callback_data="rub150"),
        types.InlineKeyboardButton(text="300 рублей", callback_data="rub300"),
        types.InlineKeyboardButton(text="1к на еду", callback_data="rub1000"),
        types.InlineKeyboardButton(text="Вернуться назад", callback_data="back")
    ]
    inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
    inline_keyboard.add(*buttons)
    return inline_keyboard


def back_keyboard() -> types.InlineKeyboardMarkup:
    inline_keyboard = types.InlineKeyboardMarkup(row_width=1)
    inline_keyboard.add(types.InlineKeyboardButton(text="Вернуться назад", callback_data="back"))
    return inline_keyboard
