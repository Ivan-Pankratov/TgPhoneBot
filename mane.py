from phone_metods import *
import telebot

phonebook = []

API_TOKEN = '6839222843:AAEST2MYqnaAOIwIzYuodH83bD6AVU8YWYs'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    init_db()
    bot.send_message(message.chat.id, "Справочник инициализирован,\n /help - список команд")

@bot.message_handler(commands=['all'])
def show_all(message):
    try:
        phonebook = look_all()
        res = look_array(phonebook)
        if res == []:
            bot.send_message(message.chat.id, "Список контактов пуст")
        else:
            bot.send_message(message.chat.id, "Список контактов: ")
            bot.send_message(message.chat.id, ", \n".join(res))
    except:
        bot.send_message(message.chat.id, "Возможно, справочник не инициализирован, используйте /start")

@bot.message_handler(commands=['sort'])
def show_sort(message):
    try:
        qq = message.text.split()[1:]
        if qq == []:
            bot.send_message(message.chat.id, "Отсутствуют параметры команды. Попробуйте снова")
        else:
            phonebook = look_sort(qq)
            res = look_array(phonebook)
            if res == []:
                bot.send_message(message.chat.id, "Список контактов пуст")
            else:
                bot.send_message(message.chat.id, "Список контактов: ")
                bot.send_message(message.chat.id, ", \n".join(res))
    except:
        bot.send_message(message.chat.id, "Что-то не получилось. Попробуй иначе.")

@bot.message_handler(commands=['help'])
def show_help(message):
    help_text = print_help()
    try:
        bot.send_message(message.chat.id, "".join(help_text))
    except:
        bot.send_message(message.chat.id, "Что-то не получилось. Попробуй иначе.")

@bot.message_handler(commands=['add'])
def show_add(message):
    qq = message.text.split()[1:]
    if qq == []:
        bot.send_message(message.chat.id, "Отсутствуют параметры команды. Попробуйте снова.")
    elif len(qq)!=4:
        bot.send_message(message.chat.id, "Параметры команды не полные. Попробуйте снова.")
    else:
        look_add(qq)
        bot.send_message(message.chat.id, "Ваш контакт успешно добавлен в справочник")

@bot.message_handler(commands=['delete'])
def show_find(message):
    quest = message.text.split()[1:]
    if quest == []:
        bot.send_message(message.chat.id, "Отсутствуют параметры команды. Попробуйте снова")
    else:

        qq = "".join(quest)
        res = look_surname(qq)
        if res == []:
            bot.send_message(message.chat.id, "Нет контакта с такими данными")
        else:
            look_delete(qq)
            bot.send_message(message.chat.id, "Контакт успешно удалён из справочника")

@bot.message_handler(commands=['find'])
def show_find(message):
    quest = message.text.split()[1:]
    if quest == []:
        bot.send_message(message.chat.id, "Отсутствуют параметры команды. Попробуйте снова")
    else:
        qq = "".join(quest)
        res = look_surname(qq)
        res = look_array(res)
        try:
            if res == []:
                bot.send_message(message.chat.id, "Нет контакта с такими данными")
            else:
                bot.send_message(message.chat.id, "Вот данные, которые вы запросили: ")
                bot.send_message(message.chat.id, ", \n".join(res))
        except:
            bot.send_message(message.chat.id, "Возможно, справочник не инициализирован, используйте /start")

@bot.message_handler(commands=['clear'])
def show_clear(message):
    try:
        look_clear()
        bot.send_message(message.chat.id, "Вы очистили список контактов")
    except:
        bot.send_message(message.chat.id, "Что-то пошло не так.")

@bot.message_handler(commands=['oops'])
def show_oops(message):
    try:
        look_oops()
        bot.send_message(message.chat.id, "Поздравляю: справочника больше нет!")
    except:
        bot.send_message(message.chat.id, "Что-то пошло не так.")

bot.polling()
