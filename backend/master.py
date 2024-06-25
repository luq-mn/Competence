class Master():
    def __init__(self, bot):
        self.bot = bot
        @self.bot.listen()
        async def on_message(message):
            print('one')
    
    def CommandManager(self):
        pass