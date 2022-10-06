# Создайте программу для игры с конфетами человек против бота(интелект).

from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random

bot = Bot(token='5690369723:AAGFmz-mUi6sekH2fj3qeWoFLfd6S7rrMsc')
updater = Updater(token='5690369723:AAGFmz-mUi6sekH2fj3qeWoFLfd6S7rrMsc')
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Игра в конфеты. На столе лежат 2021 конфет. Можно взять от 1 до 28 конфет.')
    turn = int(random.randint(0, 1))
    candies = 2021
    max_grap = 28
    count1 = 0
    count2 = 0
    while candies > 0:
        if turn == 0:
            turn, candies, count1 = turn_user(update, context, max_grap, turn, count1, candies)
        elif turn == 1:
            turn, candies, count2 = turn_bot(update, context, max_grap, turn, count2, candies)
    win(update, context, candies, turn, count2, count1)

def turn_bot(update, context, max_grap, turn, count2, candies):
    if max_grap < candies <= max_grap + max_grap + 1 + 1:
        i = candies - (max_grap + 1)
        bot = i
        candies = candies - bot
        count2 = count2 + bot
        context.bot.send_message(update.effective_chat.id, f'Бот: я возьму {bot} конфет')
        context.bot.send_message(update.effective_chat.id, f'Осталось {candies} конфет')
        turn = 0
    elif max_grap + max_grap + 1 + 1 < candies <= max_grap + max_grap + max_grap + 1:
        i = candies - (max_grap + 1) - (max_grap + 1)
        bot = i
        candies = candies - bot
        count2 = count2 + bot
        context.bot.send_message(update.effective_chat.id, f'Бот: я возьму {bot} конфет')
        context.bot.send_message(update.effective_chat.id, f'Осталось {candies} конфет')
        turn = 0
    elif 0 < candies <= max_grap:
        bot = candies
        candies = candies - bot
        count2 = count2 + bot
        context.bot.send_message(update.effective_chat.id, f'Бот: я возьму {bot} конфет')
        context.bot.send_message(update.effective_chat.id, f'Осталось {candies} конфет')
        turn = 0
    else:
        bot = max_grap
        candies = candies - bot
        count2 = count2 + bot
        context.bot.send_message(update.effective_chat.id, f'Бот: я возьму {bot} конфет')
        context.bot.send_message(update.effective_chat.id, f'Осталось {candies} конфет')
        turn = 0
    return turn, candies, count2

def turn_user(update, context, max_grap, turn, count1, candies):
    context.bot.send_message(update.effective_chat.id, 'Ваш ход. Сколько возьмете конфет?')
    first = int(update.message.text)
    context.bot.send_message(update.effective_chat.id, f'{first}')
    if first > max_grap or first <= 0:
        while first > max_grap or first < 0:
            context.bot.send_message(update.effective_chat.id, 'Введенно неверное значение! Повторите попытку')
            context.bot.send_message(update.effective_chat.id, 'Ваш ход. Сколько возьмете конфет?')
            first = int(update.message.text)
    candies = candies - first
    count1 = count1 + first
    context.bot.send_message(update.effective_chat.id, f'Осталось {candies} конфет!')
    turn = 1
    return turn, candies, count1

def win(update, context, candies, turn, count2, count1):
    if candies == 0 and turn == 0:
        context.bot.send_message(update.effective_chat.id, f'Бот: Я победил!!! Итого собрано {count2} конфет для победы!')
    elif candies == 0 and turn == 1:
        context.bot.send_message(update.effective_chat.id, f'Вы победили!!! Итого собрано {count1} конфет для победы!')

def exit(update, context):
    context.bot.send_message(update.effective_chat.id, 'Конец!')

start_handler = CommandHandler('start', start)
text_handler = MessageHandler(Filters.text, turn_user)
cancel_handler = CommandHandler('exit', exit)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(text_handler)
dispatcher.add_handler(cancel_handler)



updater.start_polling()
updater.idle()
