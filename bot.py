import os
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

app = Flask(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salut Jojo ! Ton bot BJ JULES est en ligne H24 ✅")

@app.route('/')
def home():
    return "Bot is Live!"

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    main()
