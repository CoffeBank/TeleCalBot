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
        "Привет! Вот список команд, которые ты можешь использовать:\n\n"
    
        "**Основные команды**\n"
        "/start - запуск бота\n"
    
        "**Работа с календарем**\n"
        "/addtolist [цель] [время] - добавить событие в список\n"
        "/rmfromlist [цель] - удалить событие из списка\n"
        "/show_list - показать все события в списке\n"
        "/clear_list - очистить весь список\n"
    
        "**Прочие команды**\n"
        "/help - показать это сообщение\n"
        "/about - информация о боте\n"
    )