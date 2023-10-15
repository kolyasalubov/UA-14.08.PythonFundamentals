import telebot
from telebot import types

bot = telebot.TeleBot('6665291125:AAE9QO09o1pkkpvlYTlTzdjAitpyYlF8-Ec')

available_tables = ['Столик 1', 'Столик 2', 'Столик 3', 'Столик 4', 'Столик 5', 'Столик 6', 'Столик 7', 'Столик 8', 'Столик 9', 'Столик 10']

reservations = {}


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    order_button = types.KeyboardButton("Акції 🍔")
    menu_button = types.KeyboardButton("Меню 📜")
    hellp_button = types.KeyboardButton("Навігація 🧭")
    reserve_table = types.KeyboardButton("Замовити столик 🛒")
    markup.add(order_button, menu_button, hellp_button, reserve_table)

    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEKbdVlGaSr1TyWH25fhuCzBdrRvEOQBgACxgEAAhZCawpKI9T0ydt5RzAE")
    bot.send_message(message.chat.id, f"Вітаю!Я чат-бот ресторану 'La Danta', приходьте, ми смачно вас нагодуємо! ".format(message.from_user), reply_markup = markup)
        
@bot.message_handler()
def aliluya(message):
    if message.text == 'Акції 🍔':
        stock = open('stock.jpg', 'rb')
        bot.send_photo(message.chat.id, stock, caption="Ось наші свіжі акції!")
    elif message.text == 'Меню 📜':
        menu = open('menu.jpg', 'rb')
        bot.send_photo(message.chat.id, menu, caption="Ось наше найсмачніше меню!")
    elif message.text == 'Навігація 🧭':
        bot.send_message(message.chat.id, "Якщо ти заблукав, то тобі крупно так повезло! Зараз я тобі розповім, що, де і як\n/start = ця команда запустить бот, просто тицни\nАкції виведуть тобі фото з нашими свіжими та ще й як заманливими акціями на які ти просто не зможеш не повестись\nМеню покаже тобі меню нашего ресторану, а також, якщо ти придивишся, то побачиш , що у тебе додалася синя кнопка меню, з якою ти все зрозумієш\n Наш ресторан знаходиться у Дніпровському парку за адресою вулиця Тягинська 149, Херсон, Херсонська область, 73000\n У разі питань звертайтесь за номером +380 50 990 3272")
    elif message.text == 'Замовити столик 🛒':
        reserve_table(message)
    else:
        bot.send_message(message.chat.id, 'Вибач, я тебе не розумію, якщо ти заблукав, тицяй "Навігація 🧭"')


@bot.message_handler(commands=['reservetable'])
def reserve_table(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for table in available_tables:
        markup.add(types.KeyboardButton(table))
    
    bot.send_message(message.chat.id, "Оберіть столик з доступних:", reply_markup=markup)
    bot.register_next_step_handler(message, reserve_time)

def reserve_time(message):
    table = message.text
    if table not in available_tables:
        return reserve_table(message)
    
    bot.send_message(message.chat.id, f"Ви обрали {table}. Введіть час на який хочете замовити столик (наприклад, 18:00):")
    bot.register_next_step_handler(message, complete_reservation, table)

def complete_reservation(message, table):
    time = message.text
    if not time_is_valid(time):
        bot.send_message(message.chat.id, f"Вводьте час коректно (наприклад, 18:00), оформлюємо бронь знову")
        return reserve_time(message)

    reservations[table] = time
    bot.send_message(message.chat.id, f" {table} успішно заброньованно на {time}.")
    
    admin_chat_id = '5669937597'  
    bot.send_message(admin_chat_id, f"Прийшло нове бронювання: {table}\nЧас: {time}\nДанні замовника: {message.from_user.username}, {message.from_user.id}, {message.from_user.first_name}, {message.from_user.last_name}")

@bot.message_handler(func=lambda message: message.text.lower().endswith(' звільнено'))
def free_table(message):

    if message.chat.id == '5669937597':
        table = message.text.rsplit(' ', 1)[0] 
        
        if table in reservations:
            del reservations[table]
            bot.send_message(admin_chat_id, f"Столик {table} успішно звільнено.")
        else:
            bot.send_message(admin_chat_id, f"Столик {table} не був заброньований.")
    else:
        bot.send_message(message.chat.id, "У вас немає прав.")

def time_is_valid(time):
    try:

        hours, minutes = map(int, time.split(':'))
        if 0 <= hours <= 23 and 0 <= minutes <= 59:
            return True
        else:
            return False
        
    except ValueError:
        return False

if __name__ == "__main__":
    bot.polling()