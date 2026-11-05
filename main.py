import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 8361368078

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    menu = InlineKeyboardMarkup()
    menu.add(InlineKeyboardButton("📋 Katalogas", callback_data="catalog"))
    menu.add(InlineKeyboardButton("ℹ️ Informacija", callback_data="info"))

    bot.send_message(
        message.chat.id,
        "Sveiki atvykę į Tedzisbot! 👋",
        reply_markup=menu
    )

@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
    if call.data == "catalog":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "Demonstracinis katalogas.")
    elif call.data == "info":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "Tedzisbot informacija.")

bot.infinity_polling()
