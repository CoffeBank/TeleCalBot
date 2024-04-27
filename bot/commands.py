# Обработчики запросов в БД для бота
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

from domain.impl.Repository import repository
from text import HELLO_TEXT, ITEMS_ADD, ITEMS_ERROR, REPORT, ERR, ERR_SOLO, LIST_DEL, LIST_ERR

async def add_to_list(update: Update, context: ContextTypes.DEFAULT_TYPE):

    strings = update.message.text.lower().split()

    if len(strings) >= 3:
        strings.remove('/addtolist')

        chat_id = update.message.chat_id
        chat_id = str(chat_id)
        username = update.message.from_user.username

        result = repository.add_to_list(chat_id, username, strings)

        if result:
            await update.message.reply_text(ITEMS_ADD)
        else:
            await update.message.reply_text(ITEMS_ERROR)
    else:
        await update.message.reply_text(ITEMS_ERROR)


async def remove_from_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    strings = update.message.text.lower().split()

    if len(strings) >= 3:
        strings.remove('/rmfromlist')

        chat_id = update.message.chat_id
        chat_id = str(chat_id)

        report = REPORT
        err = ERR

        (reportContent, errContent) = repository.remove_from_list(chat_id, strings)

        await update.message.reply_text(report + reportContent + "\n" + err + errContent)
    else:
        await update.message.reply_text(ITEMS_ERROR)


async def show_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    chat_id = str(chat_id)

    result = repository.show_list(chat_id)
    if result is not None:
        username = update.message.from_user.username
        await update.message.reply_text(username + " list:\n" + result)
    else:
        await update.message.reply_text(ERR_SOLO)


async def clear_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    chat_id = str(chat_id)

    if repository.clear_list(chat_id):
        await update.message.reply_text(LIST_DEL)
    else:
        await update.message.reply_text(LIST_ERR)
