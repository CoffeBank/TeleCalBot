# Обработчики команд бота
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from text import HELLO_TEXT

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=HELLO_TEXT)