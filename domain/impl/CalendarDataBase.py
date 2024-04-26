import sqlite3


class CalendarDataBase:

    sqlite_connection = None
    cursor = None

    _dbPath = "../database/Calendar.db"

    def init(self):
        self.sqlite_connection = sqlite3.connect(self._dbPath)
        self.cursor = self.sqlite_connection.cursor()

        create_table_query = '''create table Calendar(
            id integer primary key,
            name text not null,
            time text not null
        );
        '''

        self.cursor.execute(create_table_query)
