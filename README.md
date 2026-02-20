import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("8242054150:AAGABV7UnUYRlo172XRI5dJJI9dJJBuQKRs")

async def handle_poll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    poll = update.message.poll

    if poll.type != "quiz":
        await update.message.reply_text("Only quiz poll allowed")
        return

    await update.message.reply_poll(
        question="New Poll Name",
        options=[o.text for o in poll.options],
        type="quiz",
        correct_option_id=poll.correct_option_id
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.POLL, handle_poll))
app.run_polling()
