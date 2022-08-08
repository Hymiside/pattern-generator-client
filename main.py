from aiogram import Bot, Dispatcher, executor, types


bot = Bot(token="5564021133:AAESz5jSDpDYdOERnfIHtQGlOOt9sbIpDcc")
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)