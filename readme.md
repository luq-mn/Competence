# Competence

An economy/currency focused Discord bot, made as a fun part-time project, using the [pycord](https://pycord.dev/) and built-in SQLite3 Python libraries.

> [!WARNING]
> This bot is under active development, and may not be functioning as intended. Expect overhauls and bugs, and changes without prior notice.

## Features

- **Account Management**
  - Account overview (Work in Progress)
  - Account locking/unlocking with password protection
  - Account settings (Work in Progress)

- **Master Commands** (Admin only)
  - Pull updates from Git repository
  - Display bot information
  - Add all server members to the bot database
  - Load, reload, and unload bot extensions
  - Close the bot

- **Event Handling**
  - Automatically add new members to the database when joining a server
  - Log server join and leave events

- **General Commands**
  - Ping command to check bot latency

- **Statistics Tracking**
  - Log command usage and events for analysis

- **Database Integration**
  - Use SQLite3 for storing user data and statistics

## Notes

- This bot keeps track of all the commands invoked, transactions and other relevant actions. This data is stored in our database.

### To-do

#### Commands

- [ ] Account overview
- [x] Account locking
- [ ] Transfer cash to another user

#### Backend

- [ ] Enforce transfer cooldown, and account backend
- [ ] Add all user in server when join
