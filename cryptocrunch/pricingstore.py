import sqlite3


class PricingStore:
    # TODO: Use a proper model
    # TODO: Use flask config and app context
    def __init__(self, table='pricing'):
        self.table = table
        self.conn = sqlite3.connect('instance/cryptocrunch.db',
                                    detect_types=sqlite3.PARSE_DECLTYPES,
                                    check_same_thread=False
                                    )

    def get_insert_statement(self, values):
        return f"INSERT INTO {self.table} VALUES ({values})"

    def insert(self, records):
        # TODO: Handle exceptions and retry/dead letter queue failures
        insert_statement = f"INSERT INTO {self.table} VALUES (?, ?, ?, ?, ?)"
        self.conn.executemany(insert_statement, records)
        self.conn.commit()

    def select(self, condition=None):
        # TODO: Implementation
        pass
