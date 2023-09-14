import telebot
from telebot import types
from os import listdir

bot = telebot.TeleBot('5992771765:AAFaWOHVG5LDPVTovFyYLEarivV_pAtbZPw')


def reader(list_p, name_p, adres, mode):
    logic = False if 'rb' in mode else True

    with open(f'{adres}/{[el for el in list_p if name_p in el and (".txt" in el) == logic][0]}',
              mode,
              encoding='utf-8' if logic else None) as fl:
        return fl.read()


# підекрана клавіатура
main_keyboard = types.ReplyKeyboardMarkup().add('Каталог', 'Поділитися')


# Декоратор обробки меседж команд

@bot.message_handler(commands=["start", 'help'])
def get_commands(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Привіт це магазин infinity тут ти можешь купити що тобі потрібно',
                         reply_markup=main_keyboard
                         )
    elif message.text == '/help':
        bot.send_message(message.chat.id,
                         'Привіт тут це магазин infinity тут ти можешь купити різні речі по типу одігу, іграшок та інше',
                         reply_markup=main_keyboard
                         )


# Декоратор обробки тескт меседжів
@bot.message_handler(content_types='text')
def get_text(message):
    # Обробка події натиснення кнопки Каталог
    if message.text == 'Каталог':
        # Обєкт інлайн кнопок
        inl_key_board = types.InlineKeyboardMarkup()

        # Додавання інлайн кнопок
        inl_key_board.add(types.InlineKeyboardButton('Одяг', callback_data='cat1'),
                          types.InlineKeyboardButton('Іграшки', callback_data='cat2'))

        inl_key_board.add(types.InlineKeyboardButton('Меблі', callback_data='cat3'),
                          types.InlineKeyboardButton('Гаджети', callback_data='cat4'))

        inl_key_board.add(types.InlineKeyboardButton('Побутова техніка', callback_data='cat5'),
                          types.InlineKeyboardButton('Сантехніка', callback_data='cat6'))

        bot.send_message(message.chat.id,
                         'Оберіть категорію яка вас зацікавила:',
                         reply_markup=inl_key_board)

    elif message.text == 'Поділитися':
        bot.send_message(message.chat.id, 't.me/nfinity_magazine_bot')


# Декоратор обрибки натиснення інлайн кнопок

@bot.callback_query_handler(lambda a: True)
def get_query(query):
    # обробка події натиснення інлайн кнопки Одяг callback_data=cat1

    if query.data == 'cat1':
        inl_key_board = types.InlineKeyboardMarkup()
        # додавання під категорій до Одягу
        inl_key_board.add(types.InlineKeyboardButton('Взутя', callback_data='Shoes'),
                          types.InlineKeyboardButton('Штани', callback_data='trouses'))

        inl_key_board.add(types.InlineKeyboardButton('Футболки', callback_data='T-short'),
                          types.InlineKeyboardButton('Майки', callback_data='T-shirt'))

        inl_key_board.add(types.InlineKeyboardButton('Блайзера', callback_data='Blazer'),
                          types.InlineKeyboardButton('панамки', callback_data='panama'))

        inl_key_board.add(types.InlineKeyboardButton('Сукні', callback_data='Dress'),
                          types.InlineKeyboardButton('Шорти', callback_data='short'))

        inl_key_board.add(types.InlineKeyboardButton('Шкарпетки', callback_data='soks'),
                          types.InlineKeyboardButton('Джинси', callback_data='dgence'))

        bot.send_message(query.message.chat.id,
                         'Оберіть вид одягу який вас зацікавив:',
                         reply_markup=inl_key_board)

        # події натиснення інлайн кнопки  Іграшки callbach_data=cat2
    elif query.data == 'cat2':
        inl_key_board = types.InlineKeyboardMarkup()
        # Додавання під категорій до кнопки Іграшки

        inl_key_board.add(types.InlineKeyboardButton('Поп ит', callback_data='pop'),
                          types.InlineKeyboardButton('Дитячі мячі', callback_data='ball'))

        inl_key_board.add(types.InlineKeyboardButton('Машинки', callback_data='car'),
                          types.InlineKeyboardButton('Бейблейди', callback_data='beyblade'))

        inl_key_board.add(types.InlineKeyboardButton('Фігурки Супер героїв', callback_data='super_hero'),
                          types.InlineKeyboardButton('Конструртор Лего', callback_data='lego'))

        inl_key_board.add(types.InlineKeyboardButton('Монополія', callback_data='monopoly'),
                          types.InlineKeyboardButton('Коструктор Знаток', callback_data='znatok'))

        bot.send_message(query.message.chat.id,
                         'Оберіть категорію іграшок яка вас зацікавила:',
                         reply_markup=inl_key_board)

    if query.data == 'cat3':
        inl_key_board = types.InlineKeyboardMarkup()
        # додавання під категорій до Меблі
        inl_key_board.add(types.InlineKeyboardButton('дивани', callback_data='Sofa'),
                          types.InlineKeyboardButton('крісла', callback_data='back_chairs'))

        inl_key_board.add(types.InlineKeyboardButton('Стілець', callback_data='chairs'),
                          types.InlineKeyboardButton('Ліжка', callback_data='bad'))

        inl_key_board.add(types.InlineKeyboardButton('Шафа', callback_data='Closet'),
                          types.InlineKeyboardButton('Тумбочки', callback_data='Bedside tables'))

        inl_key_board.add(types.InlineKeyboardButton('Ванна', callback_data='Bath'),
                          types.InlineKeyboardButton('Люстри', callback_data='Chandeliers'))

        inl_key_board.add(types.InlineKeyboardButton('Столи', callback_data='tish'),
                          types.InlineKeyboardButton('Двері', callback_data='dor'))

        bot.send_message(query.message.chat.id,
                         'Оберіть категорію меблів яка вас зацікавила:',
                         reply_markup=inl_key_board)

    elif query.data == 'cat4':

        inl_key_board = types.InlineKeyboardMarkup()
        # додавання під категорій до Гаджети callbach_data=cat4
        inl_key_board.add(types.InlineKeyboardButton('Телефони', callback_data='phones'),
                          types.InlineKeyboardButton('планшети', callback_data='tablets'))

        inl_key_board.add(types.InlineKeyboardButton('Навушники', callback_data='Headphone'),
                          types.InlineKeyboardButton('Зарядки', callback_data='Charging'))

        inl_key_board.add(types.InlineKeyboardButton('Ноутбуки', callback_data='Laptops'),
                          types.InlineKeyboardButton('Копмпютери', callback_data='computers'))

        inl_key_board.add(types.InlineKeyboardButton('Мишки', callback_data='mause'),
                          types.InlineKeyboardButton('Мікрофони', callback_data='mike'))

        inl_key_board.add(types.InlineKeyboardButton('Телевізори', callback_data='tv'),
                          types.InlineKeyboardButton('Павербанки', callback_data='power_banks'))

        bot.send_message(query.message.chat.id,
                         'Оберіть категорію гаджетів яка вас зацікавила:',
                         reply_markup=inl_key_board)

    if query.data == 'cat5':
        inl_key_board = types.InlineKeyboardMarkup()
        # додавання під категорій до побутової техніки callback_data=cat5
        inl_key_board.add(types.InlineKeyboardButton('Мікроволновка', callback_data='Microwave'),
                          types.InlineKeyboardButton('Пилесоси', callback_data='Vacuum cleaners'))

        inl_key_board.add(types.InlineKeyboardButton('Плити', callback_data='slabs'),
                          types.InlineKeyboardButton('Духовки', callback_data='Ovens'))

        inl_key_board.add(types.InlineKeyboardButton('Холодильник', callback_data='frig'),
                          types.InlineKeyboardButton('Чайник', callback_data='Kettle'))

        inl_key_board.add(types.InlineKeyboardButton('Стіралні машини', callback_data='Washing machines'),
                          types.InlineKeyboardButton('Мультиварки', callback_data='Multicookers'))

        inl_key_board.add(types.InlineKeyboardButton('Сушилка', callback_data='Dryer'),
                          types.InlineKeyboardButton('Посудно миюша машина', callback_data='Dishwasher'))

        bot.send_message(query.message.chat.id,
                         'Оберіть категорію побутової техніки яка вас зацікавила:',
                         reply_markup=inl_key_board)

    elif query.data == 'cat6':

        inl_key_board = types.InlineKeyboardMarkup()
        # додавання під категорій до сантехніки callbach_data=cat6
        inl_key_board.add(types.InlineKeyboardButton('Душові кабіни', callback_data='Shower cabins'),
                          types.InlineKeyboardButton('Рукомийники', callback_data='Hand washers'))

        inl_key_board.add(types.InlineKeyboardButton('Шланги', callback_data='Hoses'),
                          types.InlineKeyboardButton('Крани', callback_data='Cranes'))

        inl_key_board.add(types.InlineKeyboardButton('Труби', callback_data='Pipes'),
                          types.InlineKeyboardButton('Туалети', callback_data='toilets'))

        inl_key_board.add(types.InlineKeyboardButton('Крани для душа', callback_data='Cranes_for_dysh'),
                          types.InlineKeyboardButton('Ванни', callback_data='bathes'))

        bot.send_message(query.message.chat.id,
                         'Оберіть категорію сантехніки яка вас зацікавила:',
                         reply_markup=inl_key_board)

    if query.data == 'Shoes':
        # алготитм завантаження ресурсів товарів
        address = f'magazine/clothes/shoes'

        # завантаження ресурсів
        list_product = listdir(address)

        list_uniq_name = list({el.split('.')[0] for el in list_product})

        for name_prod in list_uniq_name:
            # Відправка фотограій та опису товару
            bot.send_photo(query.message.chat.id,
                           reader(list_product, name_prod, address, 'rb'),
                           caption=reader(list_product, name_prod, address, 'r'))

    elif query.data == 'trouses':
        # алготитм завантаження ресурсів товарів
        address = f'magazine/clothes/trouser'

        # завантаження ресурсів
        list_product = listdir(address)

        list_uniq_name = list({el.split('.')[0] for el in list_product})

        for name_prod in list_uniq_name:
            # Відправка фотограій та опису товару
            bot.send_photo(query.message.chat.id,
                           reader(list_product, name_prod, address, 'rb'),
                           caption=reader(list_product, name_prod, address, 'r'))


bot.polling()
