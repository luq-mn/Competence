# Competence

Economy/currency focused Discord bot, with virtual stock markets, trades and investments.

## Features

### Account

An account is stored at the Competence database, with your user ID as the primary key. By default, an account has a balance of **$100**, a transfer limit of **$50000** per transaction, and the **clear** flag.

#### Flags

Competence features flags on accounts, which allows certain users to fall under certain restrictions if necessary. Below are the list of flags and their description.

- **Master** - Competence accounts, only accessible via the backend or any users listed as bot admins. These accounts has no transfer limits, and its id are not based on any user.
- **Clear** - Default flag. No restrictions, normal account.
- **Watchlist** - No restrictions, but this flag means you are being watched by the admins.
- **Restrict** - Transfer limit reduced to 10%, only transferring/receiving money is allowed.
- **Blacklist** - Account is banned from using the bot's economy/currency features.

#### Commands

`account init`

Initialize your account. Invoking a command that requires access to your account will also initialise an account for you, if you have not done so.

`account balance`

Check for your the balance of your account.

### Utility

Despite being an economy/currency focused bot, Competence provides you with basic utility features that other bots have (usually to test out something at the backend).

`user info`

Get information about a user.

`calculator [num_1] [operator] [num_2]>`

Basic calculator with adddition, subtraction, multiplication, division and modulus.

`ping`

Check the bot's latency.

## Notes

- Commands invoked to this bot are logged and stored in a database. The database stores your user ID, guild ID, command used and the output.
- Types of flags on your account:
**Master** (Competence account, has no owner)
**Clear** (no restrictions, normal account),
**Watchlist** (clear, but this flag is not good.),
**Restrict** (transfer limit reduced to 10%, only transferring/receiving money is allowed.),
**Blacklist** (account is banned from using the bot).
- Each account has a default transfer limit of **$50000**.
