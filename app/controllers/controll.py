from app.models.models import Database

class BaseController:
    def __init__(self, db_name):
        self.db = Database(db_name)

    def insert(self, table, **kwargs):
        columns = ', '.join(kwargs.keys())
        placeholders = ', '.join(['?'] * len(kwargs))
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.db.execute_query(query, *kwargs.values())

    def update(self, table, condition, **kwargs):
        updates = ', '.join([f"{key} = ?" for key in kwargs])
        query = f"UPDATE {table} SET {updates} WHERE {condition}"
        self.db.execute_query(query, *kwargs.values())

    def select(self, table, condition="1=1"):
        query = f"SELECT * FROM {table} WHERE {condition}"
        return self.db.fetch_query(query)

    def delete(self, table, condition):
        query = f"DELETE FROM {table} WHERE {condition}"
        self.db.execute_query(query)
