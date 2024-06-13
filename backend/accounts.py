import sqlite3
from contextlib import closing

class AccountManager:
    def __init__(self):
        self.db_name = 'backend/database/clients.db'

        # Create the account table if it doesn't exist
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                conn.execute("CREATE TABLE IF NOT EXISTS account (user_id INTEGER PRIMARY KEY, balance FLOAT, transfer_limit INTEGER, flag TEXT)")
                conn.commit()
    
    # Check if an account exists
    def account_check(self, user_id):
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                cursor = conn.execute("SELECT * FROM account WHERE user_id = ?", (user_id,))
                # If account exists
                if cursor.fetchone():
                    return True
                # If account doesn't exist
                else:
                    self.account_init(user_id)
                    return False

    # Initialise account
    def account_init(self, user_id):
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                conn.execute("INSERT INTO account (user_id, balance, transfer_limit, flag) VALUES (?, ?, ?, ?)", (user_id, 100, 50000, "clear"))
                conn.commit()

    # Get account balance
    def account_balance(self, user_id):
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                cursor = conn.execute("SELECT balance FROM account WHERE user_id = ?", (user_id,))
                return cursor.fetchone()[0]