from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from bot.loger import logger

async def bad_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    logger.info("Call bad com from user {}".format(user.username))
    await context.bot.wrong_method_name()