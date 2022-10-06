# Напишите бота, удаляющего из текста все слова, 
# содержащие "абв". (текст вводит пользователь)

from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='5690369723:AAGFmz-mUi6sekH2fj3qeWoFLfd6S7rrMsc')
updater = Updater(token='5690369723:AAGFmz-mUi6sekH2fj3qeWoFLfd6S7rrMsc')
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите текст и я удалю из него все абв!')
    
def text_input(update, context):
    text = update.message.text
    if 'абв' in text.lower():
        context.bot.send_message(update.effective_chat.id, ' '.join(list(filter(lambda x: 'абв' not in x.lower(), text.split()))))
    else:
        context.bot.send_messege(update.effective_chat.id, f'Здесь нечего удалять!/n{text}')

start_handler = CommandHandler('start', start)
text_handler = MessageHandler(Filters.text, text_input)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(text_handler)

updater.start_polling()
updater.idle()
