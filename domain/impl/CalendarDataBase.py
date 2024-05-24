import sqlite3
from typing import Optional


class CalendarDataBase:
    sqlite_connection = None
    cursor = None

    _dbPath = 'REMINDERS.db'

    def init(self):
        self.sqlite_connection = sqlite3.connect(self._dbPath)
        self.cursor = self.sqlite_connection.cursor()
        create_table_query = '''create table if not exists REMINDERS(
            CHATID string,
            ITEM text not null,
            USERNAME text not null,
            AT_TIME timestamp not null
        );
        '''
        self.cursor.execute(create_table_query)
        self.sqlite_connection.commit()

    def put(self, chat_id, username, string, date):
        self.cursor.execute(
            "INSERT INTO REMINDERS VALUES(?, ?, ?, ?);",
            (chat_id, string, username, date)
        )
        self.sqlite_connection.commit()

    def delete(self, chat_id, string) -> bool:
        result = (self
                  .cursor
                  .execute("DELETE FROM REMINDERS WHERE CHATID='" + chat_id + "' AND ITEM='" + string + "'").rowcount)
        if result <= 0:
            return False
        else:
            return True

    def select(self, chat_id) -> Optional[str]:
        self.cursor.execute("SELECT ITEM, AT_TIME FROM REMINDERS WHERE CHATID='" + chat_id + "'")
        rows = self.cursor.fetchall()
        if len(rows) > 0:
            items = ""
            for row in rows:
                items += row[0] + " (" + row[1] + ")\n"
            return items
        else:
            return ""

    def delete_all(self, chat_id) -> Optional[bool]:
        if self.cursor.execute("DELETE FROM REMINDERS WHERE CHATID='" + str(chat_id) + "'").rowcount > 0:
            self.sqlite_connection.commit()
            return True
        else:
            return False
