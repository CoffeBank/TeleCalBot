from typing import Optional


# noinspection PyBroadException
class Repository:
    database = 0
    cursor = 0

    def __init__(self, database):
        self.database = database
        self.database.init()
        self.cursor = database.cursor

    def add_to_list(self, chat_id, username, strings) -> bool:
        try:
            for s in strings:
                (self.cursor.execute(
                    "INSERT INTO REMINDERS VALUES("
                    "'" + chat_id + "','" + s + "','" + username +
                    "')"))
            return True
        except Exception:
            return False

    def remove_from_list(self, chat_id, strings) -> (str, str):
        try:
            err = ""
            result = ""
            for s in strings:
                rc = self.cursor.execute(
                    "DELETE FROM REMINDERS WHERE CHATID='" + chat_id + "' AND ITEM='" + s + "'").rowcount
                if rc <= 0:
                    err += s + "\n"
                else:
                    result += s + "\n"
            return result, err
        except Exception:
            return None

    def show_list(self, chat_id) -> Optional[str]:
        try:
            self.cursor.execute("SELECT ITEM FROM REMINDERS WHERE CHATID='" + chat_id + "'")
            rows = self.cursor.fetchall()
            if len(rows) > 0:
                items = ""
                for row in rows:
                    items += row[0] + "\n"
                return items
            else:
                return ""
        except Exception:
            return None

    def clear_list(self, chat_id) -> Optional[bool]:
        try:
            if self.cursor.execute("DELETE FROM REMINDERS WHERE CHATID='" + chat_id + "'").rowcount > 0:
                self.cursor.commit()
                return True
            else:
                return False
        except Exception:
            return None
