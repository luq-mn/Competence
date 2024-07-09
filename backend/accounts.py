import sqlite3, os

from .statistics import StatisticsTracker
stats = StatisticsTracker()

class AccountManager:
    def __init__(self):
        self.db_name = f"{os.getcwd()}/backend/database/accounts.db"

        # Create the account table if it doesn't exist
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                conn.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, flag TEXT, tier TEXT, access TEXT, xp INTEGER)")
                conn.execute("CREATE TABLE IF NOT EXISTS currency (user_id INTEGER PRIMARY KEY, balance FLOAT)")
                conn.execute("CREATE TABLE IF NOT EXISTS security (user_id INTEGER PRIMARY KEY, password TEXT, lock BOOLEAN DEFAULT FALSE)")
                conn.commit()

    # Check if an account exists
    def check_exists(self, user_id):
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                cursor = conn.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
                conn.commit()

                # If account exists
                if cursor.fetchone():
                    return True
                # If account doesn't exist
                else:
                    self.init(user_id)
                    return False

    # Initialise account
    def init(self, user_id):
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                conn.execute("INSERT INTO users (user_id, flag, tier, access, xp) VALUES (?, ?, ?, ?, ?, ?)", (user_id, "clear", 1, "default", 0))
                conn.execute("INSERT INTO currency (user_id, balance) VALUES (?, ?)", (user_id, 0))
                conn.commit()
                return True

    # Get account data
    def get_data(self, user_id):
        self.check_exists(user_id)
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                cursor = conn.execute(f"SELECT * FROM user WHERE user_id = {user_id}")
                conn.commit()
                return cursor.fetchone()[0]

    # Get account balance
    def get_balance(self, user_id):
        self.account_check(user_id)
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                cursor = conn.execute(f"SELECT balance FROM currency WHERE user_id = {user_id}")
                conn.commit()
                return cursor.fetchone()[0]
    
    # Security - toggle locking of account
    def toggle_lock(self, user_id):
        self.check_exists(user_id)
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                # Check if lock is true/false
                lock = self.check_lock(user_id)

                # Toggle lock
                if lock == True:
                    conn.execute(f"UPDATE users SET lock = False WHERE user_id = {user_id}")
                    conn.commit()
                    return "unlocked"
                else:
                    conn.execute(f"UPDATE users SET lock = True WHERE user_id = {user_id}")
                    conn.commit()
                    return "locked"
    
    # Security - check if locked
    def check_lock(self, user_id):
        self.check_exists(user_id)
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                cursor = conn.execute(f"SELECT lock FROM users WHERE user_id = {user_id}")
                conn.commit()
                lock = cursor.fetchone()[0]

                if lock == True:
                    return True
                else:
                    return False
    
    # Security - check if password is correct

    # Security - set password