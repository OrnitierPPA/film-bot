from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

drama = KeyboardButton(text = 'Драма 😧')
comedy = KeyboardButton(text = 'Комедии 😁')
musical = KeyboardButton(text = 'Мюзикл 🎵')
romance = KeyboardButton(text = 'Романтика 🥰')
horror = KeyboardButton(text = 'Ужасы 🔪')
fantasy = KeyboardButton(text = 'Фэнтази 🧝🧙')
action = KeyboardButton(text = 'Экшен 🥷')

kd = ReplyKeyboardMarkup().add(drama).add(comedy).add(musical).add(romance).add(horror).add(fantasy).add(action)