from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="Добавить карточки", callback_data="add_flashcards"),
    InlineKeyboardButton(text="Тренировать карточки", callback_data="training")],
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)

adding_confirmation = [
    [InlineKeyboardButton(text="Да", callback_data="accepted_new_card"),
    InlineKeyboardButton(text="Нет", callback_data="rejected_new_card")],
]
adding_confirmation = InlineKeyboardMarkup(inline_keyboard=adding_confirmation)

retry_confirmation = [
    [InlineKeyboardButton(text="Добавить еще карточку", callback_data="accepted_retry_card"),
    InlineKeyboardButton(text="Вернуться в главное меню", callback_data="rejected_retry_card")],
]
retry_confirmation = InlineKeyboardMarkup(inline_keyboard=retry_confirmation)







# exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
# iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])