"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '7984621034:AAHYG9d8ZgFd2umgPqGDC5ypeN39HgSVQx8'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/cats.jpg', 'rb') as photo:
        await bot.send_photo(message.chat.id, photo, caption='xush kelibsiz botga ',
                             reply_to_message_id=message.message_id)


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp)