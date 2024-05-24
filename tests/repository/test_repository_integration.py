import asyncio
import unittest

from bot.commands import add_to_list, show_list, remove_from_list
from bot.main_com import repository


class Test_Repository(unittest.TestCase):

    def test_commands_work_with_repository(self):
        username = "username1"
        chat_id = 1231

        repository.clear_list(1231)

        update = Test_Update(Test_Message("/addtolist hello 2024-03-02", username, chat_id))
        asyncio.run(add_to_list(update, None))
        self.assertEqual(update.message.reply, "Заметка добавлена!")

        update = Test_Update(Test_Message("/show_list", username, chat_id))
        asyncio.run(show_list(update, None))
        self.assertEqual(update.message.reply, "username1 list:\nhello (2024-03-02)\n")

        update = Test_Update(Test_Message("/rmfromlist hello", username, chat_id))
        asyncio.run(remove_from_list(update, None))
        self.assertEqual(update.message.reply, "Удаленные элементы:\nhello\n\nНе обнаружены:\n")

        update = Test_Update(Test_Message("/show_list", username, chat_id))
        asyncio.run(show_list(update, None))
        self.assertTrue(update.message.reply, "")


class Test_User:
    username = None

    def __init__(self, username):
        self.username = username


class Test_Message:
    text = None
    from_user = None
    chat_id = None

    reply = None

    def __init__(self, text, username, chat_id):
        self.text = text
        self.from_user = Test_User(username)
        self.chat_id = chat_id

    async def reply_text(self, text):
        self.reply = text


class Test_Update:
    message = None

    def __init__(self, message: Test_Message):
        self.message = message
