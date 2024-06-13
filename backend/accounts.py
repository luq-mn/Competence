import sqlite3, os, datetime
from .transactions import TransactionsTracker

class AccountManager:
    def __init__(self):
        self.tt = TransactionsTracker()

        # Initialize database connection
        self.connection_open()

        # Create table (if not exists)
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                user_id TEXT PRIMARY KEY,
                balance INTEGER,
                transfer_limit INTEGER,
                transactions INTEGER,
                timestamp TEXT
            )
        ''')
        self.conn.commit()

    def connection_open(self, db_path="database/economy.db"):
        # Initialize database connection
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(self.script_dir, db_path)
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def connection_close(self):
        # Close database connection
        self.conn.commit()
        self.conn.close()

    def user_exists(self, user_id):
        self.connection_open()
        # Check if user exists in database
        self.cursor.execute("SELECT * FROM accounts WHERE user_id=?", (user_id,))
        if self.cursor.fetchone():
            self.connection_close()
            return True
        else:
            self.connection_close()
            return False
    
    def transfer(self, sender_id,receiver_id, amount, description):
        # Transfer money from one account to another
        if self.user_exists(user_id=sender_id) == True and self.user_exists(user_id=receiver_id) == True:
            # Check if sender has enough money
            if self.get_balance(user_id=sender_id) < amount:
                return "ERR" # Not enough balance
            
            else:
                # Check if amount higher than transfer limit (stored in database)
                if self.get_balance(user_id=sender_id) - amount > self.get_transfer_limit(user_id=sender_id):
                    return "ERR" # Transfer limit exceeded
                
                else:
                    self.connection_open()
                    # Deduct sender id
                    self.cursor.execute("UPDATE accounts SET balance = balance - ? WHERE user_id = ?", (amount, sender_id))
                    # Increment receiver id
                    self.cursor.execute("UPDATE accounts SET balance = balance + ? WHERE user_id = ?", (amount, receiver_id))
                    # Update transaction count
                    self.cursor.execute("UPDATE accounts SET transactions = transactions + 1 WHERE user_id = ?", (sender_id,))

                    self.connection_close()
                    # Record transaction
                    self.tt.transaction_record(sender_id, receiver_id, amount, description, datetime.datetime.now())

        else:
            return False # User does not exist
    
    def get_balance(self, user_id):
        # Get balance of a user
        if self.user_exists(user_id=user_id) == True:
            self.connection_open()
            self.cursor.execute("SELECT balance FROM accounts WHERE user_id=?", (user_id,))
            data = self.cursor.fetchone()[0]

            self.connection_close()
            return data
        else:
            return False # User does not exist
    
    def set_balance(self, user_id, amount):
        if self.user_exists(user_id=user_id) == True:
            # Set balance of a user
            self.connection_open()
            self.cursor.execute("UPDATE accounts SET balance = ? WHERE user_id = ?", (amount, user_id))
            self.connection_close()
        else:
            return False # User does not exist
    
    def get_transfer_limit(self, user_id):
        # Get transfer limit of a user
        if self.user_exists(user_id=user_id) == True:
            self.connection_open()
            self.cursor.execute("SELECT transfer_limit FROM accounts where user_id=?", (user_id))
            self.connection_close()
            return self.cursor.fetchone()[0]
        else:
            return False # User does not exist

    def initialise(self, user_id):
        if self.user_exists(user_id=user_id) == True:
            return False # User already has an account
        else:
            self.connection_open()
            # Initialise account for the new user
            self.cursor.execute("INSERT INTO accounts (user_id, balance, transfer_limit, transactions) VALUES (?, ?, ?, ?)", (user_id, 100, 25000, 0))
            
            self.connection_close()

# Example usage:
if __name__ == "__main__":
    am = AccountManager()
    print(am.set_balance(1, 1000))
    print(am.get_balance(1))
    print(am.transfer(1,2,100, "test"))
    print(am.get_balance(1))
    print(am.get_balance(2))