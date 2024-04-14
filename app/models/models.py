import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name

    def execute_query(self, query, *args):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
        conn.close()

    def fetch_query(self, query, *args):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(query, args)
        rows = cursor.fetchall()
        conn.close()
        return rows
