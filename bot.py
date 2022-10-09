from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from config import token, host, user, password, db_name
from imdb import films, database
import keyboards
import psycopg2
import random
import time

bot = Bot(token = token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('Привет!\nВыберите жанр кино, который Вам нравится.', reply_markup = keyboards.kd)

# Череда команд для показа списков фильмов. Можно заменить число выводимых фильмов
@dp.message_handler(Text("Драма 😧"))
async def drama(message: types.Message):
    await message.reply('Ожидайте..')

    try:
        con = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name
        )
        con.autocommit = True
    
        with con.cursor() as cursor:
            cursor.execute(
            """SELECT header, stars, link
            FROM drama"""
            )

            headers = cursor.fetchall()

        filmlist = random.sample(headers, 5)

        for h, s, l in filmlist:
            film = f'{h} | {s} | https://www.imdb.com/{l}'

            await message.answer(film)

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)

    finally:
        if con:
            con.close()
            print('[INFO] PostgreSQL connection closed')
        
@dp.message_handler(Text("Комедии 😁"))
async def comedy(message: types.Message):
    await message.reply('Ожидайте..')

    try:
        con = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name
        )
        con.autocommit = True
    
        with con.cursor() as cursor:
            cursor.execute(
            """SELECT header, stars, link
            FROM comedy"""
            )

            headers = cursor.fetchall()

        filmlist = random.sample(headers, 5)

        for h, s, l in filmlist:
            film = f'{h} | {s} | https://www.imdb.com/{l}'

            await message.answer(film)

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)

    finally:
        if con:
            con.close()
            print('[INFO] PostgreSQL connection closed')

@dp.message_handler(Text("Мюзикл 🎵"))
async def musical(message: types.Message):
    await message.reply('Ожидайте..')

    try:
        con = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name
        )
        con.autocommit = True
    
        with con.cursor() as cursor:
            cursor.execute(
            """SELECT header, stars, link
            FROM musical"""
            )

            headers = cursor.fetchall()

        filmlist = random.sample(headers, 5)

        for h, s, l in filmlist:
            film = f'{h} | {s} | https://www.imdb.com/{l}'

            await message.answer(film)

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)

    finally:
        if con:
            con.close()
            print('[INFO] PostgreSQL connection closed')

@dp.message_handler(Text("Романтика 🥰"))
async def romance(message: types.Message):
    await message.reply('Ожидайте..')

    try:
        con = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name
        )
        con.autocommit = True
    
        with con.cursor() as cursor:
            cursor.execute(
            """SELECT header, stars, link
            FROM romance"""
            )

            headers = cursor.fetchall()

        filmlist = random.sample(headers, 5)

        for h, s, l in filmlist:
            film = f'{h} | {s} | https://www.imdb.com/{l}'

            await message.answer(film)

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)

    finally:
        if con:
            con.close()
            print('[INFO] PostgreSQL connection closed')
        
@dp.message_handler(Text("Ужасы 🔪"))
async def horror(message: types.Message):
    await message.reply('Ожидайте..')

    try:
        con = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name
        )
        con.autocommit = True
    
        with con.cursor() as cursor:
            cursor.execute(
            """SELECT header, stars, link
            FROM horror"""
            )

            headers = cursor.fetchall()

        filmlist = random.sample(headers, 5)

        for h, s, l in filmlist:
            film = f'{h} | {s} | https://www.imdb.com/{l}'

            await message.answer(film)

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)

    finally:
        if con:
            con.close()
            print('[INFO] PostgreSQL connection closed')

@dp.message_handler(Text("Фэнтази 🧝🧙"))
async def fantsy(message: types.Message):
    await message.reply('Ожидайте..')

    try:
        con = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name
        )
        con.autocommit = True
    
        with con.cursor() as cursor:
            cursor.execute(
            """SELECT header, stars, link
            FROM fantasy"""
            )

            headers = cursor.fetchall()

        filmlist = random.sample(headers, 5)

        for h, s, l in filmlist:
            film = f'{h} | {s} | https://www.imdb.com/{l}'

            await message.answer(film)

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)

    finally:
        if con:
            con.close()
            print('[INFO] PostgreSQL connection closed')

@dp.message_handler(Text("Экшен 🥷"))
async def action(message: types.Message):
    await message.reply('Ожидайте..')

    try:
        con = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name
        )
        con.autocommit = True
    
        with con.cursor() as cursor:
            cursor.execute(
            """SELECT header, stars, link
            FROM action"""
            )

            headers = cursor.fetchall()

        filmlist = random.sample(headers, 5)

        for h, s, l in filmlist:
            film = f'{h} | {s} | https://www.imdb.com/{l}'

            await message.answer(film)

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)

    finally:
        if con:
            con.close()
            print('[INFO] PostgreSQL connection closed')

@dp.message_handler(Text("Обновить список(только для владельца)")) # Обновляет списки фильмов в базе данных
async def refresh(message: types.Message):
    await message.reply('Ожидайте..')
    user_id = message.from_user.id

    if user_id == 1234567890: # Здесь впишите свой ID пользователя
        database()
        films('drama')
        time.sleep(1.5)
        print("Таблица драмы обновлена")
        films('comedy')
        time.sleep(1.5)
        print("Таблица комедий обновлена")
        films('musical')
        time.sleep(1.5)
        print("Таблица мюзиклов обновлена")
        films('romance')
        time.sleep(1.5)
        print("Таблица романтики обновлена")
        films('horror')
        time.sleep(1.5)
        print("Таблица ужасов обновлена")
        films('fantasy')
        time.sleep(1.5)
        print("Таблица фэнтези обновлена")
        films('action')
        time.sleep(1.5) 
        print("Таблица экшена обновлена")
        print('Обновление такблиц завершенно.')
    else:
        await message.reply('Эта команда Вам недоступна')

def main():
	executor.start_polling(dp)

if __name__ == '__main__':
    main()