import discord
from discord.ext import commands
from settings import TOKEN, DATABASE_URL
from db import Database

class JungBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    async def setup(self):
        self.db = Database(database_url=DATABASE_URL)
        self.db.initialize_database()
        if self.db.connect:
            print("Database connection successful")
        else:
            print("Failed to connect to the database")
        
    async def setup_hook(self):
        await self.load_extension("cogs.messages.handler")
        await self.load_extension("cogs.voice.handler")
        await self.tree.sync()

    async def on_ready(self):
        print("===========")
        print(f"Login as {self.user.name}")
        print("===========")
        
        await self.setup()
        await self.change_presence(status=discord.Status.online, activity=discord.Game("Jung"))


intents = discord.Intents.default()
intents.message_content = True
bot = JungBot(command_prefix="/", intents=intents)

bot.run(TOKEN)
