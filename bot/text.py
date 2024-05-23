# Тексты команд

HELLO_TEXT = "Телекал бот включен!"
ITEMS_ADD = "Заметка добавлена!"
ITEMS_ERROR = "Ошибка синтаксиса. Попробуй /help"
REPORT = "Удаленные элементы:\n"
ERR_SOLO = "Не обнаружено элементов"
ERR = "Не обнаружены:\n"
LIST_DEL = "Список удален"
LIST_ERR = "Нечего удалять"

LOG_INFO_USER_START = "User {} started the conversation"
LOG_INFO_USER_HELP = "User {} called /help"
LOG_INFO_USER_ADD_TO_LIST = "User {} called /addtolist"
LOG_INFO_USER_REM_FR_LIST = "User {} called /rmfromlist"
LOG_INFO_USER_SHOW_LIST = "User {} called /show_list"
LOG_INFO_USER_CLEAR_LIST = "User {} called /clear_list"


LOG_INFO_USER_ADD_TO_LIST_SUC = "User {} add item in list {}"
LOG_INFO_USER_ADD_TO_LIST_BAD = "User {} did not add item in list {}"
LOG_INFO_USER_RM_FROM_LIST_SUC = "User {} remove from list {}"
LOG_INFO_USER_RM_FROM_LIST_BAD = "User {} did not remove from list {}"
LOG_INFO_USER_SHOW_LIST_SUC_AND_LONG = "User {} received from showlist items len {}"
LOG_INFO_USER_SHOW_LIST_EMPTY = "User {} received from showlist zero items"
LOG_INFO_USER_CLEAR_LIST_SUC = "User {} cleared list"
LOG_INFO_USER_CLEAR_LIST_BAD = "User {} did not cleared list"


HELP_INFO = (
        "Привет! Вот список команд, которые ты можешь использовать:\n\n"
    
        "**Основные команды**\n"
        "/start - запуск бота\n"
    
        "**Работа с календарем**\n"
        "/addtolist [цель] [время] - добавить событие в список. Время в формате YYYY-MM-DD\n"
        "/rmfromlist [цель] - удалить событие из списка\n"
        "/show_list - показать все события в списке\n"
        "/clear_list - очистить весь список\n"
    
        "**Прочие команды**\n"
        "/help - показать это сообщение\n"
        "/about - информация о боте\n"
)