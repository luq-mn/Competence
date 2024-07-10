import sqlite3, os, datetime

def get_datetime():
    return datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

class StatisticsTracker:
    def __init__(self):
        self.db_name = os.path.join(os.getcwd(), "backend", "database", "statistics.db")

        # Create table if it does not exist
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                # commands table (author_id, command, output, latency, timestamp)
                conn.execute("CREATE TABLE IF NOT EXISTS commands (author_id INTEGER, command TEXT, output TEXT, latency INTEGER, timestamp TEXT)")
                # events table (type, details, timestamp)
                conn.execute("CREATE TABLE IF NOT EXISTS events (type TEXT, details TEXT, timestamp TEXT)")
                # transactions table (sender_id, recipient_id, currency, amount, description, timestamp)
                conn.execute("CREATE TABLE IF NOT EXISTS transactions (sender_id INTEGER, recipient_id INTEGER, currency TEXT, amount FLOAT, description TEXT, timestamp TEXT)")
    
    # Log bot actions and master commands
    def event_log(self, action, details):
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                conn.execute("INSERT INTO events (type, details, timestamp) VALUES (?, ?, ?)", (action, details, get_datetime()))
                conn.commit()

                print(f"-\nBot action [{action}] with details [{details}]\n{get_datetime()}")

    # Log invoked commands
    def command_log(self, user_id, command, output, latency):
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                conn.execute("INSERT INTO commands (author_id, command, output, latency, timestamp) VALUES (?, ?, ?, ?, ?)", (user_id, command, output, latency, get_datetime()))
                conn.commit()

                print(f"-\nCommand '{command}' invoked by [{user_id}]\n{get_datetime()} | Latency: {latency}ms")
    
    # Log transactions
    def transaction_log(self, sender_id, recipient_id, currency, amount, description):
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                conn.execute("INSERT INTO transactions (sender_id, recipient_id, currency, amount, description, timestamp) VALUES (?, ?, ?, ?, ?, ?)", (sender_id, recipient_id, currency, amount, description, get_datetime()))
                conn.commit()

                print(f"-\nTransaction from [{sender_id}] to [{recipient_id}] of [{amount}] in {currency}\n{get_datetime()}")