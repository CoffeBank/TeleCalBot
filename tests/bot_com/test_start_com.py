import pytest
from unittest.mock import AsyncMock
from bot.main_com import start
from bot.text import HELLO_TEXT

# Mocks
class MockUser:
    def __init__(self, id):
        self.id = id

class MockChat:
    def __init__(self, id):
        self.id = id

class MockBot:
    async def send_message(self, chat_id, text):
        pass


@pytest.mark.asyncio
async def test_start_function():
    update_mock = AsyncMock()
    context_mock = AsyncMock()
    context_mock.bot = AsyncMock()
    update_mock.effective_user = MockUser(932872542)
    update_mock.effective_chat = MockChat(123)
    update_mock.message.text = "/start"

    await start(update_mock, context_mock)

    context_mock.bot.send_message.assert_called_once_with(
        chat_id=123,
        text=HELLO_TEXT)