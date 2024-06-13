import sqlite3
from main import datetime

class Coins:
    def __init__(self):
        self.db_name = "backend/database/coins.db"

        # Create table if not exists
        with sqlite3.connect(self.db_name) as conn:
            with conn:
                # Create table for coins
                conn.execute("""CREATE TABLE IF NOT EXISTS coins (
                    coin TEXT PRIMARY KEY,
                    
                    )
                """)

                # Create table for GPUs
                conn.execute("""CREATE TABLE IF NOT EXISTS gpus (
                    gpu_id TEXT PRIMARY KEY,
                    name TEXT,
                    mining_rate INTEGER,
                    price INTEGER
                    )
                """)
                # Create table for inventory
                conn.execute("""CREATE TABLE IF NOT EXISTS inventory (
                    user_id INTEGER,
                    gpu_id TEXT PRIMARY KEY,
                    amount INTEGER
                    )
                """)
                conn.commit()
    
    # Get all the GPUs (includes its id, price, etc)
    def gpu_get(self):
        pass

    # Buy GPU
    def gpu_buy(self, user_id, gpu_id, amount):
        pass

    # Sell GPU
    def gpu_sell(self, user_id, gpu_id, amount):
        pass