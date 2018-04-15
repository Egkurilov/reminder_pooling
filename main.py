# main variables
from sqlalchemy.orm import sessionmaker
import migrate
import telebot
import config
import wordbook

bot = telebot.TeleBot(config.TOKEN)
DBSession = sessionmaker(bind=migrate.engine)
session = DBSession()


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, wordbook.HELLO_MESSAE)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def start_handler(message):
    print(message)
    chat_id = message.chat.id
    text = message.text.lower()
    date = message.date
    if 'заметка' in text:
        send_to_base(text_note(text), date, chat_id, type_note(text))
        bot.send_message(chat_id, wordbook.ADD_NOTE)
    elif 'list' or 'список' in text:
        bot.send_message(message.chat.id, wordbook.REMIND_LIST)
        print("zz")
        # for msg in session.query(migrate.Message).filter(migrate.Message.chat_id == chat_id):
        #     for mess in range(msg.id):
        #         print(mess + msg.message)
        #     bot.send_message(message.chat.id, msg.message)
    elif 'помощь' or 'help' in text:
        bot.send_message(message.chat.id, wordbook.COMMAND_LIST)
    elif 'hh' in text:
        print("hh")
    else:
        bot.send_message(message.chat.id, wordbook.ELSE_MESSAGE)


def send_to_base(message_text, message_date, chat_id, type_note):
    new_message = migrate.Message(message=message_text, datetime=message_date, \
                                  chat_id=chat_id, type=type_note)
    session.add(new_message)
    session.commit()

zip()
def text_note(text):
    text_rem = text.split("заметка ")[1]
    return text_rem


def type_note(text):
    type_rem = text.split(" ")[0]
    return type_rem


bot.polling()
# bot.polling(none_stop=True)
