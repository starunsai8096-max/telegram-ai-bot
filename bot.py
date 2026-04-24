from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"


def ai_reply(text):
    text = text.lower()

    if "hi" in text or "hello" in text:
        return "Hello 👋 I am your 24/7 bot!"
    elif "how are you" in text:
        return "I am good 😊"
    else:
        return "You said: " + text


async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message:
        return

    msg = update.message.text
    reply = ai_reply(msg)

    await update.message.reply_text(reply)


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

    print("Bot running...")

    app.run_polling()


if __name__ == "__main__":
    main()