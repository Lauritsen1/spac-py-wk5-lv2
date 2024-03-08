import sqlite3

from utils import SingletonMeta

class Connection(metaclass=SingletonMeta):
    _connection = None
    _cursor = None

    def __init__(self):
        self._connect()
        self._init_db()

    def __enter__(self):
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def _init_db(self):
        try:
            self._cursor.execute('CREATE TABLE products (id TEXT, name TEXT, category TEXT, price INTEGER, created_at TEXT)')
        except self._connection.Error as err:
            pass

    def _connect(self):
        try:
            self._connection = sqlite3.connect('./db/inventory.db')
            self._cursor = self._connection.cursor()
        except self._connection.Error as err:
            pass

    def close(self):
        try:
            self._connection.close()
        except self._connection.Error as err:
            pass