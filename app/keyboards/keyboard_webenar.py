from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


confirm_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="✅ Подтвердить регистрацию")]],
    resize_keyboard=True
)

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📅 Регистрация на вебинар")],
        [KeyboardButton(text="📆 Расписание"), KeyboardButton(text="📦 Каталог товаров")],
        [KeyboardButton(text="🔙 Назад")]
    ],
    resize_keyboard=True
)

back_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔙 Назад")]
    ],
    resize_keyboard=True
)