from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

BOT_TOKEN = "8613274805:AAFTtxg-qWu-bFu68EjLOXz2Q7Lo3ymqgMs"


# START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ AI Telegram Bot Online Hai!"
    )


# MESSAGE REPLY
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    reply = f"🤖 Tumne kaha:\n{user_text}"

    await update.message.reply_text(reply)


# MAIN FUNCTION
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("BOT RUNNING...")

    app.run_polling()


if __name__ == "__main__":
    main()
