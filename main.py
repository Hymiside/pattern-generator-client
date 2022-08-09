from typing import Dict

from aiogram import Bot, Dispatcher, executor, types

from config import Config
from pkg.service import service
from pkg.keyboard import keyboard


config = Config()
bot = Bot(token=config.token)
dp = Dispatcher(bot)


@dp.message_handler(commands="start", state="*")
async def start(message: types.Message):
    response: Dict[str, str] = service.user_status(message.from_user.id)

    match response["status"]:
        case "user already exists":
            await message.answer("Управляй ботом с помощью клавиатуры и создавай"
                                 " новые интересные паттерны из сообщений в Telegram 👇", reply_markup=keyboard.main_keyboard(), parse_mode=types.ParseMode.MARKDOWN_V2)
        case "user does not exist":
            await message.answer(f"*Привет, {message.from_user.full_name}👋*\n\nЭто "
                                 f"бот умеет создавать паттерны из сообщений в Telegram, скорее читай инструкцию и создавай свой первый паттерн 👇\n\n"
                                 f"*Кстати*, мы зачислили тебе на счёт *50 бонусных рублей*, чтобы ты мог посмотреть как работает бот 💸", reply_markup=keyboard.main_keyboard(),
                                 parse_mode=types.ParseMode.MARKDOWN)
        case "error":
            await message.answer("**Бот поломался :(**\n\nСообщи пожалуйста "
                                 "об этом @hymiside", parse_mode=types.ParseMode.MARKDOWN_V2)


@dp.callback_query_handler(text="balance")
async def get_balance(callback: types.CallbackQuery):
    response: Dict[str, str] = service.get_balance(callback.from_user.id)
    match response["status"]:
        case "ok":
            await callback.message.edit_text(f"💰 Ваш баланс составляет: {response['balance']} рублей 💰")
            await callback.message.edit_reply_markup(reply_markup=keyboard.back_keyboard())
            await callback.answer()
        case "error":
            await callback.message.edit_text("Произошла ошибка, приносим свои извинения ¯\_(ツ)_/¯")
            await callback.message.edit_reply_markup(reply_markup=keyboard.back_keyboard())
            await callback.answer()


@dp.callback_query_handler(text="update_cash")
async def update_cash(callback: types.CallbackQuery):
    await callback.message.edit_text("Выбери сумму на которую ты хочешь пополнить счёт 💸👇")
    await callback.message.edit_reply_markup(reply_markup=keyboard.cash_keyboard())
    await callback.answer()


@dp.callback_query_handler(text="back")
async def update_cash(callback: types.CallbackQuery):
    await callback.message.edit_text("Управляй ботом с помощью клавиатуры и создавай"
                                     " новые интересные паттерны из сообщений в Telegram 👇")
    await callback.message.edit_reply_markup(reply_markup=keyboard.main_keyboard())
    await callback.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
