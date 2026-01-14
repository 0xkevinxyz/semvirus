import discord 
from discord import app_commands

# Class to instance the discord client
class Client(discord.Client):
  def __init__(self, bot_token: str) -> None:
    super().__init__(
      intents=discord.Intents.all()
    )
    
    # Token of the bot 
    self.token = bot_token
    self.tree = app_commands.CommandTree(self)
    
  async def on_ready(self) -> None:
    await self.tree.sync()
    
    print(f"Bot logged as {self.user.name}")
  
  # Function to run the bot
  def start_bot(self) -> None:
    self.run(self.token)