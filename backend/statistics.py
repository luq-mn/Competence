import sqlite3
import os

class StatisticsTracker:
    def __init__(self):
        # Initialize database connection
        self.connection_open()

        # Create table (if not exists)
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS commands (
                author_id TEXT,
                guild_id TEXT,
                command TEXT,
                output TEXT
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
        self.conn.close()

    def command_invoked(self, author_id, guild_id, command, output):
        # Track command in database
        self.cursor.execute(f"""
            INSERT INTO commands (author_id, guild_id, command, output) 
            VALUES (?, ?, ?, ?)
        """, (author_id, guild_id, command, output))
        self.conn.commit()
        print(f"Command '{command}' invoked by {author_id} in {guild_id}\n- Output: {output}")
        self.connection_close()

# Example usage:
if __name__ == "__main__":
    tracker = StatisticsTracker()
    tracker.command_invoked("1234567890", "9876543210", "ping", "Pong!")