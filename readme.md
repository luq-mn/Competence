# Competence

An economy/currency focused Discord bot, made as a fun part-time project, using the [pycord](https://pycord.dev/) and built-in SQLite3 Python libraries.

> [!WARNING]
> This bot is under active development, and may not be functioning as intended. Expect regularmajorsignificant changes/overhauls.

## Features

Each feature is its own Cog-based extension, and can be reloaded without the bot restarting*.

----

### Account

An account is stored at the Competence database, with each user having their own dedicated account. Each account consists of the user id, balance, [tier](#different-tiers-for-your-account), and [flag](#account-flags).

Quicklink:
[Flags](#account-flags), [Tiers](#different-tiers-for-your-account), [Commands](#account-commands)

#### Account flags

Competence features flags on accounts, which allows certain users to fall under certain restrictions if necessary. Below are the list of flags and their description.

- **master** - Competence accounts, only accessible via the backend or any users listed as bot admins. Read [more](#master-accounts).
- **clear** - Default flag. No restrictions, normal account.
- **watchlist** - No restrictions, but this flag means you are being watched by the admins.
- **restrict** - Transfer limit reduced to 10%, only transferring/receiving money is allowed.
- **blacklist** - Account is banned from using the bot's economy/currency features.

#### Different Tiers for your Account

Tiers will inherit all the privileges available from the previous tiers, however, does not inherit its requirements.

|Tier|Transfer Limit, Fee|Debt Limit, Interest|Upgrade fees|Requirements|Privileges|
|----|-------------------|--------------------|------------|------------|----------|
|1|$2000, 5.00%|$10000, 3.00%|None|None|Default|
|2|$5000, 4.70%|$30000, 2.75%|$10000|Min 2 owned properties|None|
|3|$10000, 4.20%|$80000, 2.30%|$20000|Collected rent at least 5x times|Investing in loan pool|
|4|$25000, 3.60%|$200000, 2.05%|$50000|Bought min 15 items from the commodities store|None|
|5|$75000, 3.15%|$500000, 1.90%|$150000|None|None|
|6|$150000, 2.50%|$2000000, 1.65%|$300000|None|None|
|7|$500000, 2.20%|$5000000, 1.40%|$1000000|Min 10 owned properties|Build properties|
|8|$1200000, 1.80%|$12000000, 1.10%|$3000000|None|None|
|9|$5000000, 1.25%|$50000000, 0.60%|$100000000|None|None|
|10|No limit, 0.75%|No limit, 0.55%|$250000000|None|None|
|11|No limit, 0%|No limit, 0.20%|$1000000000|Top 111 richest|None|

#### Master accounts

Master accounts are accounts used by Competence. Unlike other accounts which uses the owner's ID as its identifier, these accounts use values 0, 1, and 2 as its id.

- **Master account 0** - Owns everything apart from properties. Transfer fees, debt collection and other forms of transactions between the user and the bot are stored here.
- **Master account 1** - Responsible for purchasing properties from selling users, and ownership of all the properties in the store.
- **Master account 2** - Manages the loan pool. Distributes its collection to all investors, which also includes account 0.

#### Account commands

`account init` - Initializes your account. Invoking a command that requires access to your account will also initialize an account for you, if you have not done so.

WIP - `account overview` - Shows an overview of your account, the balance, debt (total, interest, days), coins and amount of properties.

`account balance [type]` - Check for the balance of your account. Select between balance of coin or currency.

`account transfer [receiver_id] [amount]` - Transfer money to another account. Subject to transfer fees based on your account's [tier](#different-tiers-for-your-account).

WIP - `account upgrade` - Opens the upgrade menu.

----

### Property (WIP)

Allows you to buy, trade and sell properties. All accounts initializes with a starter house included, which can be sold for a quick buck. You can collect daily rent from the properties you own.

#### Property Value Mechanic

All properties from the store is held by master account 1. This account also purchases the properties you are selling, for 90% of the total value. There are a **limited** amount of property, with each purchase decreasing the supply and incrementing the market price by 0.5%.

#### Property commands

`property list` - Opens the property interface, with options to select a property, build, buy or sell.

`property rent` - Collect rent from your properties.

`property buy [property] [amount]` - Purchase an amount of the specified property from the store.

`property sell [property] [amount]` - Sell an amount of the specified property.

`property build [property] [amount]` - Build an amount of the specified property. **Requires a [tier](#different-tiers-for-your-account) 7 account.**

`property give [property] [user] [amount]` - Give owned property to another user.

----

### Utility

Despite being an economy/currency focused bot, Competence provides you with basic utility features that other bots have (usually to test out something at the backend).

`user info` - Get information about a user.

`calculator [num_1] [operator] [num_2]>` - Basic calculator with adddition, subtraction, multiplication, division and modulus.

`ping` - Check the bot's latency.

----

## Notes

- The bot still requires a restart to load in new extensions.
- Commands invoked to this bot are logged and stored in a database. The database stores your user ID, guild ID, command used and the output.

### To-do

- [ ] Account overview, upgrade
- [ ] Enforce transfer cooldown, and flagging
- [ ] Property backend
- [ ] Property commands
