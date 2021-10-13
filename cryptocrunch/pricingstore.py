import sqlite3


class KeyValueStore:
    def __init__(self, database):
        self.conn = sqlite3.connect(database)

    def create_table(self):
        pass

    def insert(self, record):
        pass

    def select(self):
        pass
