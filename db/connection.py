from utils import SingletonMeta

import mysql.connector

class Connection(metaclass=SingletonMeta):
    _db = None

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

        try:
            self._db = mysql.connector.connect(host=self.host, user=self.user, password=self.password)
            print('Connection made')
        except:
            print('Connection failed')

    def close(self):
        self._db.close()
        print('Connection to server closed')