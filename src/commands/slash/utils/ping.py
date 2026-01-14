from discord import app_commands, Interaction 

class Ping(app_commands.Command):
  def __init__(self):
    super().__init__(
      name="ping",
      description="Replys with pong",
      callback=self.callback 
    )
    
  async def callback(self, interaction: Interaction):
    await interaction.response.send_message(content="Pong!")
    
def setup(app: app_commands.CommandTree):
  app.add_command(Ping())