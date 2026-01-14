import os 
import importlib.util
from discord import app_commands 

# Functon to load the slash commands
# /commands/slash/category/command_module.py
def load_commands(app: app_commands.CommandTree, root_dir: str) -> None:
  command_main_path = os.path.join(root_dir, "commands", "slash")
  
  for categorys in os.listdir(command_main_path):
    if categorys.startswith("__init__"):
      continue 
    
    command_files_path = os.path.join(root_dir, "commands", "slash", categorys)
    
    for command_files in os.listdir(command_files_path):
      if not command_files.endswith(".py") or command_files.startswith("__init__"):
        continue 
      
      module_name = f"{command_main_path}.{categorys}.{command_files[:-3]}"
      module_loc = os.path.join(root_dir, "commands", "slash", categorys, command_files)
      
      module_spec = importlib.util.spec_from_file_location(module_name, module_loc)
      module = importlib.util.module_from_spec(module_spec)
      module_spec.loader.exec_module(module)
      
      try:
        # Checks if the module has the setup function 
        if hasattr(module, "setup"):
          # Execute the setup function to add the command
          module.setup(app)
          
      except Exception as err:
        print(err) 