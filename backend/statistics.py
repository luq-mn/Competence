import sqlite3
from main import get_datetime

class StatisticsTracker:
    def __init__(self):
        self.db_name = "backend/database/statistics.db"

        # Create table if it does not exist
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                conn.execute("CREATE TABLE IF NOT EXISTS commands (user_id INTEGER, command TEXT, output TEXT, timestamp TEXT)")
                conn.execute("CREATE TABLE IF NOT EXISTS transactions (sender_id INTEGER, receiver_id INTEGER, amount INTEGER, note TEXT, timestamp TEXT)")
                conn.commit()
    
    # Log invoked commands
    def command_log(self, user_id, command, output):
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                conn.execute("INSERT INTO commands (user_id, command, output, timestamp) VALUES (?, ?, ?, ?)", (user_id, command, output, get_datetime()))
                conn.commit()

                print(f"Command '{command}' invoked by user {user_id} at {get_datetime()}\nOutput: {output}")
    
    # Log transactions
    def transaction_log(self, sender_id, receiver_id, amount, note):
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                conn.execute("INSERT INTO transactions (sender_id, receiver_id, amount, note, timestamp) VALUES (?, ?, ?, ?, ?)", (sender_id, receiver_id, amount, note, get_datetime()))
                conn.commit()

                print(f"Transaction from {sender_id} to {receiver_id} of {amount} at {get_datetime()}")