import os
import telebot
TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "Bot BJ Jules actif H24 ✅")

@bot.message_handler(func=lambda m: True)
def echo(m):
    bot.reply_to(m, f"Reçu: {m.text}")

bot.infinity_polling()
