import telebot

bot = telebot.TeleBot(token='6332707799:AAHbm-WDEgB03UgRtdHn0MYKioOzClUWE7s')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')


@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, 'Данный чат-бот создан студенткой группы Б9123-01.03.04МЦМ , Пличко Дарьей '
                                      'Дмитриевной')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '/info - информация о создательнице бота')


bot.infinity_polling()
