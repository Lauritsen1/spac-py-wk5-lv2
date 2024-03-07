import mysql.connector

from utils import SingletonMeta

class Connection(metaclass=SingletonMeta):
    _db = None

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self._connect()

    def _connect(self):
        try:
            self._db = mysql.connector.connect(host=self.host, user=self.user, password=self.password)
            print(f'Successfully established connection to {self.host} as {self.user}.')
        except mysql.connector.Error as err:
            print(f'Error: {err.msg}')

    def close(self):
        if self._db is not None:
            try:
                self._db.close()
                print(f'Successfully closed connection to {self.host}.')
            except mysql.connector.Error as err:
                print(f"Error: {err.msg}")
            finally:
                self._db = None
        else:
            print(f"Failed closing connection to {self.host}. Connection already closed or never established.")