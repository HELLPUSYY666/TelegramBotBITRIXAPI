from aiogram.filters import callback_data
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Косметолог', callback_data='cosmetolog')],
    [InlineKeyboardButton(text='Владелец салона красоты/клиники', callback_data='owner')],
    [InlineKeyboardButton(text='Дилер', callback_data='diller')],
    [InlineKeyboardButton(text='Покупатель', callback_data='buyer')]
])
