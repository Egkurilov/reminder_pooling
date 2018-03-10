# main variables
from sqlalchemy.orm import sessionmaker
import migrate
import telebot

TOKEN = "*"
bot = telebot.TeleBot(TOKEN)
DBSession = sessionmaker(bind=migrate.engine)
session = DBSession()


# handlers
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, когда я вырасту, Я буду напоминать тебе о не завершенных делах :)')
    bot.send_message(message.chat.id, 'Для того что бы добавить новую заметку напиши "заметка"')


@bot.message_handler(commands=['лист', 'list'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Список заметок')


@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    date = message.date
    if 'заметка' in text:
        bot.send_message(chat_id, 'Заметка добавлена.')
        send_to_base(text_note(text), date, chat_id, type_note(text))
    else:
        bot.send_message(chat_id, 'Простите, я вас не понял :(')


@bot.message_handler(content_types=['photo'])
def text_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Красиво.')


def send_to_base(mesasge_text, message_date, chat_id, type_note):
    new_message = migrate.Message(message=mesasge_text, datetime=message_date, \
                                  chat_id=chat_id, type=type_note)
    session.add(new_message)
    session.commit()


def text_note(text):
    text_rem = text.split("заметка ")[1]
    return text_rem


def type_note(text):
    type_rem = text.split(" ")[0]
    return type_rem


bot.polling()
# bot.polling(none_stop=True)