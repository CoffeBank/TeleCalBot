# Обработчики для основных команд бота
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from bot.text import HELLO_TEXT, ITEMS_ADD, ITEMS_ERROR, REPORT, ERR, ERR_SOLO, LIST_DEL, LIST_ERR
from domain.impl.CalendarDataBase import CalendarDataBase
from domain.impl.Repository import Repository

repository = Repository(CalendarDataBase())

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=HELLO_TEXT)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Используй /start для запуска :) \n"
        "addtolist \n"
        "rmfromlist \n"
        "show_list \n"
        "clear_list \n"
    )