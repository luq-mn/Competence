import sqlite3, os, datetime

class AccountManager:
    def __init__(self):
        # Initialize database connection
        self.connection_open()

        # Create table (if not exists)
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                user_id TEXT PRIMARY KEY,
                balance INTEGER,
                limit INTEGER,
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
        self.conn.close()
    
    def transfer(self, receiver_id, amount):
        # Transfer money from one account to another
        pass

    def initialise(self, user_id):
        # Initialise account for a new user
        pass
    


# Example usage:
if __name__ == "__main__":
    acc = AccountManager()