from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from django.conf import settings

print("Бот запущен. Нажмите Ctrl+C для завершения")

# Подключаем базу
import sqlite3
conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
cursor = conn.cursor()

def db_table_val(user_id: int, name: str, user_name: str, tel: str):
    cursor.execute('INSERT INTO app_for_bot (user_id, name, '
                       'user_name, tel) VALUES (?, ?, ?, ?)', (user_id, name, user_name, tel))
    conn.commit()

def on_start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Привет")
    context.bot.send_message(chat_id=chat.id, text='Ваше имя добавлено в базу данных')
    us_id = update.message.from_user.id
    us_name = update.message.from_user.first_name
    us_sname = update.message.from_user.last_name
    username = update.message.from_user.username
    tel_n = " "
    db_table_val(user_id=us_id, name=us_name + ' ' + us_sname, user_name=username, tel=tel_n)

def on_phone(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Введите номер телефона")

def on_message (update, context):
        us_id = update.message.from_user.id
        us_name = update.message.from_user.first_name
        us_sname = update.message.from_user.last_name
        username = update.message.from_user.username
        tel_n = update.message.text
        db_table_val(user_id=us_id, name=us_name + ' ' + us_sname, user_name=username, tel=tel_n)
        chat = update.effective_chat
        context.bot.send_message(chat_id=chat.id, text='Ваш телефон добавлен в базу данных')

updater = Updater(settings.BOT_TOKEN)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", on_start))
dispatcher.add_handler(CommandHandler("set_phone", on_phone))
dispatcher.add_handler(MessageHandler(Filters.all, on_message))

updater.start_polling()
updater.idle()