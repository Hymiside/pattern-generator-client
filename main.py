from aiogram import Bot, Dispatcher, executor, types

from config import Config


config = Config()
bot = Bot(token=config.token)
dp = Dispatcher(bot)


@dp.message_handler(commands="start", state="*")
async def start(message: types.Message):
    await message.answer("dsf")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

