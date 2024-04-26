# Обработчики запросов в БД для бота
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from text import HELLO_TEXT, ITEMS_ADD, ITEMS_ERROR, REPORT, ERR, ERR_SOLO, LIST_DEL, LIST_ERR

async def add_to_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #await context.bot.send_message(chat_id=update.effective_chat.id, text="Выполняю запрос")

    strings = update.message.text.lower().split()

    if len(strings) >= 3:
        strings.remove('/addtolist')

        # Connecting to the SQL database
        #conn = sqlite3.connect('../database/list.db')
        #c = conn.cursor()

        chat_id = update.message.chat_id
        chat_id = str(chat_id)
        username = update.message.from_user.username

        #for s in strings:
        #    c.execute("INSERT INTO REMINDERS VALUES('" + chat_id + "','" + s + "','" + username + "')")

        #conn.commit()
        #conn.close()

        await update.message.reply_text(ITEMS_ADD)
    else:
        await update.message.reply_text(ITEMS_ERROR)


async def remove_from_list(update: Update, context: ContextTypes.DEFAULT_TYPE):

    strings = update.message.text.lower().split()

    if len(strings) >= 3:
        strings.remove('/rmfromlist')

        # Connecting to the SQL database
        #conn = sqlite3.connect('../database/list.db')
        #c = conn.cursor()

        chat_id = update.message.chat_id
        chat_id = str(chat_id)

        report = REPORT
        err = ERR

        #for s in strings:
        #    rc = c.execute("DELETE FROM REMINDERS WHERE CHATID='"+chat_id+"' AND ITEM='"+s+"'").rowcount
        #    if rc <= 0:
        #        err += s + "\n"
        #    else:
        #        report += s + "\n"

        #conn.commit()
        #conn.close()

        await update.message.reply_text(report + err)
    else:
        await update.message.reply_text(ITEMS_ERROR)


async def show_list(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # Connecting to the SQL database
    #conn = sqlite3.connect('../database/list.db')
    #c = conn.cursor()

    chat_id = update.message.chat_id
    chat_id = str(chat_id)

    #c.execute("SELECT ITEM FROM REMINDERS WHERE CHATID='" + chat_id + "'")
    #rows = c.fetchall()
    #conn.close()
    #if len(rows) > 0:
    #    items = ""
    #    for row in rows:
    #        items += row[0] + "\n"

    #    username = update.message.from_user.username
    #    await update.message.reply_text(username + " list:\n" + items)
    #else:
    #   await update.message.reply_text(ERR_SOLO)


async def clear_list(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # Connecting to the SQL database
    #conn = sqlite3.connect('../database/list.db')
    #c = conn.cursor()

    chat_id = update.message.chat_id
    chat_id = str(chat_id)

    #if c.execute("DELETE FROM REMINDERS WHERE CHATID='" + chat_id + "'").rowcount > 0:
    #    conn.commit()
    #    await update.message.reply_text(LIST_DEL)
    #else:
    #    await update.message.reply_text(LIST_ERR)

    #conn.close()