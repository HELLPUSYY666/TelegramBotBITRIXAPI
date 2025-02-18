from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery
import app.keyboards.keyboards as kb
from aiogram.fsm.context import FSMContext
import app.database.requests as rq
from app.keyboards import keyboard_webenar as webenar_kb

router = Router()


class WebinarRegistration(StatesGroup):
    full_name = State()
    phone = State()
    email = State()
    region = State()
    specialty = State()


@router.message(F.text == "🔙 Назад")
async def go_back(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Вы вернулись в главное меню", reply_markup=webenar_kb.main_menu)


@router.message(F.text == "✅ Подтвердить регистрацию")
async def go_back(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Вы вернулись в главное меню", reply_markup=webenar_kb.main_menu)


@router.message(F.text == "📅 Регистрация на вебинар")
async def register_webinar(message: Message, state: FSMContext):
    await state.set_state(WebinarRegistration.full_name)
    await message.answer("Введите ваше *ФИО*:", reply_markup=webenar_kb.back_button)


@router.message(WebinarRegistration.full_name)
async def get_full_name(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await state.set_state(WebinarRegistration.phone)
    await message.answer("Введите ваш *номер телефона*:", reply_markup=webenar_kb.back_button)


@router.message(WebinarRegistration.phone)
async def get_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await state.set_state(WebinarRegistration.email)
    await message.answer("Введите ваш *E-mail*:", reply_markup=webenar_kb.back_button)


@router.message(WebinarRegistration.email)
async def get_email(message: Message, state: FSMContext):
    if "@" not in message.text or "." not in message.text:
        await message.answer("⚠️ Введите корректный email!")
        return
    await state.update_data(email=message.text)
    await state.set_state(WebinarRegistration.region)
    await message.answer("Введите ваш *регион*:", reply_markup=webenar_kb.back_button)


@router.message(WebinarRegistration.region)
async def get_region(message: Message, state: FSMContext):
    await state.update_data(region=message.text)
    await state.set_state(WebinarRegistration.specialty)
    await message.answer("Введите вашу *специальность*:", reply_markup=webenar_kb.back_button)


@router.message(WebinarRegistration.specialty)
async def get_specialty(message: Message, state: FSMContext):
    user_data = await state.get_data()
    user_data["specialty"] = message.text

    # Отправляем данные в Битрикс (пример)
    # send_to_bitrix(user_data)
    user = await rq.save_user_data(user_data, tg_id=message.from_user.id)

    await message.answer(
        f"🎉 Вы успешно зарегистрированы на вебинар!\n\n"
        f"👤 *ФИО*: {user_data['full_name']}\n"
        f"📞 *Телефон*: {user_data['phone']}\n"
        f"📧 *Email*: {user_data['email']}\n"
        f"🌍 *Регион*: {user_data['region']}\n"
        f"💼 *Специальность*: {user_data['specialty']}\n",
        reply_markup=webenar_kb.confirm_kb
    )
    await state.clear()
