# -*- coding: utf-8 -*-

import telebot
from telebot import types

bot = telebot.TeleBot("1102385682:AAGIceYLadoGq-yHSEu_IcCNrlkPef_It-8")


@bot.message_handler(content_types=["text"])
def any_msg(message):
    # Создаем клавиатуру и каждую из кнопок (по 2 в ряд)
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    url_button = types.InlineKeyboardButton(text="ADRES", adres="https://yandex.ru/maps/76/khabarovsk/house/ulitsa_ordzhonikidze_21a/ZUoDaAdkTUIHW0Jua2J1eHlnYQg=/?ll=135.047553%2C48.495029&z=17.06")
    callback_button = types.InlineKeyboardButton(text="OTSOSU", otsosu ="test")
    switch_button = types.InlineKeyboardButton(text="SK 0,5 - 1500", switch_inline_query="Telegram")
    keyboard.add(url_button, callback_button, switch_button)
    bot.send_message(message.chat.id, "Я – Лёша эльф скоростушник", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "test":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="кому отсосать?")
            # Уведомление в верхней части экрана
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="сосу за ск")
    # Если сообщение из инлайн-режима
    elif call.inline_message_id:
        if call.data == "test":
            bot.edit_message_text(inline_message_id=call.inline_message_id, text="я барыга")


# Простейший инлайн-хэндлер для ненулевых запросов
@bot.inline_handler(lambda query: len(query.query) > 0)
def query_text(query):
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="test"))
    results = []
    # Обратите внимание: вместо текста - объект input_message_content c текстом!
    single_msg = types.InlineQueryResultArticle(
        id="1", title="Press me",
        input_message_content=types.InputTextMessageContent(message_text="Я – сообщение из инлайн-режима"),
        reply_markup=kb
    )
    results.append(single_msg)
    bot.answer_inline_query(query.id, results)


if __name__ == '__main__':
    bot.infinity_polling()
