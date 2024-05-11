from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

async def bad_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.wrong_method_name()