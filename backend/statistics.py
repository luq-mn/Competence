import sqlite3, os, datetime

def get_datetime():
    return datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

class StatisticsTracker:
    def __init__(self):
        self.db_name = f"{os.getcwd()}/backend/database/statistics.db"

        # Create table if it does not exist
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                conn.execute("CREATE TABLE IF NOT EXISTS transactions (sender_id INTEGER, recipient_id INTEGER, amount INTEGER, note TEXT, timestamp TEXT)")
                conn.execute("CREATE TABLE IF NOT EXISTS commands (command TEXT, user_id INTEGER, latency INTEGER, timestamp TEXT)")
                conn.execute("CREATE TABLE IF NOT EXISTS bot (action TEXT, details TEXT, timestamp TEXT)")
                conn.commit()
    
    # Log bot actions and master commands
    def bot_log(self, action, details):
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                conn.execute("INSERT INTO bot (action, details, timestamp) VALUES (?, ?, ?)", (action, details, get_datetime()))
                conn.commit()

                print(f"-\nBot action [{action}] with details [{details}]\n{get_datetime()}")

    # Log invoked commands
    def command_log(self, user_id, command, latency):
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                conn.execute("INSERT INTO commands (user_id, command, latency, timestamp) VALUES (?, ?, ?, ?)", (user_id, command, latency, get_datetime()))
                conn.commit()

                print(f"-\nCommand '{command}' invoked by [{user_id}]\n{get_datetime()} | Latency: {latency}ms")
    
    # Log transactions
    def transaction_log(self, sender_id, recipient_id, amount, note):
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                conn.execute("INSERT INTO transactions (sender_id, recipient_id, amount, note, timestamp) VALUES (?, ?, ?, ?, ?)", (sender_id, recipient_id, amount, note, get_datetime()))
                conn.commit()

                print(f"-\nTransaction from [{sender_id}] to [{recipient_id}] of [{amount}]\n{get_datetime()}")