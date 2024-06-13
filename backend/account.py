import sqlite3
from contextlib import closing

class AccountManager:
    def __init__(self):
        self.conn = sqlite3.connect('backend/database/account.db')

        with closing(self.conn) as conn:
            with conn:
                conn.execute("CREATE TABLE IF NOT EXISTS account (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
                conn.commit()

am = AccountManager()