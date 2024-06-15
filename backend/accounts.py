import json
import os

from .statistics import StatisticsTracker
stats = StatisticsTracker()

class AccountManager:
    def __init__(self):
        self.db_name = 'backend/database/users.json'
        if not os.path.exists(self.db_name):
            self.data = {
                "accounts": [],
                "debts": [],
                "properties": []
            }
            self._save_data()
        else:
            self._load_data()

    def _load_data(self):
        with open(self.db_name, 'r') as f:
            self.data = json.load(f)

    def _save_data(self):
        with open(self.db_name, 'w') as f:
            json.dump(self.data, f, indent=4)
    
    def _find_account(self, user_id):
        for account in self.data['accounts']:
            if account['user_id'] == user_id:
                return account
        return None

    def account_check(self, user_id):
        self._load_data()
        if self._find_account(user_id):
            return True
        else:
            self.account_init(user_id)
            return False

    def account_init(self, user_id):
        self.data['accounts'].append({
            "user_id": user_id,
            "balance": 100,
            "tier": 1,
            "flag": "clear"
        })
        self._save_data()

    def account_balance(self, user_id):
        self.account_check(user_id)
        account = self._find_account(user_id)
        return account['balance'] if account else None

    def account_tier(self, user_id):
        self.account_check(user_id)
        account = self._find_account(user_id)
        tier = account['tier'] if account else None

        if user_id in [0, 1, 2]:
            return {"tier": 0, "transfer_limit": 0, "transfer_fee": 0, "debt_limit": 0, "debt_interest": 0}
        elif tier == 1:
            return {"tier": 1, "transfer_limit": 2000, "transfer_fee": 0.05, "debt_limit": 10000, "debt_interest": 0.03}
    
    def account_transfer(self, user_id, recipient_id, amount, note):
        self.account_check(user_id)
        self.account_check(recipient_id)

        user_account = self._find_account(user_id)
        recipient_account = self._find_account(recipient_id)

        balance = user_account['balance']
        tier = self.account_tier(user_id)

        if amount < balance:
            if tier["transfer_limit"] == 0 or amount < tier["transfer_limit"]:
                user_account['balance'] -= amount
                recipient_account['balance'] += amount
                self._save_data()

                stats.transaction_log(user_id, recipient_id, amount, note)

                return "success"
            else:
                return "exceed"
        else:
            return "insufficient"
