import sqlite3

from .statistics import StatisticsTracker
stats = StatisticsTracker()

class AccountManager:
    def __init__(self):
        self.db_name = 'backend/database/users.db'

        # Create the account table if it doesn't exist
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                conn.execute("CREATE TABLE IF NOT EXISTS accounts (user_id INTEGER, balance FLOAT, tier INTEGER, flag TEXT)")
                conn.execute("CREATE TABLE IF NOT EXISTS debts (user_id INTEGER, amount FLOAT, interest_Rate FLOAT, timestamp TEXT)")
                conn.execute("CREATE TABLE IF NOT EXISTS properties (user_id, property_id, amount INTEGER)")
                conn.commit()
    
    # Check if an account exists
    def account_check(self, user_id):
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                cursor = conn.execute("SELECT * FROM accounts WHERE user_id = ?", (user_id,))
                conn.commit()
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
                conn.execute("INSERT INTO accounts (user_id, balance, tier, flag) VALUES (?, ?, ?, ?)", (user_id, 100, 1, "clear"))
                conn.commit()

    # Get account balance
    def account_balance(self, user_id):
        self.account_check(user_id)
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                cursor = conn.execute(f"SELECT balance FROM accounts WHERE user_id = {user_id}")
                conn.commit()
                return cursor.fetchone()[0]
    
    # Get tier details
    def account_tier(self, user_id):
        self.account_check(user_id)
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                cursor = conn.execute(f"SELECT tier FROM accounts WHERE user_id = {user_id}")
                conn.commit()
                tier = cursor.fetchone()[0]

                # Check if master account
                if user_id in [0, 1, 2]:
                    data = {"tier": 0,"transfer_limit": 0, "transfer_fee": 0, "debt_limit": 0, "debt_interest": 0}
                    return data
                else:
                    if tier == 1:
                        data = {"tier": 1, "transfer_limit": 2000, "transfer_fee": 0.05, "debt_limit": 10000, "debt_interest": 0.03}
                        return data

    # Transfer account
    def account_transfer(self, user_id, recipient_id, amount, note):
        # Check if exists
        self.account_check(user_id)
        self.account_check(recipient_id)
        # Get balance and tier of user id
        balance = self.account_balance(user_id)
        tier = self.account_tier(user_id)
        # Check if enough balance
        if amount < balance:
            # Can transfer
            if tier["transfer_limit"] == 0 or amount < tier["transfer_limit"]:
                with sqlite3.connect(self.db_name) as conn:
                    with conn:
                        # Perform the transaction
                        conn.execute("UPDATE accounts SET balance = balance - ? WHERE user_id = ?", (amount, user_id))
                        conn.execute("UPDATE accounts SET balance = balance + ? WHERE user_id = ?", (amount, recipient_id))
                        conn.commit()

                        stats.transaction_log(user_id, recipient_id, amount, note)

                return "success"
            # Exceeds transfer limit
            else:
                return "exceed"
        else:
            return "insufficient"
