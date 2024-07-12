# TeleCalBot

TeleCalBot is a Telegram bot designed to help you manage your daily tasks with ease. You can create, view, and delete tasks with specific dates.

## Key Features

- Create daily tasks with a specific date
- View all your tasks
- Delete tasks

## Library

- `python-telegram-bot`
- `sqlite3`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/CoffeBank/TeleCalBot.git
   ```

2. Navigate to the project directory:
  ```bash
  cd TeleCalBot
  ```

3. Install the dependencies:
  ```bash
  pip install -r requirements.txt
  ```

4. Configuration in config.py:
  ```text
    TOKEN = string  # Get your token from BotFather
    DEBUG = bool  # Turn on/off debug mode
    DEVELOPER_CHAT_ID = string  # Chat ID for alarm messages/bug reports
  ```

6. Usage
  ```bash
  python main.py
  ```
Feedback
If you have any questions or suggestions, please open an issue on the Issues page!
