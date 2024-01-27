from aiogram import F, Router, types, flags
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types.callback_query import CallbackQuery

from states import Gen 
import kb
import text
from process import add_word 


router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)


@router.callback_query(F.data == "add_flashcards")
async def add_flashcards(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.adding_en_meaning)
    await clbck.message.edit_text(text.process)


@router.message(Gen.adding_en_meaning)
async def english_meaning(en_word: Message, state: FSMContext):
    await state.update_data(en_word=en_word.text)
    await state.set_state(Gen.adding_ru_meaning)
    await en_word.answer(text.first_word)


@router.message(Gen.adding_ru_meaning)
async def russian_meaning(ru_word: Message, state: FSMContext):
    await state.update_data(ru_word=ru_word.text)
    await state.set_state(Gen.finish_adding)
    data = await state.get_data()
    print(data['en_word'], data['ru_word'])
    await ru_word.answer(text.confirmation.format(en_word=data['en_word'].title(), ru_word=data['ru_word'].title()), reply_markup=kb.adding_confirmation)


@router.callback_query(F.data == "accepted_new_card")
async def add_confirmation(clbck: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    add_word((data['en_word']).lower(), (data['ru_word']).lower())
    await clbck.message.edit_text(text.ready, reply_markup=kb.retry_confirmation)
    await state.clear()


@router.callback_query(F.data == "accepted_retry_card")
async def retry_confrimation(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.adding_en_meaning)
    await clbck.message.edit_text(text.process)

@router.callback_query(F.data == "rejected_retry_card")
async def back_to_the_menu(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.edit_text(text.menu, reply_markup=kb.menu)