import datetime
from typing import Optional

from domain.impl.CalendarDataBase import CalendarDataBase


# noinspection PyBroadException
class Repository:
    database = 0

    def __init__(self, database):
        self.database = database
        self.database.init()

    def add_to_list(self, chat_id, username, string, time) -> bool:
        try:
            time_splited = time.split("-")
            time = datetime.date(int(time_splited[0]), int(time_splited[1]), int(time_splited[2]))
            self.database.put(chat_id, username, string, time)
            return True
        except Exception:
            return False

    def remove_from_list(self, chat_id, strings) -> (str, str):
        try:
            err = ""
            result = ""
            for s in strings:
                if self.database.delete(chat_id, s):
                    result += s + "\n"
                else:
                    err += s + "\n"
            return result, err
        except Exception:
            return None

    def show_list(self, chat_id) -> Optional[str]:
        try:
            rows = self.database.select(chat_id)
            if len(rows) > 0:
                return rows
            else:
                return ""
        except Exception:
            return None

    def clear_list(self, chat_id) -> Optional[bool]:
        try:
            return self.database.delete_all(chat_id)
        except Exception:
            return None

"""
x = Repository(CalendarDataBase())
x.add_to_list("1", "q", "w")
print(x.show_list("1"))
"""