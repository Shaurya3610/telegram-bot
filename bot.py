from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

TOKEN = os.environ.get("TOKEN")

async def handle_poll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.poll:
        poll = update.message.poll
        await update.message.reply_poll(
            question="Edited: " + poll.question,
            options=[o.text for o in poll.options],
            type="quiz",
            correct_option_id=0
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.POLL, handle_poll))

print("Bot Running...")
app.run_polling()
