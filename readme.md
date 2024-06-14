# Competence

An economy/currency focused Discord bot, made as a fun part-time project, using the [pycord](https://pycord.dev/) and built-in SQLite3 Python libraries.

> [!WARNING]
> This bot is under active development, and may not be functioning as intended. Expect regularmajorsignificant changes/overhauls.

## Features

Each feature is its own Cog-based extension, and can be reloaded without the bot restarting*.

----

### Account

An account is stored at the Competence database, with your user ID as the primary key. By default, an account has a balance of **$100**, a transfer limit of **$50000** per transaction, and the **clear** flag.

#### Flags

Competence features flags on accounts, which allows certain users to fall under certain restrictions if necessary. Below are the list of flags and their description.

- **master** - Competence accounts, only accessible via the backend or any users listed as bot admins. These accounts has no transfer limits, and its id are not based on any user.
- **clear** - Default flag. No restrictions, normal account.
- **watchlist** - No restrictions, but this flag means you are being watched by the admins.
- **restrict** - Transfer limit reduced to 10%, only transferring/receiving money is allowed.
- **blacklist** - Account is banned from using the bot's economy/currency features.

#### Commands

`account init`

Initialize your account. Invoking a command that requires access to your account will also initialise an account for you, if you have not done so.

`account balance`

Check for your the balance of your account.

`account transfer [receiver_id] [amount]`

Transfer money to another account. Subject to 2% transfer fee.

----

### Utility

Despite being an economy/currency focused bot, Competence provides you with basic utility features that other bots have (usually to test out something at the backend).

`user info`

Get information about a user.

`calculator [num_1] [operator] [num_2]>`

Basic calculator with adddition, subtraction, multiplication, division and modulus.

`ping`

Check the bot's latency.

## Notes

- The bot still requires a restart to load in new extensions.
- Commands invoked to this bot are logged and stored in a database. The database stores your user ID, guild ID, command used and the output.
