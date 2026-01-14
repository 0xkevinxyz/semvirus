if __name__ == "__main__":
  import os 
  from .config.client import Client 
  from .config.constants import BOT_TOKEN 
  from .core.commands import load_commands
  
  ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
  
  # Instance the client 
  client = Client(bot_token=BOT_TOKEN)
  # Execute the function to load commands
  load_commands(client.tree, ROOT_DIR)
  # Starts the bot 
  client.start_bot()