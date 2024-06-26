# https://docs.python-telegram-bot.org/en/stable/index.html

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

from bot.config import TOKEN, DEBUG

from bot.main_com import start, help_command
from bot.commands import add_to_list, remove_from_list, show_list, clear_list
from bot.debug_com import bad_command
from bot.loger import logger, error_handler


if __name__ == '__main__':

    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(CommandHandler('addtolist', add_to_list))
    application.add_handler(CommandHandler('rmfromlist', remove_from_list))
    application.add_handler(CommandHandler('show_list', show_list))
    application.add_handler(CommandHandler('clear_list', clear_list))

    #application.add_handler(CommandHandler('about', about))

    if DEBUG:
        application.add_handler(CommandHandler("bad_command", bad_command))
    
    application.add_error_handler(error_handler)
    
    application.run_polling()
