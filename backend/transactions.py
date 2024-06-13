# Tracks transactions related metric
import sqlite3, os, datetime

class TransactionsTracker:
    def __init__(self):
        # Initialize database connection
        self.connection_open()

        # Create table (if not exists)
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                sender_id INTEGER,
                receiver_id INTEGER,
                amount INTEGER,
                description TEXT,
                timestamp TEXT
            )
        ''')
        self.conn.commit()

    def connection_open(self, db_path="database/statistics.db"):
        # Initialize database connection
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(self.script_dir, db_path)
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def connection_close(self):
        # Close database connection
        self.conn.commit()
        self.conn.close()

    def transaction_record(self, sender_id, receiver_id, amount, description, timestamp):
        self.connection_open()
        # Insert transaction record into database
        self.cursor.execute('''
            INSERT INTO transactions (sender_id, receiver_id, amount, description, timestamp)
            VALUES (?, ?, ?, ?, ?)
        ''', (sender_id, receiver_id, amount, description, timestamp)
        )
        self.connection_close()
        print(f"Transaction recorded from {sender_id} to {receiver_id} for {amount} with description '{description}' at {timestamp}.")

# Example usage:
if __name__ == "__main__":
    tracker = TransactionsTracker()