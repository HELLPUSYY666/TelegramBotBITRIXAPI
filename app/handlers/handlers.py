from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery

import app.keyboards.keyboards as kb
import app.keyboards.keyboard_webenar as webenar_kb
from aiogram.fsm.context import FSMContext
import app.database.requests as rq

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Это тестовый бот PHCOS.",
                         reply_markup=kb.settings)


@router.callback_query(F.data == 'cosmetolog')
async def cosmetolog(callback: CallbackQuery):
    await callback.answer('Вы косметолог')
    await callback.message.answer('Привет косметолог', reply_markup=webenar_kb.main_menu)


@router.callback_query(F.data == 'owner')
async def owner(callback: CallbackQuery):
    await callback.answer('Вы владелец')
    await callback.message.answer('Привет владелец', reply_markup=webenar_kb.main_menu)


@router.callback_query(F.data == 'diller')
async def diller(callback: CallbackQuery):
    await callback.answer('Вы дилер')
    await callback.message.answer('Привет дилер')


@router.callback_query(F.data == 'buyer')
async def buyer(callback: CallbackQuery):
    await callback.answer('Вы покупатель')
    await callback.message.edit_text('Привет покупатель')
