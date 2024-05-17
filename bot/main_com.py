# Обработчики для основных команд бота
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from bot.text import HELLO_TEXT, LOG_INFO_USER_START, LOG_INFO_USER_HELP, HELP_INFO
from domain.impl.CalendarDataBase import CalendarDataBase
from domain.impl.Repository import Repository
from bot.loger import logger

repository = Repository(CalendarDataBase())

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info(LOG_INFO_USER_START.format(user.username))
    await context.bot.send_message(chat_id=update.effective_chat.id, text=HELLO_TEXT)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    logger.info(LOG_INFO_USER_HELP.format(user.username))
    await update.message.reply_text(HELP_INFO)