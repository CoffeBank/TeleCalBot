import sqlite3


class CalendarDataBase:
    sqlite_connection = None
    cursor = None

    _dbPath = './database/REMINDERS.db'

    def init(self):
        self.sqlite_connection = sqlite3.connect(self._dbPath)
        self.cursor = self.sqlite_connection.cursor()

        create_table_query = '''create table if not exists REMINDERS(
            CHATID string,
            ITEM text not null,
            USERNAME text not null
        );
        '''

        self.cursor.execute(create_table_query)
