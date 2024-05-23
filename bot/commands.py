# Обработчики запросов в БД для бота
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from bot.main_com import repository
from bot.text import ITEMS_ADD, ITEMS_ERROR, REPORT, ERR, ERR_SOLO, LIST_DEL, LIST_ERR, \
                    LOG_INFO_USER_ADD_TO_LIST, LOG_INFO_USER_ADD_TO_LIST_SUC, LOG_INFO_USER_ADD_TO_LIST_BAD, \
                    LOG_INFO_USER_REM_FR_LIST, LOG_INFO_USER_RM_FROM_LIST_SUC, LOG_INFO_USER_RM_FROM_LIST_BAD, \
                    LOG_INFO_USER_SHOW_LIST, LOG_INFO_USER_SHOW_LIST_SUC_AND_LONG, LOG_INFO_USER_SHOW_LIST_EMPTY, \
                    LOG_INFO_USER_CLEAR_LIST, LOG_INFO_USER_CLEAR_LIST_SUC, LOG_INFO_USER_CLEAR_LIST_BAD
from bot.loger import logger

async def add_to_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info(LOG_INFO_USER_ADD_TO_LIST.format(user.username))

    strings = update.message.text.lower().split()

    if len(strings) >= 3:
        strings.remove('/addtolist')

        chat_id = update.message.chat_id
        chat_id = str(chat_id)
        username = update.message.from_user.username

        text = " ".join(strings[:-1])
        date = strings[-1]

        result = repository.add_to_list(chat_id, username, text, date)

        if result:
            logger.info(LOG_INFO_USER_ADD_TO_LIST_SUC.format(user.username, strings))
            await update.message.reply_text(ITEMS_ADD)
        else:
            logger.info(LOG_INFO_USER_ADD_TO_LIST_BAD.format(user.username, strings))
            await update.message.reply_text(ITEMS_ERROR)
    else:
        logger.info(LOG_INFO_USER_ADD_TO_LIST_BAD.format(user.username, strings))
        await update.message.reply_text(ITEMS_ERROR)


async def remove_from_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info(LOG_INFO_USER_REM_FR_LIST.format(user.username))

    strings = update.message.text.lower().split()

    if len(strings) >= 2:
        strings.remove('/rmfromlist')

        chat_id = update.message.chat_id
        chat_id = str(chat_id)

        report = REPORT
        err = ERR

        (reportContent, errContent) = repository.remove_from_list(chat_id, strings)

        logger.info(LOG_INFO_USER_RM_FROM_LIST_SUC.format(user.username, strings))
        await update.message.reply_text(report + reportContent + "\n" + err + errContent)
    else:
        logger.info(LOG_INFO_USER_RM_FROM_LIST_BAD.format(user.username, strings))
        await update.message.reply_text(ITEMS_ERROR)


async def show_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info(LOG_INFO_USER_SHOW_LIST.format(user.username))

    chat_id = update.message.chat_id
    chat_id = str(chat_id)

    result = repository.show_list(chat_id)
    if result is not None:
        username = update.message.from_user.username
        logger.info(LOG_INFO_USER_SHOW_LIST_SUC_AND_LONG.format(username, len(result)))
        await update.message.reply_text(username + " list:\n" + result)
    else:
        username = update.message.from_user.username
        logger.info(LOG_INFO_USER_SHOW_LIST_EMPTY.format(username))
        await update.message.reply_text(ERR_SOLO)


async def clear_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info(LOG_INFO_USER_CLEAR_LIST.format(user.username))
    
    chat_id = update.message.chat_id
    chat_id = str(chat_id)

    if repository.clear_list(chat_id):
        logger.info(LOG_INFO_USER_CLEAR_LIST_SUC.format(user.username))
        await update.message.reply_text(LIST_DEL)
    else:
        logger.info(LOG_INFO_USER_CLEAR_LIST_BAD.format(user.username))
        await update.message.reply_text(LIST_ERR)
