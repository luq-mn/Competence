import sqlite3, os, hashlib

from .statistics import StatisticsTracker
st = StatisticsTracker()

class AccountManager:
    def __init__(self):
        self.db_name = f"{os.getcwd()}/backend/database/accounts.db"

        # Create the account table if it doesn't exist
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                # users table (user_id, access, tier, flag, and xp)
                conn.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, access TEXT, tier TEXT, flag TEXT, xp INTEGER)")
                # security table (user_id, password, lock)
                conn.execute("CREATE TABLE IF NOT EXISTS security (user_id INTEGER PRIMARY KEY, password TEXT, lock BOOLEAN)")
                # settings
                # conn.execute("CREATE TABLE IF NOT EXISTS settings ()")

    # Check if an account exists
    def check_exists(self, user_id):
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                cursor = conn.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
                conn.commit()

                # If account exists
                if cursor.fetchone():
                    return True
                # If account doesn't exist, create account
                else:
                    self.init_account(user_id)
                    return False

    # Initialise account
    def init_account(self, user_id):
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                conn.execute("INSERT INTO users (user_id, flag, tier, access, xp) VALUES (?, ?, ?, ?, ?)", (user_id, "clear", 1, "default", 0))
                conn.execute("INSERT INTO security (user_id, password, lock) VALUES (?, ?, ?)", (user_id, "password", False))
                # conn.execute("INSERT INTO currency (user_id, balance) VALUES (?, ?)", (user_id, 0))
                conn.commit()
                st.event_log("account init", user_id)
                
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
    def toggle_lock(self, user_id, password):
        self.check_exists(user_id)
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                # Check if lock is true/false
                lock = self.check_lock(user_id)

                # Unlock
                if lock == True:
                    check = self.check_password(user_id, password)

                    # Check if password is valid
                    if check == True:
                        conn.execute(f"UPDATE security SET lock = False WHERE user_id = {user_id}")
                        conn.commit()
                        return "unlocked"
                    else:
                        return "wrong password"
                
                # Lock
                else:
                    # Only set new password if entered
                    if password != "":
                        self.set_password(user_id, password)
                    conn.execute(f"UPDATE security SET lock = True WHERE user_id = {user_id}")
                    conn.commit()
                    return "enabled"
    
    # Security - check if locked
    def check_lock(self, user_id):
        self.check_exists(user_id)
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                cursor = conn.execute(f"SELECT lock FROM security WHERE user_id = {user_id}")
                conn.commit()
                lock = cursor.fetchone()[0]

                if lock == True:
                    return True
                else:
                    return False
    
    # Security - check if password is correct
    def check_password(self, user_id, password):
        # Hash password
        password = hashlib.sha512(password.encode())
        password = password.hexdigest()

        self.check_exists(user_id)
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                cursor = conn.execute(f"SELECT password FROM security WHERE user_id = {user_id}")
                conn.commit()
                password_db = cursor.fetchone()[0]

                if password_db == password:
                    return True
                else:
                    return False

    # Security - set password
    def set_password(self, user_id, password):

        if password == "":
            password = "password"

        password = hashlib.sha512(password.encode())
        password = password.hexdigest()

        self.check_exists(user_id)
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                conn.execute(f"UPDATE security SET password = '{password}' WHERE user_id = {user_id}")
                conn.commit()
                return True