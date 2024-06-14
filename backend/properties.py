import sqlite3

# from main import get_datetime

class PropertiesManager:
    def __init__(self):
        self.db_name = "backend/database/economy.db"

        with sqlite3.connect(self.db_name) as conn:
            with conn:
                conn.execute("CREATE TABLE IF NOT EXISTS properties (property_id TEXT PRIMARY KEY, name TEXT, description TEXT, price FLOAT, rent FLOAT)")
                conn.commit()

pm = PropertiesManager()