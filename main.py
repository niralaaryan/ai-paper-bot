from telegram.ext import Application, CommandHandler
import os

BOT_TOKEN = os.getenv("8924341818:AAHw7lhFd2ubSwYJOZYo03VJT3uHvEvgKvM")

async def start(update, context):
    await update.message.reply_text("Bot running successfully!")

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("BOT STARTED...")

app.run_polling()
