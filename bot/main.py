#https://docs.python-telegram-bot.org/en/stable/index.html

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

from config import TOKEN
from main_com import start, help_command
from commands import add_to_list, remove_from_list, show_list, clear_list

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(CommandHandler('addtolist', add_to_list))
    application.add_handler(CommandHandler('rmfromlist', remove_from_list))
    application.add_handler(CommandHandler('show_list', show_list))
    application.add_handler(CommandHandler('clear_list', clear_list))

    #application.add_handler(CommandHandler('about', about))
    
    application.run_polling()