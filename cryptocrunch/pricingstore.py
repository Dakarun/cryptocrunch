import sqlite3
import os

from cryptocrunch.db import get_db, close_db


class PricingStore:
    def __init__(self, table='pricing'):
        self.table = table
        self.conn = get_db()

    @staticmethod
    def generate_insert_statement(record):
        return f"INSERT INTO pricing VALUES ({{','.join(record)}})"

    def insert(self, record):
        query = self.generate_insert_statement(record)
        self.conn.execute(query)
        self.conn.commit()

    def bulk_insert(self, records):
        for record in records:
            query = self.generate_insert_statement(record)
            self.conn.execute(query)
        self.conn.commit()

    def select(self, condition=None):
        pass
