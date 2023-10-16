import requests
from datetime import datetime, timedelta
from config import open_weather_token, tg_bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Ініціалізуємо об'єкти бота і диспетчера
bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

# Створюємо текст для команди /help
HELP_COMMAND = """
<b>Напишіть назву міста, щоб дізнатися поточну погоду</b>
<b>/start</b> - <em>Запустити бота</em>
<b>/help</b> - <em>Список команд</em>
"""


# Обробник команди /start
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.reply("Привіт! Я - твій Телеграм бот погоди. Щоб дізнатися погоду в своєму місті, просто введи "
                        "назву свого міста. Наприклад, якщо ти хочеш дізнатися погоду в Києві, просто введи 'Київ'. Я "
                        "буду повідомляти тебе про погоду у режимі реального часу, а також надавати детальну "
                        "інформацію про температуру, вологість, швидкість вітру та інші метеорологічні показники. Для "
                        "отримання додаткової інформації ти можеш скористатися командою /help. Що б ти не робив - "
                        "залишайся на зв'язку, а я завжди буду з тобою, щоб нагадати тобі про потребу взяти з собою "
                        "парасольку або куртку на прогулянку!)")


# Обробник команди /help
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode='HTML')


# Обробник повідомлень з назвою міста
@dp.message_handler()
async def get_weather(message: types.Message):
    global text
    global resoult
    global markup
    global markup2
    text = message.text

    # Ініціалізація кнопок 'Прогноз на 3 дні' та 'Подробніше'
    markup = InlineKeyboardMarkup(row_width=2)

    text_button = 'Прогноз на 3 дні'
    text_in_more_detail = 'Подробніше'

    button = InlineKeyboardButton(text=text_button, callback_data='id')
    in_more_detail = InlineKeyboardButton(text=text_in_more_detail, url=f"https://ua.sinoptik.ua/погода-{text.lower()}")
    markup.add(button, in_more_detail)

    # Ініціалізація кнопки 'Назад'
    markup2 = InlineKeyboardMarkup()

    text_return_button = 'Назад'

    return_button = InlineKeyboardButton(text=text_return_button, callback_data='id2')
    markup2.add(return_button)

    # Створюємо словник для заміни коду погоди на відповідний емоджі
    code_to_smile = {
        'Clear': "Сонячно \U00002600",
        'Clouds': "Хмарно \U00002601",
        'Rain': "Дощ \U00002614",
        'Drizzle': "Дощик \U00002614",
        'Thunderstorm': "Гроза \U000026A1",
        'Snow': "Сніг \U0001F328",
        'Mist': "Туман \U0001F32B"

    }

    try:
        # Ініціалізуємо get-запрос на сайт openweather для отримання данних з погоди і перетворювання їх у формат json
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={text}&appid={open_weather_token}&units=metric')
        data = r.json()

        # Додавання смайликів, в залежності від стану погоди
        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            smile = code_to_smile[weather_description]

        else:
            smile = 'Не можу розібрати погоду :('

        # Ініціалізація данних про погоду, що будуть виводитися
        country = data['sys']['country']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.fromtimestamp(data['sys']['sunset'])
        lenght_of_the_day = sunset - sunrise

        # Ініціалізація змінної, що містить в собі текст про поточну погоду
        resoult = (f'<b>\U0001F566{datetime.now().strftime("%Y-%m-%d %H:%M")}\U0001F566 \n</b>'
                   f'<b>\U0001F30DПогода в місті: {message.text} ({country})\U0001F30D \n</b>'
                   f'\n'
                   f'<b>{smile}\n</b>'
                   f'Температура: {int(temp)}°C\n'
                   f'Відчувається як: {int(feels_like)}°C\n'
                   f'Вологість: {humidity}%\n'
                   f'Тиск: {pressure}\n'
                   f'Швидкість вітру: {wind} м/с\n'
                   f'Світанок: {sunrise}\n'
                   f'Захід сонця: {sunset}\n'
                   f'Тривалість світлового дня: {lenght_of_the_day}\n'
                   f'---------\n'
                   f'<b>Слава Україні \U0001F1FA\U0001F1E6</b>'
                   )
        # Вивід користовачу данних про погоду з розміщенням кнопок 'Прогноз на 3 дні' та 'Подробніше'
        await bot.send_message(message.chat.id, resoult, reply_markup=markup, parse_mode='HTML')

    # Обробник помилок
    except Exception as ex:
        await message.reply('\U0001F6AB Перевірьте назву міста \U0001F6AB')


# Обробник функції tree_days/Обробник натискання кнопки
@dp.callback_query_handler()
async def three_days(callback: types.CallbackQuery):
    # Обробник кнопки 'Прогноз на 3 дні'
    if callback.data == 'id':

        # Створюємо словник для заміни коду погоди на відповідний емоджі
        all_data = []
        code_to_smile = {
            'Clear': "Сонячно \U00002600",
            'Clouds': "Хмарно \U00002601",
            'Rain': "Дощ \U00002614",
            'Drizzle': "Дощик \U00002614",
            'Thunderstorm': "Гроза \U000026A1",
            'Snow': "Сніг \U0001F328",
            'Mist': "Туман \U0001F32B"

        }
        try:
            r = requests.get(
                f'https://api.openweathermap.org/data/2.5/forecast?q={text}&appid={open_weather_token}&units=metric')
            i = r.json()
            list = i['list']

            # отримуємо поточну дату
            today = datetime.today().date()
            # отримуємо наступний день
            tomorrow = today + timedelta(days=1)
            # отримуємо третій день для обмеження роботи програми по його закінченню
            three_days_from_now = today + timedelta(days=3)

            for i in list:
                # Ініціалізація змінних
                dt_txt = i['dt_txt']
                temp = i['main']['temp']
                # отримуємо дату
                date = dt_txt[:10]
                # отримуємо час
                time = dt_txt[11:16]

                # Ініціалізація змінної, що вказує на потрібний емоджі
                weather_description = i['weather'][0]['main']
                if weather_description in code_to_smile:
                    smile = code_to_smile[weather_description]
                else:
                    smile = 'Не можу розібрати погоду :('

                # завершення циклу по закінченню третього дня
                if date > str(three_days_from_now):
                    break

                # обробник виводу дати та часу та записування данних в список all_data для корректного виводу
                if date >= str(tomorrow):
                    if time == '00:00':
                        all_data.append('')
                        all_data.append('<b>\U0001F5D3' + date + '\U0001F5D3</b >')

                    all_data.append(f'<b>{time}:</b> '
                                    f'{smile}, {int(temp)}°C')

            # перетворювання all_data у формат string
            res = '\n'.join(all_data)

            # Видалення попереднього повідомлення та вивід данних про погоду на 3 дні/розміщення кнопки 'Назад'
            await bot.delete_message(callback.from_user.id, callback.message.message_id)
            await bot.send_message(callback.message.chat.id, res, reply_markup=markup2, parse_mode='HTML')

        # Обробник помилок
        except Exception as ex:
            print(ex)

    # Обробник кнопки 'Назад'
    elif callback.data == 'id2':
        # Видалення попереднього повідомлення та вивід тексту про поточну погоду
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
        await bot.send_message(callback.message.chat.id, resoult, reply_markup=markup, parse_mode='HTML')


# Запускаємо бота
if __name__ == '__main__':
    executor.start_polling(dp)
