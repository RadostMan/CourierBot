from aiogram import Bot, Dispatcher, executor, types
import os

bot = Bot(os.getenv("OZON_BOT_TOKEN"))
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text)


if __name__ == '__main__':
    executor.start_polling(dp)