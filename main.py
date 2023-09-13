import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('6533756398:AAFN1nBIT3VTJFpQRPU_Rhj1a-eVliWXHvs')


@bot.message_handler(commands=['start'])
def main(message):

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Блок 20W (оригинал)', callback_data='blok')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('AirPods Pro', callback_data='air1')
    btn3 = types.InlineKeyboardButton('AirPods Pro 2', callback_data='air2')
    btn4 = types.InlineKeyboardButton('AirPods 3', callback_data='air3')
    markup.row(btn2, btn3, btn4)
    btn5 = types.InlineKeyboardButton('Авито магазин', callback_data='avito')
    btn6 = types.InlineKeyboardButton('Помощь', callback_data='help')
    btn7 = types.InlineKeyboardButton('Связь с менеджером', callback_data='connect')
    markup.row(btn5, btn6)
    markup.row(btn7)

    bot.send_message(message.chat.id,
                     f'Здравствуйте, {message.from_user.first_name} ! Выберете, что Вас интересует 👇',
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'air2':

        file1 = open('Photos/Airpods pro 2/ph1.jpg', 'rb')
        file2 = open('Photos/Airpods pro 2/ph2.jpg', 'rb')
        file3 = open('Photos/Airpods pro 2/ph3.jpg', 'rb')

        bot.send_photo(callback.message.chat.id, file1)
        bot.send_photo(callback.message.chat.id, file2)
        bot.send_photo(callback.message.chat.id, file3)

        bot.send_message(callback.message.chat.id,
                         '💛AirPods Pro 2 (Lux) 💎\n с шумоподавлением и прозрачностью! \n <b>+ Чехол в подарок!</b> \n<b>🔥Цена: 2100₽🔥</b>',
                         parse_mode='html')
        bot.send_message(callback.message.chat.id, '<b>Технические характеристики и комплектация AirPods Pro 2:</b> \n'
                                          '✅СЕНСОРНОЕ УПРАВЛЕНИЕ ГРОМКОСТЬЮ!\n✅ШУМОПОДАВЛЕНИЕ И ПРОЗРАЧНОСТЬ ОТЛИЧНО '
                                                   'РАБОТАЮТ!\n✅ЗВУК 1:1 C ОРИГИНАЛОМ!\n✅ПРОХОДЯТ ПРОВЕРКУ '
                                                   'ПОДЛИННОСТИ НА IOS 16!\n✅гравировка на пленке кейса \n✅гравировка '
                                                   'на кабеле\n✅микрофон оригинал\n✅картонная ванночка\n✅рабочее '
                                                   'пространственное аудио\n✅Серийник пробивается, совпадает в “об '
                                                   'устр-ве”, на коробке, под крышкой кейса!\n✅При нажатии на '
                                                   'серийник высвечивается L/R\n(три ПРАВИЛЬНЫХ серийника)\n✅"S", '
                                                   '"L", "XS" надписи на упаковке амбюшур\n✅Зазор как в оригинале у '
                                                   'крышки кейса \n✅Комплектация, амбюшуры и вкладыш инструкций '
                                                   '1:1\n(Рекомендую! Лучшее, что существует на сегодняшний день из '
                                                   'AirPods Pro 2)',
                        parse_mode='html')
    elif callback.data == 'air1':

        file1 = open('Photos/Airpods pro/ph1.jpg', 'rb')
        file2 = open('Photos/Airpods pro/ph2.jpg', 'rb')
        file3 = open('Photos/Airpods pro/ph3.jpg', 'rb')

        bot.send_photo(callback.message.chat.id, file1)
        bot.send_photo(callback.message.chat.id, file2)
        bot.send_photo(callback.message.chat.id, file3)

        bot.send_message(callback.message.chat.id,
                         '💛AirPods Pro (Lux) 💎\n с шумоподавлением и прозрачностью! \n <b>+ Чехол в подарок!</b> \n<b>🔥Цена: 1700₽🔥</b>',
                         parse_mode='html')
        bot.send_message(callback.message.chat.id, '<b>Технические характеристики и комплектация AirPods Pro:</b> \n'
                                                   '✅ШУМОПОДАВЛЕНИЕ!\n✅РАБОТАЮТ С IOS И ANDROID!\n'
                                                   '✅РАБОТАЕТ БЕЗ ОШИБОК НА IOS 16!\n✅Прозрачность\n'
                                                   '✅Анимация при подключении\n✅ Беспроводная зарядка\n'
                                                   '✅Сенсорное управление наушниками: остановить / воспроизвести / следующий трек\n'
                                                   '✅ Полное внешнее совпадение:\n—Три серийных номера на наушниках, кейсе и коробке\n'
                                                   '—Гравировка Apple California\n—Задняя сторона кейса с тонкой гравировкой\n'
                                                   '—Точные размеры кейса и веса наушников\n✅ Полная оригинальная комплектация:\n'
                                                   '—Наушники Bluetooth AirPods Pro\n—Кабель Lightning - Type C\n—Сменные амбушюры 2 пары\n'
                                                   '—Оригинальные вкладыши-инструкции\n'
                                                   '(Рекомендую! Лучшее, что существует на сегодняшний день из AirPods Pro!)',
                         parse_mode='html')
    elif callback.data == 'air3':

        file1 = open('Photos/Airpods 3/ph1.jpg', 'rb')
        file2 = open('Photos/Airpods 3/ph2.jpg', 'rb')

        bot.send_photo(callback.message.chat.id, file1)
        bot.send_photo(callback.message.chat.id, file2)

        bot.send_message(callback.message.chat.id,
                         '💛AirPods 3 (Lux) 💎\n  <b>+ Чехол в подарок!</b> \n<b>🔥Цена: 1700₽🔥</b>',
                         parse_mode='html')
        bot.send_message(callback.message.chat.id, '<b>Технические характеристики и комплектация AirPods 3:</b> \n'
                                                   '✅ПРОХОДЯТ ПРОВЕРКУ ПОДЛИННОСТИ НА IOS 16!✅ЗВУК 1:1 C '
                                                   'ОРИГИНАЛОМ!\n✅Отличный микрофон\n✅картонная ванночка '
                                                   '\n✅гравировка на пленке кейса\n✅гравировка на '
                                                   'кабеле\n✅пространственное аудио\n✅Серийник совпадает в “об '
                                                   'устр-ве”, на коробке, под крышкой кейса!\n✅При нажатии на '
                                                   'серийник высвечивается L/R\n(три правильных '
                                                   'серийника)\n✅Комплектация и вкладыш инструкций 1:1\n(Рекомендую! '
                                                   'Лучшее, что существует на сегодняшний день из AirPods 3.)',
                         parse_mode='html')
    elif callback.data == 'blok':

        bot.send_message(callback.message.chat.id, 'Про блок Глеб ничего не скинул')
    elif callback.data == 'help':
        bot.send_message(callback.message.chat.id, 'Памагити')
    elif callback.data == 'avito':
        webbrowser.open('https://vk.com/handmanis')
    elif callback.data == 'connect':
        bot.send_message(callback.message.chat.id, 'Ссылка на чат с нашим менеджером\n https://t.me/Tica_fo')


@bot.message_handler(commands=['avito'])
def site(message):
    webbrowser.open('https://vk.com/handmanis')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Help information')


@bot.message_handler(commands=['air1'])
def air1(message):
    file1 = open('Photos/Airpods pro/ph1.jpg', 'rb')
    file2 = open('Photos/Airpods pro/ph2.jpg', 'rb')
    file3 = open('Photos/Airpods pro/ph3.jpg', 'rb')

    bot.send_photo(message.chat.id, file1)
    bot.send_photo(message.chat.id, file2)
    bot.send_photo(message.chat.id, file3)

    bot.send_message(message.chat.id,
                     '💛AirPods Pro (Lux) 💎\n с шумоподавлением и прозрачностью! \n <b>+ Чехол в подарок!</b> \n<b>🔥Цена: 1700₽🔥</b>',
                     parse_mode='html')
    bot.send_message(message.chat.id, '<b>Технические характеристики и комплектация AirPods Pro:</b> \n'
                                               '✅ШУМОПОДАВЛЕНИЕ!\n✅РАБОТАЮТ С IOS И ANDROID!\n'
                                               '✅РАБОТАЕТ БЕЗ ОШИБОК НА IOS 16!\n✅Прозрачность\n'
                                               '✅Анимация при подключении\n✅ Беспроводная зарядка\n'
                                               '✅Сенсорное управление наушниками: остановить / воспроизвести / следующий трек\n'
                                               '✅ Полное внешнее совпадение:\n—Три серийных номера на наушниках, кейсе и коробке\n'
                                               '—Гравировка Apple California\n—Задняя сторона кейса с тонкой гравировкой\n'
                                               '—Точные размеры кейса и веса наушников\n✅ Полная оригинальная комплектация:\n'
                                               '—Наушники Bluetooth AirPods Pro\n—Кабель Lightning - Type C\n—Сменные амбушюры 2 пары\n'
                                               '—Оригинальные вкладыши-инструкции\n'
                                               '(Рекомендую! Лучшее, что существует на сегодняшний день из AirPods Pro!)',
                     parse_mode='html')


@bot.message_handler(commands=['air2'])
def air2(message):
    file1 = open('Photos/Airpods pro 2/ph1.jpg', 'rb')
    file2 = open('Photos/Airpods pro 2/ph2.jpg', 'rb')
    file3 = open('Photos/Airpods pro 2/ph3.jpg', 'rb')

    bot.send_photo(message.chat.id, file1)
    bot.send_photo(message.chat.id, file2)
    bot.send_photo(message.chat.id, file3)

    bot.send_message(message.chat.id,
                     '💛AirPods Pro 2 (Lux) 💎\n с шумоподавлением и прозрачностью! \n <b>+ Чехол в подарок!</b> \n<b>🔥Цена: 2100₽🔥</b>',
                     parse_mode='html')
    bot.send_message(message.chat.id, '<b>Технические характеристики и комплектация AirPods Pro 2:</b> \n'
                                               '✅СЕНСОРНОЕ УПРАВЛЕНИЕ ГРОМКОСТЬЮ!\n✅ШУМОПОДАВЛЕНИЕ И ПРОЗРАЧНОСТЬ ОТЛИЧНО '
                                               'РАБОТАЮТ!\n✅ЗВУК 1:1 C ОРИГИНАЛОМ!\n✅ПРОХОДЯТ ПРОВЕРКУ '
                                               'ПОДЛИННОСТИ НА IOS 16!\n✅гравировка на пленке кейса \n✅гравировка '
                                               'на кабеле\n✅микрофон оригинал\n✅картонная ванночка\n✅рабочее '
                                               'пространственное аудио\n✅Серийник пробивается, совпадает в “об '
                                               'устр-ве”, на коробке, под крышкой кейса!\n✅При нажатии на '
                                               'серийник высвечивается L/R\n(три ПРАВИЛЬНЫХ серийника)\n✅"S", '
                                               '"L", "XS" надписи на упаковке амбюшур\n✅Зазор как в оригинале у '
                                               'крышки кейса \n✅Комплектация, амбюшуры и вкладыш инструкций '
                                               '1:1\n(Рекомендую! Лучшее, что существует на сегодняшний день из '
                                               'AirPods Pro 2)',
                     parse_mode='html')


@bot.message_handler(commands=['air3'])
def air3(message):
    file1 = open('Photos/Airpods 3/ph1.jpg', 'rb')
    file2 = open('Photos/Airpods 3/ph2.jpg', 'rb')

    bot.send_photo(message.chat.id, file1)
    bot.send_photo(message.chat.id, file2)

    bot.send_message(message.chat.id,
                     '💛AirPods 3 (Lux) 💎\n  <b>+ Чехол в подарок!</b> \n<b>🔥Цена: 1700₽🔥</b>',
                     parse_mode='html')
    bot.send_message(message.chat.id, '<b>Технические характеристики и комплектация AirPods 3:</b> \n'
                                               '✅ПРОХОДЯТ ПРОВЕРКУ ПОДЛИННОСТИ НА IOS 16!✅ЗВУК 1:1 C '
                                               'ОРИГИНАЛОМ!\n✅Отличный микрофон\n✅картонная ванночка '
                                               '\n✅гравировка на пленке кейса\n✅гравировка на '
                                               'кабеле\n✅пространственное аудио\n✅Серийник совпадает в “об '
                                               'устр-ве”, на коробке, под крышкой кейса!\n✅При нажатии на '
                                               'серийник высвечивается L/R\n(три правильных '
                                               'серийника)\n✅Комплектация и вкладыш инструкций 1:1\n(Рекомендую! '
                                               'Лучшее, что существует на сегодняшний день из AirPods 3.)',
                     parse_mode='html')


@bot.message_handler(commands=['blok'])
def blok(message):
    bot.send_message(message.chat.id, 'Про блок Глеб ничего не скинул')

@bot.message_handler(commands=['connect'])
def blok(message):
    bot.send_message(message.chat.id, 'Ссылка для связи с нашим менеджером\n https://t.me/Tica_fo')


bot.polling(none_stop=True)
